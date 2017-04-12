#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  vcard_plugin.py

#  STORM BOT BY ALI

vcard_pending=[]

def order_kick(groupchat, nick, reason):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	kick=query.addChild('item', {'nick':nick, 'role':'none'})
	kick.setTagData('reason', get_bot_nick(groupchat)+': '+reason)
	iq.addChild(node=query)
	JCON.send(iq)
	
def order_visitor(groupchat, nick, reason):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	visitor=query.addChild('item', {'nick':nick, 'role':'visitor'})
	visitor.setTagData('reason', get_bot_nick(groupchat)+u': '+reason)
	iq.addChild(node=query)
	JCON.send(iq)
	
def order_ban(groupchat, nick, reason):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	ban=query.addChild('item', {'nick':nick, 'affiliation':'outcast'})
	ban.setTagData('reason', get_bot_nick(groupchat)+u': '+reason)
	iq.addChild(node=query)
	JCON.send(iq)
	
def order_unban(groupchat, jid):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	query.addChild('item', {'jid':jid, 'affiliation':'none'})
	iq.addChild(node=query)
	JCON.send(iq)

def get_novcard_state(gch):
	if not 'novcard' in GCHCFGS[gch]:
		GCHCFGS[gch]['novcard']={'res':'ignore','mess':u'املأ افيزتك حتى نتاكد انك لست فيرس'}

def handler_vcardget(type, source, parameters):
	vcard_iq = xmpp.Iq('get')
	id='vcard'+str(random.randrange(1000, 9999))
	globals()['vcard_pending'].append(id)
	vcard_iq.setID(id)
	vcard_iq.addChild('vCard', {}, [], 'vcard-temp');
	if parameters:
		if GROUPCHATS.has_key(source[1]):
			nicks = GROUPCHATS[source[1]].keys()
			nick = parameters.strip()
			if not nick in nicks:
				vcard_iq.setTo(nick)
			else:
				if GROUPCHATS[source[1]][nick]['ishere']==0:
					reply(type, source, u'هل انت متاكد ان هذا المستخدم هنا؟ :-O')
					return				
				jid=source[1]+'/'+nick
				vcard_iq.setTo(jid)
	else:
		jid=source[1]+'/'+source[2]
		vcard_iq.setTo(jid)
		nick=''
	JCON.SendAndCallForResponse(vcard_iq, handler_vcardget_answ, {'type': type, 'source': source, 'nick': nick})
		
def handler_vcardget_answ(coze, res, type, source, nick):
	id=res.getID()
	if id in globals()['vcard_pending']:
		globals()['vcard_pending'].remove(id)
	else:
		print 'اوووووووووبس!'
		return
	rep =''
	if res:
		if res.getType()=='خطأ':
			if not nick:
				reply(type,source,u'انت ليس لديك فيزا :-P')
				return
			else:
				reply(type,source,u'هذا المستخدم ليش لديه فيزا')
				return
		elif res.getType() == 'نتيجة':
			name,nickname,url,email,desc = '','','','',''
			if res.getChildren():
				props = res.getChildren()[0].getChildren()
			else:
				if not nick:
					reply(type,source,u'فيزتك خاليه ;-)')
					return
				else:
					reply(type,source,u'فيزته خاليه ;-) ')
					return
			for p in props:
				if p.getName() == 'NICKNAME':
					nickname = p.getData()
				if p.getName() == 'FN':
					name = p.getData()				
				if p.getName() == 'URL':
					url = p.getData()
				if p.getName() == 'EMAIL':
					email = p.getData()
				if p.getName() == 'DESC':
					desc = p.getData()
			if nickname:
				if not nick:
					rep = u'فيزتك هي :\nnick: '+nickname
				else:
					rep = u'هذا هو '+nick+u' vCard:\nnick: '+nickname
			if not name=='':
				rep +='\nName: '+name				
			if not url=='':
				rep +='\nURL: '+url
			if not email=='':
				rep +=u'\nE-mail: '+email		
			if not desc=='':
				rep +=u'\nAbout: '+desc
			if rep=='':
				rep = u'فيزا خاليه...'
		else:
			rep = u'He |-)'
	else:
		rep = u'شيء بأي حال من الأحوال ...'
	reply(type, source, rep)

def handler_novcard_join(groupchat, nick, aff, role):
	nvcres = GCHCFGS[groupchat]['novcard']['res']
	jid = groupchat+'/'+nick	
		
	type = 'جمهور'
	source = [groupchat+'/'+nick,groupchat,nick]
		
	if aff == 'none' and nvcres != 'ignore':
		vcard_iq = xmpp.Iq('get')
		id='vcard'+str(random.randrange(1000, 9999))
		globals()['vcard_pending'].append(id)
		vcard_iq.setID(id)
		vcard_iq.addChild('vCard', {}, [], 'vcard-temp')
		vcard_iq.setTo(jid)
		JCON.SendAndCallForResponse(vcard_iq, handler_novcardget_answ, {'type': type, 'source': source, 'nick': nick})

def handler_novcardget_answ(coze, res, type, source, nick):
	groupchat = source[1]
	id=res.getID()
	if id in globals()['vcard_pending']:
		globals()['vcard_pending'].remove(id)
	else:
		print 'اوووووووووبس!'
		return
	
	rep = 0
	nvcres = ''
	nvcmess = ''
	
	if res:
		if res.getType()=='خطأ':
			nvcres = GCHCFGS[groupchat]['novcard']['res'].strip()
			nvcmess = GCHCFGS[groupchat]['novcard']['mess']
		elif res.getType() == 'نتيجة':
			name,nickname,url,email,desc,photo,adr,bday,gender,nn,org,tel = '','','','','',None,'','','','','',''
			props = None
			
			if res.getChildren():
				props = res.getChildren()[0].getChildren()
			else:	
				nvcres = GCHCFGS[groupchat]['novcard']['res'].strip()
				nvcmess = GCHCFGS[groupchat]['novcard']['mess']
			
			if not props:	
				nvcres = GCHCFGS[groupchat]['novcard']['res'].strip()
				nvcmess = GCHCFGS[groupchat]['novcard']['mess']
							
	if nvcres:
		if nvcres == 'kick':
			order_kick(groupchat, nick, nvcmess)
		elif nvcres == 'ban':
			order_ban(groupchat, nick, nvcmess)
		elif nvcres == 'visitor':
			order_visitor(groupchat, nick, nvcmess)
#			msg(groupchat+'/'+nick,nvcmess)
			reply(type, source, nvcmess)

def handler_novcard_res(type, source, parameters):
	groupchat = source[1]
	
	if not GROUPCHATS.has_key(groupchat):
		reply(type, source, u'يمكن استخدام هذا الامر فقط فى الرومات')
		return
	
	if parameters:
		if not parameters.strip() in ['ignore','kick','ban','visitor']:
			reply(type,source,u'خطأ في بناء الجملة :ermm:')
			return
		
		GCHCFGS[groupchat]['novcard']['res']=parameters.strip()
		reply(type,source,u'رد فعل الفيزا الخاليه هو'+parameters.strip()+'.')
		
		write_file('dynamic/'+groupchat+'/config.cfg', str(GCHCFGS[groupchat]))
	else:
		reply(type,source,u'رد فعل الفيزا الخاليه هو: '+GCHCFGS[groupchat]['novcard']['res']+'.')
		
def handler_novcard_mess(type, source, parameters):
	groupchat = source[1]
	
	if not GROUPCHATS.has_key(groupchat):
		reply(type, source, u'يمكن استخدام هذا الامر فقط فى الرومات')
		return
	
	if parameters:
		GCHCFGS[groupchat]['novcard']['mess']=parameters.strip()
		reply(type,source,u'يتم الاستجابه لرساله الفيزا')
		
		write_file('dynamic/'+groupchat+'/config.cfg', str(GCHCFGS[groupchat]))
	else:
		reply(type,source,u'يتم الاستجابه لرساله الفيزا وهيه: '+GCHCFGS[groupchat]['novcard']['mess'])

register_command_handler(handler_novcard_mess, 'رساله-فيزا-خاليه', ['عام','معلومات','الكل'], 20, 'يحدد أو يعرض رسالة في رد فعل على بصيغة بطاقة فارغة.', 'رساله-فيزا-خاليه <رساله>', ['رساله-فيزا-خاليه شغل بصيغة بطاقة الخاصة بك، ثم الحديث!','رساله-فيزا-خاليه'])
register_command_handler(handler_novcard_res, 'ريسورس-فيزا-خاليه', ['عام','معلومات','الكل'], 20, 'يحدد أو يوضح رد فعل من بوت على بصيغة بطاقة فارغة: تجاهل, طرد, فصل, نسخه.', 'novc_res [تجاهل|طرد|فصل|نسخه]', ['ريسورس-فيزا-خاليه طرد','ريسورس-فيزا-خاليه فصل','ريسورس-فيزا-خاليه'])
register_command_handler(handler_vcardget, 'فيزا', ['عام','معلومات','الكل'], 10, 'يعرض بصيغة بطاقة المستخدم المحدد.', 'فيزا [اسم]', ['فيزا شخص','فيزا'])

register_stage1_init(get_novcard_state)
register_join_handler(handler_novcard_join)
