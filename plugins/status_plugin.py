#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  status_plugin.py

#  STORM BOT BY ALI

def handler_status(type, source, parameters):
	if parameters:
		if GROUPCHATS.has_key(source[1]) and GROUPCHATS[source[1]].has_key(parameters):
			stmsg=GROUPCHATS[source[1]][parameters]['stmsg']
			status=GROUPCHATS[source[1]][parameters]['status']
			if stmsg:
				reply(type,source, parameters+u' الان '+status+u' ('+stmsg+u')')
			else:
				reply(type,source, parameters+u' الان '+status)
		else:
			reply(type,source, u'بالله كان هون ؟ :-O')
	else:
		if GROUPCHATS.has_key(source[1]) and GROUPCHATS[source[1]].has_key(source[2]):
			stmsg=GROUPCHATS[source[1]][source[2]]['stmsg']
			status=GROUPCHATS[source[1]][source[2]]['status']
			if stmsg:
				reply(type,source, u'حالتك هى  ;-) '+status+u' ('+stmsg+u')')
			else:
				reply(type,source, u'حالتك هى  ;-) '+status)

def status_change(prs):
	groupchat = prs.getFrom().getStripped()
	nick = prs.getFrom().getResource()
	stmsg = prs.getStatus()
	if not stmsg:
		stmsg=''
	status = prs.getShow()
	if not status:
		status=u'online'
	if groupchat in GROUPCHATS and nick in GROUPCHATS[groupchat]:
		GROUPCHATS[groupchat][nick]['status']=status
		GROUPCHATS[groupchat][nick]['stmsg']=stmsg


register_presence_handler(status_change)
register_command_handler(handler_status, 'حاله', ['info','muc','all'], 0, 'Shows status and status report (if available) of certain user or itself.', 'status <user>', ['status', 'status guy'])
