#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  idle_plugin.py

#  STORM BOT BY ALI

idle_pending=[]
def handler_idle(type, source, parameters):
	idle_iq = xmpp.Iq('get')
	id='idle'+str(random.randrange(1000, 9999))
	globals()['idle_pending'].append(id)
	idle_iq.setID(id)
	idle_iq.addChild('query', {}, [], 'jabber:iq:last');
	if parameters:
		param = parameters.strip()
		idle_iq.setTo(param)
	else:
		param=CONNECT_SERVER
		idle_iq.setTo(param)
	JCON.SendAndCallForResponse(idle_iq, handler_idle_answ, {'type': type, 'source': source, 'param': param})
	
		
def handler_idle_answ(coze, res, type, source, param):
	id=res.getID()
	if id in globals()['idle_pending']:
		globals()['idle_pending'].remove(id)
	else:
		print 'ooops!'
		return
	rep =''
	if res:
		if res.getType()=='error':
			reply(type,source,u'سرفر جابر غير موجود او موقوف مؤقتا')
			return
		elif res.getType() == 'result':
			sec = ''
			props = res.getPayload()
			if not props:
				reply(type,source,u'تم ايقاف هذا السرفر')
				return 
			for p in props:
				sec=p.getAttrs()['seconds']
				if not sec == '0':
					rep = param+u' يعمل حاليا ل  '+timeElapsed(int(sec))
	else:
		rep = u'bug'
	reply(type, source, rep)

def handler_userinfo_idle(type, source, parameters):
	if GROUPCHATS.has_key(source[1]):
		if not parameters:
			reply(type,source,u'and?')
			return
		nick = parameters.strip()
		if nick==source[2]:
			reply(type,source,u'ماذا يجب ان اقول؟ ;)')
			return
		if GROUPCHATS[source[1]].has_key(nick) and GROUPCHATS[source[1]][nick]['ishere']==1:
			groupchat = source[1]
			idletime = int(time.time() - GROUPCHATS[groupchat][nick]['idle'])
			reply(type, source, nick+u' sleep '+timeElapsed(idletime)+u' ago')
		else:
			reply(type,source,u'هل كان هنا؟ :-O')
			

register_command_handler(handler_idle, 'وقت-السرفر', ['info','muc','all'], 10, 'Show uptime of certain server.', 'uptime <server>', ['uptine jsmart.web.id'])
register_command_handler(handler_userinfo_idle, 'مده-الزائر', ['info','muc','all'], 10, 'Shows how long a user is nonactive.', 'idle <nick>', ['idle guy'])
