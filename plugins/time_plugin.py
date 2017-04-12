#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  time_plugin.py

#  STORM BOT BY ALI

import string,re

time_pending=[]		
	
def handler_gettime_xep_disco(type, source, parameters):
	if parameters.strip():
		jid=source[1]+'/'+parameters.strip().strip()
		if GROUPCHATS.has_key(source[1]) and GROUPCHATS[source[1]].has_key(parameters.strip()):
			if GROUPCHATS[source[1]][parameters.strip()].has_key('timexep'):
				if GROUPCHATS[source[1]][parameters.strip()]['timexep']:
					gettime_xep0202(type,source,jid,parameters.strip())
					return
				else:
					gettime_xep0090(type,source,jid,parameters.strip())
					return
		else:
			reply(type,source, u'بالله كان هون ولو ؟ :-O')
			return
	else:
		jid=source[1]+'/'+source[2]
		if GROUPCHATS[source[1]][source[2]].has_key('timexep'):
			if GROUPCHATS[source[1]][source[2]]['timexep']:
				gettime_xep0202(type,source,jid,source[2])
				return
			else:
				gettime_xep0090(type,source,jid,source[2])
				return
	iq = xmpp.Iq('get')
	iq.setTo(jid)
	id='info'+str(random.randrange(1000, 9999))
	globals()['time_pending'].append(id)
	iq.setID(id)
	iq.addChild('query', {}, [], 'http://jabber.org/protocol/disco#info')
	JCON.SendAndCallForResponse(iq, handler_gettime_xep_disco_answ, {'type': type, 'source': source, 'parameters': parameters.strip(), 'jid':jid})

		
def handler_gettime_xep_disco_answ(coze, res, type, source, parameters, jid):
	id=res.getID()
	if id in globals()['time_pending']:
		globals()['time_pending'].remove(id)
	else:
		print 'اووووبس....'
		return
	rep =''
	if res:
		if not res.getType() == 'result':
			reply(type,source,u'لا جواب')
			return			
		res=res.getQueryChildren()
		for x in res:
			att=x.getAttrs()
			if att.has_key('var'):
				att=att['var']
				if att == 'urn:xmpp:time':
					if parameters.strip():
						GROUPCHATS[source[1]][parameters.strip()]['timexep'] = 1	
					else:
						GROUPCHATS[source[1]][source[2]]['timexep'] = 1	
					gettime_xep0202(type,source,jid,parameters.strip())
					return
		if parameters.strip():
			if GROUPCHATS.has_key(source[1]) and GROUPCHATS[source[1]].has_key(parameters.strip()):
				GROUPCHATS[source[1]][parameters.strip()]['timexep'] = 0
			else:
				reply(type,source, u'بالله كان هون ولو ؟ :-O')
				return
		else:
			if GROUPCHATS.has_key(source[1]) and GROUPCHATS[source[1]].has_key(source[2]):
				GROUPCHATS[source[1]][source[2]]['timexep'] = 0
			else:
				reply(type,source, u'بالله كان هون ولو ؟ :-O')
				return
		gettime_xep0090(type,source,jid,parameters.strip())
	else:
		reply(type,source,u'نفذ الوقت')
		return


def gettime_xep0090(type,source,jid,param=''):
	nick=''
	if param:
		nick=param
	time_iq = xmpp.Iq('get')
	id='time'+str(random.randrange(1000, 9999))
	globals()['time_pending'].append(id)
	time_iq.setID(id)
	time_iq.addChild('query', {}, [], 'jabber:iq:time');
	time_iq.setTo(jid)
	JCON.SendAndCallForResponse(time_iq, gettime_xep0090_answ, {'type': type, 'source': source, 'nick':nick})
	
	
def gettime_xep0090_answ(coze, res, nick, type, source):
	id=res.getID()
	if id in globals()['time_pending']:
		globals()['time_pending'].remove(id)
	else:
		print 'oooops...'
		reply(type,source, u'glitch')
	if res:
		if res.getType()=='error':
			if nick:
				reply(type,source, u'جهازك ليس جيدا')
			else:
				reply(type,source, u'جهازه ليس جيدا')
		elif res.getType() == 'result':
			time = ''
			props = res.getQueryChildren()
			for p in props:
				if p.getName() == 'عدم تفعيل':
					time = p.getData()
			if time:
				if nick:
					reply(type,source, u'الى <'+nick+ u'> الان ' +time)
				else:
					reply(type,source, u'الــــ♥ـــوقت الآن '+time)
	else:
		reply(type,source, u'شيء بأي شكل من الأشكال ...')
		
		
def gettime_xep0202(type,source,jid,param=''):
	nick=''
	if param:
		nick=param
	time_iq = xmpp.Iq('get')
	id='time'+str(random.randrange(1000, 9999))
	globals()['time_pending'].append(id)
	time_iq.setID(id)
	time_iq.addChild('time', {}, [], 'urn:xmpp:time');
	time_iq.setTo(jid)
	JCON.SendAndCallForResponse(time_iq, gettime_xep0202_answ, {'type': type, 'source': source, 'nick':nick})
	
	
def gettime_xep0202_answ(coze, res, nick, type, source):
	id=res.getID()
	if id in globals()['time_pending']:
		globals()['time_pending'].remove(id)
	else:
		print 'oooops...'
		reply(type,source, u'glitch')
	if res:
		if res.getType()=='خطأ':
			if nick:
				reply(type,source, u'جهازك ليس جيدا')
			else:
				reply(type,source, u'جهازه ليس جيدا')
		elif res.getType() == 'result':
			tzo = ''
			utc = ''
			props = res.getChildren()
			for p in props:
				tzo = p.getTagData('tzo')
				utc = p.getTagData('utc')
			if tzo and utc:
				try:
					[sign, tzh, tzm] = re.match('(\+|-)?([0-9]+):([0-9]+)',tzo).groups()
					[year, month, day, hours, minutes, seconds] = re.match('([0-9]+)-([0-9]+)-([0-9]+)T([0-9]+):([0-9]+):([0-9]+)',utc).groups()
				except:
					reply(type,source, u'ليس تحليل: (')
					return
				if sign == '-':
					hours=int(hours)-int(tzh)
					minutes=int(minutes)-int(tzm)
				else:
					hours=int(hours)+int(tzh)
					minutes=int(minutes)+int(tzm)
				if hours >= 24: day = int(day) + 1
				while hours>=24:
					hours=int(hours)-24
				while minutes>=60:
					minutes=int(minutes)-60
				if len(str(hours))==1:
					hours='0'+str(hours)
				if len(str(minutes))==1:
					minutes='0'+str(minutes)
				if len(str(seconds))==1:
					seconds='0'+str(seconds)				
				time=str(hours)+':'+str(minutes)+':'+str(seconds)
				date=str(year)+'-'+str(month)+'-'+str(day)
				if nick:
					reply(type,source, u'الى '+nick+u' الان '+time+' ('+date+')')
				else:
					reply(type,source, u'اليك الان '+time+' ('+date+')')
			else:
				reply(type,source, u'جهازك سيئ')
	else:
		reply(type,source, u'شيء بأي شكل من الأشكال ...')

register_command_handler(handler_gettime_xep_disco, 'الوقت', ['muc','info','all'], 10, 'Shows time of the indicated nick.', 'time <nick>', ['time','time guy'])
