#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  access_plugin.py

#  STORM BOT BY ALI



def handler_access_view_access(type, source, parameters):
	accdesc={'-200':u'(متجاهل تماما)','-1':u'(محجوز)','0':u'(زائـر)','1':u'(عضو ضعيف :D )','10':u'(مستخدم)','11':u'(عـضـو)','15':u'(مدير)','16':u'(مدير)','30':u'(ادمن)','60':u'(اونر)','40':u'(pionir)','200':u'(مـالـك الـبـوت :-))'}
	if not parameters:
		level=str(user_level(source[1]+'/'+source[2], source[1]))
		if level in accdesc.keys():
			levdesc=accdesc[level]
		else:
			levdesc=''		
		reply(type, source, level+u' '+levdesc)
	else:
		if not source[1] in GROUPCHATS:
			reply(type, source, u'اسف!هذا الامر فقط فى الروم')
			return
		nicks = GROUPCHATS[source[1]].keys()
		if parameters.strip() in nicks:
			level=str(user_level(source[1]+'/'+parameters.strip(),source[1]))
			if level in accdesc.keys():
				levdesc=accdesc[level]
			else:
				levdesc=''
			reply(type, source, level+' '+levdesc)
		else:
			reply(type, source, u'اين هو؟')

def handler_access_set_access(type, source, parameters):
	if not source[1] in GROUPCHATS:
		reply(type, source, u'اسف!هذا الامر فقط فى الروم')
		return
	splitdata = string.split(parameters)
	if len(splitdata) > 1:
		try:
			int(splitdata[1].strip())
		except:
			reply(type, source, u'امر خاطئ!اقرا الاوامر ')
			return				
		if int(splitdata[1].strip())>200 or int(splitdata[1].strip())<-200:
			reply(type, source, u'امر خاطئ!اقرا الاوامر ')
			return		
	nicks=GROUPCHATS[source[1]]
	if not splitdata[0].strip() in nicks and GROUPCHATS[source[1]][splitdata[0].strip()]['ishere']==0:
		reply(type, source, u'اين هو؟')
		return
	tjidto=get_true_jid(source[1]+'/'+splitdata[0].strip())
	tjidsource=get_true_jid(source)
	groupchat=source[1]
	jidacc=user_level(source, groupchat)
	toacc=user_level(tjidto, groupchat)

	if len(splitdata) > 1:
		if tjidsource in ADMINS:
			pass
		else:
			if tjidto==tjidsource:
				if int(splitdata[1]) > int(jidacc):
					reply(type, source, u':-P')
					return
			elif int(toacc) > int(jidacc):
				reply(type, source, u':-P')
				return		
			elif int(splitdata[1]) >= int(jidacc):
				reply(type, source, u':-P')
				return	
	else:
		if tjidsource in ADMINS:
			pass
		else:
			if tjidto==tjidsource:
				pass
			elif int(toacc) > int(jidacc):
				reply(type, source, u':-P')
				return

	if len(splitdata) == 1:		
		change_access_perm(source[1], tjidto)
		if splitdata[0].strip()==source[2]:
			reply(type, source, u'الاكسز المحلى تم سحبه')
		else:
			reply(type, source, u'الاكسز المحلى تم سحبه' % splitdata[0].strip())
	elif len(splitdata) == 2:
		change_access_temp(source[1], tjidto, splitdata[1].strip())
		reply(type, source, u'تم اعطاء الاكسز بنجاح')
	elif len(splitdata) == 3:
		change_access_perm(source[1], tjidto, splitdata[1].strip())
		reply(type, source, u'تم اعطاء الاكسز بنجاح')		
		
def handler_access_set_access_glob(type, source, parameters):
	if not source[1] in GROUPCHATS:
		reply(type, source, u'اسف!هذا الامر فقط فى الروم')
		return
	if parameters:
		splitdata = parameters.strip().split()
		if len(splitdata)<1 or len(splitdata)>2:
			reply(type, source, u'????')
			return
		nicks=GROUPCHATS[source[1]].keys()
		if not splitdata[0].strip() in nicks and GROUPCHATS[source[1]][splitdata[0].strip()]['ishere']==0:
			reply(type, source, u'اين هو؟')
			return
		tjidto=get_true_jid(source[1]+'/'+splitdata[0])
		if len(splitdata)==2:
			change_access_perm_glob(tjidto, int(splitdata[1]))
			reply(type, source, u'تم اعطاء الاكسز بنجاح')
		else:
			change_access_perm_glob(tjidto)
			reply(type, source, u'تم سحب الاكسز الكلى')
			
def get_access_levels():
	global GLOBACCESS
	global ACCBYCONFFILE
	GLOBACCESS = eval(read_file(GLOBACCESS_FILE))
	for jid in ADMINS:
		GLOBACCESS[jid] = 200
		write_file(GLOBACCESS_FILE, str(GLOBACCESS))
	ACCBYCONFFILE = eval(read_file(ACCBYCONF_FILE))

register_command_handler(handler_access_view_access, 'اكسز', ['access','admin','all'], 0, 'Show access level of a user.\n-100 - omitted, all messages from users with this access will be ignored at the kernel level\n-1 - ignored\n0 - commands and macros are very limited, automatic known as visitor\n10 - standard commands and macro, automatically known as participant\n11 - extended commands and macro (access too ;-) !!!), automatically known as member\n15 (16) - commands and macro for moderator, automatically known as moderator\n20 - commands and macro for admin, automatically known as admin\n30 - commands and macro for owner owner\n40 - not all commands implemented, can join and leave bot\n100 - Bot Admin, obey all commands', 'access [nick]', ['access', 'access guy'])
register_command_handler(handler_access_set_access, 'اعطاء-اكسز', ['access','admin','all'], 15, 'Grant or withdrawn local access of a user.\nWrite without level after nickname to delete the access, bot need to rejoin conference. if the third parameter "permanent" mentioned, the access grant permanently, if not the access deleted soon when bot bila tidak akses akan hilang saat bot rejoin conference.\n-100 - omitted, all messages from users with this access will be ignored at the kernel level\n-1 - ignored\n0 - commands and macros are very limited, automatic known as visitor\n10 - standard commands and macro, automatically known as participant\n11 - extended commands and macro (access too ;-) !!!), automatically known as member\n15 (16) - commands and macro for moderator, automatically known as moderator\n20 - commands and macro for admin, automatically known as admin\n30 - commands and macro for owner owner\n40 - not all commands implemented, can join and leave bot\n100 - Bot Admin, obey all commands', 'set_access <nick> <level> [permanent]', ['set_access guy 20', 'set_access guy 30 permanent'])
register_command_handler(handler_access_set_access_glob, 'منح-اكسز', ['access','superadmin','all'], 200, 'Grant or withdrawn global access of a user.\nWrite without level after nickname to delete the access.', 'globacc <nick> <level>', ['globacc guy 100','globacc guy'])

register_stage0_init(get_access_levels)
