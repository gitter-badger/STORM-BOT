#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  version_plugin.py

#  STORM BOT BY ALI

version_pending=[]
def handler_version(type, source, parameters):
	nick = source[2]
	groupchat=source[1]
	iq = xmpp.Iq('get')
	id='vers'+str(random.randrange(1000, 9999))
	globals()['version_pending'].append(id)
	iq.setID(id)
	iq.addChild('query', {}, [], 'jabber:iq:version');
	if parameters:
		jid=groupchat+'/'+parameters.strip()
		if GROUPCHATS.has_key(groupchat):
			nicks = GROUPCHATS[groupchat].keys()
			param = parameters.strip()
			if not nick in nicks:
				iq.setTo(param)
			else:
				if GROUPCHATS[groupchat][nick]['ishere']==0:
					reply(type, source, u'هل كان هنا؟ :-O')
					return
				iq.setTo(jid)
	else:
		jid=groupchat+'/'+nick
		iq.setTo(jid)
	JCON.SendAndCallForResponse(iq, handler_version_answ, {'type': type, 'source': source})
	return

def handler_version_answ(coze, res, type, source):
	id=res.getID()
	if id in globals()['version_pending']:
		globals()['version_pending'].remove(id)
	else:
		print 'someone is doing wrong...'
		return
	rep =''
	if res:
		if res.getType() == 'result':
			name = '[no name]'
			version = '[no ver]'
			os = '[no os]'
			props = res.getQueryChildren()
			for p in props:
				if p.getName() == 'name':
					name = p.getData()
				elif p.getName() == 'version':
					version = p.getData()
				elif p.getName() == 'os':
					os = p.getData()
			if name:
				rep = u'\nالـبـرنـامـج    :' u'  '+name+u'\n'
			if version:
				rep +=u'الإصدار :' u'  '+version+u'\n'
			if os:
				rep +=u'الـنـسـخـه    :' u'  '+os
		else:
			rep = u'ليس هنا :-| '
	else:
		rep = u'لا شيئ مثل ذلك'
	reply(type, source, rep)
	
register_command_handler(handler_version, 'نسخة', ['معلومات','عام','الكل'], 0, 'لعرض نسخه اي شخص .', 'نسخة [اسم \ الملقم]', ['نسخة','نسخة شخص','نسخة jabbe.org'])
