#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  admin_plugin.py

#  STORM BOT BY ALI

def popups_check(gch):
	DBPATH='dynamic/'+gch+'/config.cfg'
	if GCHCFGS[gch].has_key('popups'):
		if GCHCFGS[gch]['popups'] == 1:
			return 1
		else:
			return 0
	else:
		GCHCFGS[gch]['popups']=1
		write_file(DBPATH,str(GCHCFGS[gch]))
		return 1
				
def handler_admin_join(type, source, parameters):
	if parameters:
		passw=''
		args = parameters.split()
		if len(args)>1:
			groupchat = args[0]
			passw = string.split(args[1], 'pass=', 1)
			if not passw[0]:
				reason = ' '.join(args[2:])
			else:
				reason = ' '.join(args[1:])
		else:
			groupchat = parameters
			reason = ''
		get_gch_cfg(groupchat)
		for process in STAGE1_INIT:
			with smph:
				INFO['thr'] += 1
				threading.Thread(None,process,'atjoin_init'+str(INFO['thr']),(groupchat,)).start()
		DBPATH='dynamic/'+groupchat+'/config.cfg'
		write_file(DBPATH, str(GCHCFGS[groupchat]))
		if passw:
			add_gch(groupchat, DEFAULT_NICK)
			join_groupchat(groupchat, DEFAULT_NICK)
		else:
			add_gch(groupchat, DEFAULT_NICK, passw)
			join_groupchat(groupchat, DEFAULT_NICK, passw)
		MACROS.load(groupchat)
		reply(type, source, u' الان البوت بروم ' + groupchat + ' 8-)')
		if popups_check(groupchat):
			if reason:
				msg(groupchat, u'تم أرسالي عن طريق 8-) '+source[2]+u' reason:\n'+reason)
			else:
				msg(groupchat, u'تم أرسالي عن طريق 8-) '+source[2])
	else:
		reply(type, source, u'حط أسم الروم مع السيرف ياشاطر')

def handler_admin_leave(type, source, parameters):
	args = parameters.split()
	if len(args)>1:
		level=int(user_level(source[1]+'/'+source[2], source[1]))
		if level<40 and args[0]!=source[1]:
			reply(type, source, u'مارحت ع هي الروم :-D ')
			return
		reason = ' '.join(args[1:]).strip()
		if not GROUPCHATS.has_key(args[0]):
			reply(type, source, u'مارحت ع هي الروم :-D ')
			return
		groupchat = args[0]
	elif len(args)==1:
		level=int(user_level(source[1]+'/'+source[2], source[1]))
		if level<40 and args[0]!=source[1]:
			reply(type, source, u'كتير شاطر ها بس معلمي معو أكسز ;-) ')
			return
		if not GROUPCHATS.has_key(args[0]):
			reply(type, source, u'مارحت ع هي الروم :-D')
			return
		reason = ''
		groupchat = args[0]
	else:
		groupchat = source[1]
		reason = ''
	if popups_check(groupchat):
		if reason:
			msg(groupchat, u'بطلب من معلمي أنا خارج الروم  ;-) '+source[2]+u' reason:\n'+reason)
		else:
			msg(groupchat, u'بطلب من معلمي أنا خارج الروم ;-) '+source[2])
	if reason:
		leave_groupchat(groupchat, u'بطلب من معلمي أنا خارج الروم '+source[2]+u' reason:\n'+reason)
	else:
		leave_groupchat(groupchat,u'بطلب من معلمي أنا خارج الروم  '+source[2]+u' اسف ')
	reply(type, source, u'الان انا خارج هذه الروم سلام ' + groupchat + ' 8-)')


def handler_admin_msg(type, source, parameters):
	msg(string.split(parameters)[0], string.join(string.split(parameters)[1:]))
	reply(type, source, u'تم الارسال بنجاح مبروك ')
	
def handler_glob_msg_help(type, source, parameters):
	total = '0'
	totalblock='0'
	if GROUPCHATS:
		gch=GROUPCHATS.keys()
		for x in gch:
			if popups_check(x):
				msg(x, u'رساله من اونر البوت  '+source[2]+u':\n'+parameters+u'\nهذه الرساله من فريق {мαғια•тєaм™ 2ό13-2ό14 ©}')
				totalblock = int(totalblock) + 1
			total = int(total) + 1
		reply(type, source, ' تم ارسال الرساله الى 8-) '+str(totalblock)+' روم (من '+str(total)+')')
		
def handler_glob_msg(type, source, parameters):
	total = '0'
	totalblock='0'
	if parameters:
		if GROUPCHATS:
			gch=GROUPCHATS.keys()
			for x in gch:
				if popups_check(x):
					msg(x, u'رساله من اونر البوت'+source[2]+':\n'+parameters)
					totalblock = int(totalblock) + 1
				total = int(total) + 1
			reply(type, source, 'تم ارسال الرساله الى 8-) '+str(totalblock)+' روم (من '+str(total)+')')
	

def handler_admin_say(type, source, parameters):
	if parameters:
		args=parameters.split()[0]
		msg(source[1], parameters)
	else:
		reply(type, source, u'هل نسيت تكتب الرساله أنتبه ؟')

def handler_admin_restart(type, source, parameters):
	if parameters:
		reason = parameters
	else:
		reason = ''
	if GROUPCHATS:
		gch=GROUPCHATS.keys()
	if reason:
		for x in gch:
			if popups_check(x):
				msg(x, u'انا قيد التشغيل بطلب من معلمي  8-) '+source[2]+u' reason:\n'+reason)
	else:
		for x in gch:
			if popups_check(x):
				msg(x, u' انا قيد التشغيل بطلب من معلمي  8-) '+source[2])
	prs=xmpp.Presence(typ='unavailable')
	if reason:
		prs.setStatus(source[2]+u': اعاد تشغيلى معلمي  ;-) '+reason)
	else:
		prs.setStatus(source[2]+u': اعاد تشغيلى  عن طريق معلمي ;-)')
	JCON.send(prs)
	time.sleep(1)
	JCON.disconnect()

def handler_admin_exit(type, source, parameters):
	if parameters:
		reason = parameters
	else:
		reason = ''
	if GROUPCHATS:
		gch=GROUPCHATS.keys()
	if reason:
		for x in gch:
			if popups_check(x):
				msg(x, u'تم ايقافى عن طريق معلمي  8-) '+source[2]+u' for reason:\n'+reason)
	else:
		for x in gch:
			if popups_check(x):
				msg(x, u'تم ايقافى عن طريق معلمي  '+source[2])
	prs=xmpp.Presence(typ='unavailable')
	if reason:
		prs.setStatus(source[2]+u': اوقفنى عن العمل معلمي  8-) '+reason)
	else:
		prs.setStatus(source[2]+u': اوقفنى عن العمل معلمي  8-)')
	JCON.send(prs)
	time.sleep(2)
	os.abort()
	
def handler_popups_onoff(type, source, parameters):
	if parameters:
		try:
			parameters=int(parameters.strip())
		except:
			reply(type,source,u'تم الغاء الامر بنجاح')
			return		
		DBPATH='dynamic/'+source[1]+'/config.cfg'
		if parameters==1:
			GCHCFGS[source[1]]['popups']=1
			reply(type,source,u'الان تم تشغيل الاخطارات')
		else:
			GCHCFGS[source[1]]['popups']=0
			reply(type,source,u'الان تم الغاء الاخطارات')
		write_file(DBPATH,str(GCHCFGS[source[1]]))
	else:
		ison=GCHCFGS[source[1]]['popups']
		if ison==1:
			reply(type,source,u'الاخطارات هنا مشغله')
		else:
			reply(type,source,u'الاخطارات هنا موقوفه')
			
def handler_botautoaway_onoff(type, source, parameters):
	if parameters:
		try:
			parameters=int(parameters.strip())
		except:
			reply(type,source,u'تم الغاء الامر بنجاح')
			return		
		DBPATH='dynamic/'+source[1]+'/config.cfg'
		if parameters==1:
			GCHCFGS[source[1]]['autoaway']=1
			reply(type,source,u'تم تشغيل الحاله الذاتيه')
		else:
			GCHCFGS[source[1]]['autoaway']=0
			reply(type,source,u'تم تشغيل الحاله الذاتيه')
		get_autoaway_state(source[1])
		write_file(DBPATH,str(GCHCFGS[source[1]]))
	else:
		ison=GCHCFGS[source[1]]['autoaway']
		if ison==1:
			reply(type,source,u'هنا يتضمن')
		else:
			reply(type,source,u'هنا الاوتوبسنس مفصوله عن التشغيل')	
	
def handler_changebotstatus(type, source, parameters):
	if parameters:
		args,show,status=parameters.split(' ',1),'',''
		if args[0] in ['away','xa','dnd','chat']:
			show=args[0]
		else:
			show=None
			status=parameters
		if not status:
			try:
				status=args[1]
			except:
				status=None
		change_bot_status(source[1],status,show,0)
		GCHCFGS[gch]['status']={'status': status, 'show': show}
	else:
		stmsg=GROUPCHATS[source[1]][get_bot_nick(source[1])]['stmsg']
		status=GROUPCHATS[source[1]][get_bot_nick(source[1])]['status']
		if stmsg:
			reply(type,source, u'الان لدى حاله جديده شوفني  : '+status+u' ('+stmsg+u')')
		else:
			reply(type,source, u'الان لدى حاله جديده شوفني  '+status)
			
def get_autoaway_state(gch):
	if not 'autoaway' in GCHCFGS[gch]:
		GCHCFGS[gch]['autoaway']=1
	if GCHCFGS[gch]['autoaway']:
		LAST['gch'][gch]['autoaway']=0
		LAST['gch'][gch]['thr']=None
		
def set_default_gch_status(gch):
	if isinstance(GCHCFGS[gch].get('status'), str): #temp workaround
		GCHCFGS[gch]['status']={'status': u'STORM BOT BY ALI', 'show': u''}
	elif not isinstance(GCHCFGS[gch].get('status'), dict):
		GCHCFGS[gch]['status']={'status': u'STORM BOT BY ALI', 'show': u''}


register_command_handler(handler_admin_join, 'اذهب', ['superadmin','muc','all'], 100, 'Join conf. If there is a password write that password right after the name of conference.', 'join <conf> [pass=1111] [reason]', ['join stream@conference.jabbus.org', 'join stream@conference.jabbus.org *VICTORY*', 'join stream@conference.jabbus.org pass=1111 *VICTORY*'])
register_command_handler(handler_admin_leave, 'غادر', ['admin','muc','all'], 100, 'Forces to leave from current or certain conference.', 'leave <conference> [reason]', ['leave joe@conference.jabber.aq hate you', 'leave sleep','свал'])
register_command_handler(handler_admin_msg, 'رساله', ['admin','muc','all'], 40, 'Sends message on behalf of bot certain JID.', 'message <jid> <message>', ['message guy@jabbus.org *HI* Chuvak!'])
register_command_handler(handler_admin_say, 'قول', ['admin','muc','all'], 20, 'say <message>', ['say *HI* peoples'])
register_command_handler(handler_admin_restart, 'اعاده-تشغيل', ['superadmin','all'], 200, 'Restart bot.', 'restart [reason]', ['restart','restart *FIGA*'])
register_command_handler(handler_admin_exit, 'ايقاف-تشغيل', ['superadmin','all'], 200, 'Complete out.', 'exit [reason]', ['exit','say <message>'])
register_command_handler(handler_glob_msg, 'رساله-رومات', ['superadmin','muc','all'], 200, 'Send message to all conf, which a bot is in.', 'globmsg [message]', ['globmsg all *HI*'])
register_command_handler(handler_glob_msg_help, 'رساله-كليه', ['superadmin','muc','all'], 100, 'Send message to all conf, which a bot is in.', 'globmsg [message]', ['globmsg all *HI*'])
register_command_handler(handler_popups_onoff, 'بوبس', ['admin','muc','all'], 30, 'Off (0) On (1) message about join/leaves, restarts/off, and also global news for certain conf. Without a parameters will rotin current status.', 'popups [conf] [1|0]', ['popups stream@conference.jabbus.org 1','popups stream@conference.jabbus.org 0','popups'])
register_command_handler(handler_botautoaway_onoff, 'حاله-ذاتيه', ['admin','muc','all'], 30, 'Disconnects (0) Or includes (1) Autochange of the status of the bot to away  absence of commands of 10 minutes. Without parameter will show a current condition.', 'autoaway [1|0]', ['autoaway 1','autoaway'])
register_command_handler(handler_changebotstatus, 'حاله-البوت', ['admin','muc','all'], 200, 'changes the status of the bot in conference list:\naway - no,\nxa - For a long time I am absent,\ndnd - do not disturb,\nchat - want to chat,\nа Also the status message (If it is given).', 'setstatus [status] [message]', ['setstatus away','setstatus away i am busy'])

register_stage1_init(get_autoaway_state)
register_stage1_init(set_default_gch_status)
