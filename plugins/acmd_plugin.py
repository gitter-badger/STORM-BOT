#===istalismanplugin===
# -*- coding: utf-8 -*-

#  STORM BOT BY ALI

def handler_query_set43(type, source, parameters):
 if not parameters:
  reply(type, source, u'hmmm?')
  return
 groupchat=source[1]
 DBPATH='dynamic/'+groupchat+'/acmd.txt'
 if check_file(groupchat,'acmd.txt'):
  try:
   localdb = eval(read_file(DBPATH))
   keyval = string.split(parameters, '=', 1)
#  print parameters
   comma=parameters.split('=')
   commaa=comma[1].split(' ')
#  print commaa[0].lower()
   try:
    real_access = MACROS.get_access(parameters, source[1])
    if real_access < 0:
  	real_access = COMMANDS[commaa[0].lower()]['access']
    if real_access > 30:
    	reply(type, source,  u'Netushki. neprokatit ;)')	
    	return
    if not len(keyval)<2:
     key = string.lower(keyval[0]).strip()
     value = keyval[1].strip()
     localdb[key] = keyval[1].strip()
     write_file(DBPATH, str(localdb))
     reply(type, source, u'تم الاضافة')
    else:
                        reply(type, source, u'لم يتم إنشاء ملف acmd. اتصل بوت المشرف.')
   except:
    reply(type, source,  u'سوء القيادة داخل ؛) الاسم المستعار')
  except:
   reply(type, source,  u'هل تعرف حتى نفسك ما تريد مني؟ ؛)')
 else:
  reply(type,source,u'خطأ في إنشاء هذا database.tell إلى مشرف من ')
						
def handler_query_all43(type, source, parameters):
 groupchat=source[1]
 DBPATH='dynamic/'+groupchat+'/acmd.txt'
 if check_file(groupchat,'acmd.txt'):
  localdb = eval(read_file(DBPATH))
  num=len(localdb.keys())
  if num == 0:
   reply(type, source, 'empty!')
   return
  reply(type, source, u'alias list: \n'+', '.join(localdb.keys()) +'.')
 else:
  reply(type,source,u'Error creating database.tell this to admin of bot')
  return
  
def handler_query_del43(type, source, parameters):
 if not parameters:
  reply(type, source, u'hmmmm?')
  return
 groupchat=source[1]
 DBPATH='dynamic/'+groupchat+'/acmd.txt'
 if check_file(groupchat,'acmd.txt'):
  localdb = eval(read_file(DBPATH))
  if localdb.has_key(parameters.strip()):
                        del localdb[parameters.strip()]
                        write_file(DBPATH, str(localdb))
                        reply(type, source, u'removed')
  else:
                        reply(type, source,  u'انظر القائمة الأمر الأول')
 else:
  reply(type,source,u'خطأ في إنشاء هذا database.tell إلى مشرف من بوت')
  
def handler_test2(type, source, parameters):
 if parameters.count(u'alias_add') or parameters.count(u'alias_add'):
  return
 DBqPATH='dynamic/'+source[1]+'/acmd.txt'
 if check_file(source[1],'acmd.txt'):
  localdb = eval(read_file(DBqPATH))
  for grc in localdb:
                        if parameters.lower().count(grc):
                                cbody = localdb[grc]
                                comma=cbody.split()[0].lower()
                                params = cbody[(cbody.find(' ') + 1):].strip()
                                if params == comma:
									params = ''
#                                command=cbody.split()[0].lower()
#                                print str(source[2])
                                if params.count('%NICK%'):
                                    params=strip_tags.sub('', params.replace('%NICK%',str(source[2])))#.replace('11','22'))
#                                print params
                                real_access = MACROS.get_access(cbody, source[1])
                                if real_access < 0:
								    real_access = COMMANDS[comma]['access']
                                if real_access > 30:
								    reply(type, source,  u'figure!')	
								    return
                                with smph:
								    INFO['thr'] += 1
								    threading.Thread(None,COMMAND_HANDLERS[comma],'command'+str(INFO['thr']),(type, source, params,)).start()
 else:
  write_file(DBqPATH, u'{}') 
#                                call_command_handlers(comma, type, source, params, cbody) 


def handler_acmd_call(type, source, parameters):
	if parameters:
		DBPATH='dynamic/'+source[1]+'/acmd.txt'
		if not check_file(source[1],'acmd.txt'):
			write_file(DBPATH, u'{}')
		localdb = eval(read_file(DBPATH))
		actype=parameters.split()[0].lower()
		if actype == 'add' or actype == u'add':
			acparams = parameters[(parameters.find(' ') + 1):].strip()
			handler_query_set43(type, source, acparams)
			return
		if actype == 'del' or actype == u'del':
			acparams = parameters[(parameters.find(' ') + 1):].strip()
			handler_query_del43(type, source, acparams)
			return
		if actype == 'list' or actype == u'list':
			acparams = parameters[(parameters.find(' ') + 1):].strip()
			handler_query_all43(type, source, acparams)
			return
		if actype == 'show' or actype == u'show':
			acparams = parameters[(parameters.find(' ') + 1):].strip()
			handler_query_all43(type, source, acparams)
			return
		if actype == 'help' or actype == u'help':
			reply(type, source, u'أدلى akomandy مع كونه! acmd MUC 1 Gluxi بوت. \ NExamples: \ ن akmd إخفاء إضافة إلى القول = / لي اختبأ \ ن akmd الوظيفة visyu بينغ = \ ن (في هذه الحالة، يتم تنفيذ الأمر نيابة عن وقال "بينغ") \ ن akmd القائمة \ n akmd الشؤون إخفاء \ ن \ n بعد القيام علامة = هي تعويذة الفريق المعتادة. \٪ المعلمة NDotstupen NICK٪')
		else:
			reply(type, source, u'وماذا أفعل بها؟')
	else:
		reply(type, source, u'hmmmm?')
		return
		

register_command_handler(handler_acmd_call, 'مساعده-الاسم', ['muc','all'], 20, 'help on adding a command. options:\n help, add, cases, sheets. \nFrom Mr.King', 'setting alias_add <word>=<command>', ['alias_help assistance','alias_help add word=command /me smacs %NICK% haaaa!'])
						
register_message_handler(handler_test2)

register_command_handler(handler_query_set43, 'أضافة-اسم', ['muc','all'], 20, 'to add an alias to the database! \nFrom Mr.King', 'alias_add <word>=<value>', ['alias_add hi=say hello!'])
register_command_handler(handler_query_all43, 'أظهار-اسم', ['muc','all'], 10, 'shows saved aliases!\nFrom Mr.King', 'alias_show', ['alias_show'])
register_command_handler(handler_query_del43, 'حذف-اسم', ['muc','all'], 20, 'to delete an alias from the database\nFrom Mr.King', 'alias_del <word>', ['alias_del hi'])


