#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  commoff_plugin.py

#  STORM BOT BY ALI

def handler_commoff(type,source,parameters):
	na=[u'access',u'eval',u'login',u'logout',u'!stanza',u'unglobacc',u'leave',u'restart',u'globacc',u'commands',u'sh',u'exec',u'commoff',u'common']
	valcomm,notvalcomm,alrcomm,npcomm,vcnt,ncnt,acnt,nocnt,rep,commoff=u'',u'',u'',u'',0,0,0,0,u'',[]
	if not source[1] in COMMOFF:
		get_commoff(source[1])
	commoff=COMMOFF[source[1]]
	DBPATH='dynamic/'+source[1]+'/config.cfg'
	if parameters:
		param=string.split(parameters, ' ')
		for y in param:
			if COMMANDS.has_key(y) or y in MACROS.macrolist[source[1]] or y in MACROS.gmacrolist:
				if not y in na:
					if not y in commoff:
						commoff.append(y)
						vcnt+=1
						valcomm+=str(vcnt)+u') '+y+u'\n'
					else:
						acnt+=1
						alrcomm+=str(acnt)+u') '+y+u'\n'						
				else:
					ncnt+=1
					npcomm+=str(ncnt)+u') '+y+u'\n'
			else:
				nocnt+=1
				notvalcomm+=str(nocnt)+u') '+y+u'\n'
		if valcomm:
			rep+=u'تم الغاء هذه الاوامر بنجاح :THUMBS UP::\n'+valcomm
		if alrcomm:
			rep+=u'\هذه الاوامر ملغيه من قبل :-|:\n'+alrcomm
		if notvalcomm:
			rep+=u'\nهذه الاوامر ليست العامه ;-) :\n'+notvalcomm
		if npcomm:
			rep+=u'\nمستحيل فصل هذه الاوامر من العامه ;-):\n'+npcomm
		if not GCHCFGS[source[1]].has_key('commoff'):
			GCHCFGS[source[1]]['commoff']='commoff'
			GCHCFGS[source[1]]['commoff']=[]
		GCHCFGS[source[1]]['commoff']=commoff
		write_file(DBPATH, str(GCHCFGS[source[1]]))
		get_commoff(source[1])
	else:
		for x in commoff:
			vcnt+=1
			valcomm+=str(vcnt)+u') '+x+u'\n'
		if valcomm:
			rep=u'تم الغاء هذه الاوامر بنجاح :THUMBS UP::\n'+valcomm
		else:
			rep=u'كل االاوامر تتضمن هذه الروم ;-)'
			
		
	reply(type,source,rep.strip())
		
def handler_common(type,source,parameters):
	na=[u'access',u'eval',u'login',u'logout',u'!stanza',u'unglobacc',u'leave',u'restart',u'globacc',u'?commands all',u'sh',u'exec',u'commoff',u'common']
	valcomm,notvalcomm,alrcomm,npcomm,vcnt,ncnt,acnt,nocnt,rep,commoff=u'',u'',u'',u'',0,0,0,0,u'',[]
	if not source[1] in COMMOFF:
		get_commoff(source[1])
	commoff=COMMOFF[source[1]]
	DBPATH='dynamic/'+source[1]+'/config.cfg'
	if parameters:
		param=string.split(parameters, ' ')
		for y in param:
			if COMMANDS.has_key(y) or y in MACROS.macrolist[source[1]] or y in MACROS.gmacrolist:
				if not y in na:
					if y in commoff:
						commoff.remove(y)
						vcnt+=1
						valcomm+=str(vcnt)+u') '+y+u'\n'
					else:
						acnt+=1
						alrcomm+=str(acnt)+u') '+y+u'\n'						
				else:
					ncnt+=1
					npcomm+=str(ncnt)+u') '+y+u'\n'
			else:
				nocnt+=1
				notvalcomm+=str(nocnt)+u') '+y+u'\n'
		if valcomm:
			rep+=u'تم تفعيل هذه الااوامر بنجاح :THUMBS UP::\n'+valcomm
		if alrcomm:
			rep+=u'\nهذه الاوامر مغلقه من قبل :-|:\n'+alrcomm
		if notvalcomm:
			rep+=u'\nالاوامر اللتى بالاسفل ليست من العامه ;-) :\n'+notvalcomm
		if npcomm:
			rep+=u'\nالاوامر الاتيه ليست بالعامه ;-)::\n'+npcomm
		if not GCHCFGS[source[1]].has_key('commoff'):
			GCHCFGS[source[1]]['commoff']='commoff'
			GCHCFGS[source[1]]['commoff']=[]
		GCHCFGS[source[1]]['commoff']=commoff
		write_file(DBPATH, str(GCHCFGS[source[1]]))
		get_commoff(source[1])
	else:
		rep=u'and?'
		
	reply(type,source,rep.strip())
	
def get_commoff(gch):
	try:
		if GCHCFGS[gch].has_key('commoff'):
			commoff=GCHCFGS[gch]['commoff']
			COMMOFF[gch]=commoff
		else:
			COMMOFF[gch]=gch
			COMMOFF[gch]=[]
	except:
		pass
	
	
register_command_handler(handler_commoff, 'عدم-تفعيل-امر', ['admin','muc','all'], 20, 'Disconnects certain commands for current conf, without parameters shows the list of already power-off commands.', 'commoff [commands]', ['commoff','commoff poked disko version ping'])
register_command_handler(handler_common, 'تفعيل-امر', ['admin','muc','all'], 20, 'Includes certain commands for current conf.', 'common [commadns]', ['common poked disko version ping'])

register_stage1_init(get_commoff)
