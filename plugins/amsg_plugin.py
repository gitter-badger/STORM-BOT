#===istalismanplugin===
# -*- coding: utf-8 -*-

#  STORM BOT BY ALI

AMSGCONF = {}

def handler_amsg(type, source, parameters):
      ADMINFILE = 'static/amsg.txt'
      fp = open(ADMINFILE, 'r')
      txt = eval(fp.read())
      if checkbl(get_true_jid(source[1]+'/'+source[2]).lower()):
            reply(type, source, u'يتم حظر لك لأن: '+checkbl(get_true_jid(source[1]+'/'+source[2]).lower()) )
            return
      if len(txt)>=1:
        if parameters:
          if len(parameters)>150:
            reply(type, source, u'لقد كتبت الكلمه مرات متعدده!!!')
            return
      
          if not AMSGCONF.has_key(get_true_jid(source[1]+'/'+source[2])):
                AMSGCONF[get_true_jid(source[1]+'/'+source[2])] = {'timesend':time.time(), 'count':1}
          else:
                if time.time() - AMSGCONF[get_true_jid(source[1]+'/'+source[2])]['timesend'] <= 300:
                      reply(type, source, u'يتم ارسال الرساله الى المديرين من فضلك انتظر')
                      return
                else:
                      AMSGCONF[get_true_jid(source[1]+'/'+source[2])]['timesend'] = time.time()
                      AMSGCONF[get_true_jid(source[1]+'/'+source[2])]['count'] += 1

          for x in txt:
            msg(x, u'Note for subscribers from '+source[1]+'/'+source[2]+u' (jid: '+get_true_jid(source[1]+'/'+source[2])+u')\nText message: '+parameters)
          reply(type, source, u'تم ارسال الرساله بنجاح')
        else:
          reply(type, source, u'لقد نسيت ان تكتب الرساله!!!')
      else:
        if not AMSGCONF.has_key(get_true_jid(source[1]+'/'+source[2])):
            AMSGCONF[get_true_jid(source[1]+'/'+source[2])] = {'timesend':time.time(), 'count':1}
        else:
            if time.time() - AMSGCONF[get_true_jid(source[1]+'/'+source[2])]['timesend'] <= 300:
                  reply(type, source, u'يتم ارسال الرساله الى المديرين من فضلك انتظر')
                  return
            else:
                  AMSGCONF[get_true_jid(source[1]+'/'+source[2])]['timesend'] = time.time()
                  AMSGCONF[get_true_jid(source[1]+'/'+source[2])]['count'] += 1

        if parameters:
          if len(parameters)>150:
            reply(type, source, u'لقد كتبت الكلمه مرات متعدده!!!')
            return

          for z in ADMINS:
            msg(z, u'رساله الى مديرين البوت من '+source[1]+'/'+source[2]+u' (jid: '+get_true_jid(source[1]+'/'+source[2])+u')\nText message: '+parameters)
          reply(type, source, u'تم ارسال الرساله بنجاح')
        else:
          reply(type, source, u'لقد نسيت ان تكتب الرسالهe!!!')
      
  
        

def amsg_subscribe(type, source, parameters):
    ADMINFILE = 'static/amsg.txt'
    fp = open(ADMINFILE, 'r')
    txt = eval(fp.read())
    if parameters:
      if parameters in txt:
        reply(type, source, u'هذا الايميل موجود حاليه بالمعلومات')
        return
      else:
        txt.append(parameters)
        write_file(ADMINFILE,str(txt))
        fp.close()
        reply(type, source, u'JID '+parameters+u' اكتتبت في الإعلام')
    else:
      parameters = get_true_jid(source[1]+'/'+source[2])
      fp = open(ADMINFILE, 'r')
      txt = eval(fp.read())
      fp.close()
      if parameters in txt:
        reply(type, source, u'انت حاليا فى المعلومات')
        return
      else:
        txt.append(get_true_jid(source[1]+'/'+source[2]))
        write_file(ADMINFILE,str(txt))
        
        reply(type, source, u'انت حاليا من الاعضاء')
      
def amsg_unsubscribe(type, source, parameters):
      ADMINFILE = 'static/amsg.txt'
      if parameters:
            fp = open(ADMINFILE, 'r')
            txt = eval(fp.read())
            fp.close()
            if parameters in txt:
                  txt.remove(parameters)
            else:
                  reply(type, source, u'هل ترى هذا الايميل فى القائمه؟ انا لا ارى')
                  return
            write_file(ADMINFILE,str(txt))

            reply(type, source, u'JID '+parameters+u' unsubscribed from the notification')
      else:
            parameters = get_true_jid(source[1]+'/'+source[2])
            fp = open(ADMINFILE, 'r')
            txt = eval(fp.read())
            fp.close()
            if parameters in txt:
                  txt.remove(get_true_jid(source[1]+'/'+source[2]))
            else:
                  reply(type, source, u'هل ترى هذا الايميل فى القائمه؟ انا لا ارى')
                  return
            write_file(ADMINFILE,str(txt))
            reply(type, source, u'تم المسح من القائمه')
      
def amsg_show(type, source, parameters):
    ADMINFILE = 'static/amsg.txt'
    fp = open(ADMINFILE, 'r')
    txt = eval(fp.read())
    fp.close()
    if len(txt) == 0:
      reply(type, source, u'قاءمه الاعضاء خاليه!')
      return
    p =1
    spisok = ''
    for usr in txt:
          spisok += str(p)+'. '+usr+'\n'
          p +=1
    reply(type, source, u'الأعضاء إخطارات (مجموع '+str(len(txt))+u'):\n'+spisok)
          
def amsg_clear(type, source, parameters):
    ADMINFILE = 'static/amsg.txt'
    write_file(ADMINFILE,str('[]'))
    reply(type, source, u'تم تنظيف قائمه الاعضاء')

def amsg_blacklist(type, source, parameters):
      ADMINFILE = 'static/blacklist.txt'
      if not parameters:
            reply(type, source, u'اسف!امر خاطئ يرجى قراءه الاوامر')
            return
      params = parameters.split(' ', 1)
      if len(params) == 2:

            if params[0] == 'add':
                  fp = open(ADMINFILE, 'r')
                  txt = eval(fp.read())
                  fp.close()
                  a = params[1].split('|', 1)
                  if txt.has_key(a[0].lower()):
                        reply(type, source, u'هذا الايميل حاليا فى القائمه السوداء')
                        return
                  else:
                        if len(a) == 1:
                              txt[a[0].lower()] = u'Locked'
                        elif len(a) == 2:
                              txt[a[0].lower()] = a[1]
                              
                        write_file(ADMINFILE, str(txt))
                        reply(type, source, u'تم اضافه الايميل فى القائمه السوداء')

            elif params[0] == 'del':
                  fp = open(ADMINFILE, 'r')
                  txt = eval(fp.read())
                  fp.close()
                  if txt.has_key(params[1].lower() ):
                        del txt[params[1].lower()]
                        write_file(ADMINFILE, str(txt))
                        reply(type, source, u'تم مسح الايميل من القائمه السوداء')
                  else:
                        reply(type, source, u'هذا الايميل غائب عن القائمه السوداء')
            else:
                  reply(type, source, u'امر غير معروف')
                  return
      elif len(params) == 1:
            if params[0] == 'show':
                  fp = open(ADMINFILE, 'r')
                  txt = eval(fp.read())
                  fp.close()
                  p = 1
                  spisok = ''
                  if len(txt.keys()) == 0:
                        reply(type, source, u'القائمه السوداء خاليه')
                        return
                  for usr in txt.keys():
                        spisok += str(p)+'. '+usr+' ('+txt[usr]+')\n'
                        p +=1
                  reply(type, source, u'القائمة السوداء (مجموع '+str(len(txt.keys()))+u'):\n'+spisok)
      else:
            reply(type, source, u'امر غير معروف')
            return

def checkbl(jid):
      jid = jid.lower()
      ADMINFILE = 'static/blacklist.txt'
      fp = open(ADMINFILE, 'r')
      txt = eval(fp.read())
      fp.close()

      if txt.has_key(jid):
            return txt[jid]
      else:
            return 0
      

register_command_handler(handler_amsg, 'رساله', ['all','amsg'], 0,'Sends a message to all administrators on the bot jid, specify from whom the message - do not, the bot itself shows the conference and the nickname of the sender.','amsg', ['amsg Hello, there are some problems, please come to me'])
#register_command_handler(handler_amsg, '.blade', ['all','amsg'], 0,'Sends a message to all administrators on the bot jid, specify from whom the message - do not, the bot itself shows the conference and the nickname of the sender.','amsg', ['.oxygen Hello, there are some problems, please come to me'])
register_command_handler(handler_amsg, 'رساله-مديرين', ['all','amsg'], 0,'Sends a message to all administrators on the bot jid, specify from whom the message - do not, the bot itself shows the conference and the nickname of the sender.','message_admin', ['message_admin Hello, there are some problems, please come to me'])
register_command_handler(amsg_subscribe, 'رساله-اشتراك', ['all','amsg','superadmin'], 100, 'Subscription notification plugin amsg. List of jid`s which will be sent the message. Without the option its mean adds your jid', 'amsg_subscribe <jid>', ['amsg_subscribe user@server.tld'])
register_command_handler(amsg_unsubscribe, 'رساله-عدم-اشتراك', ['all','amsg','superadmin'], 100, 'Unsubscription notifications plug amsg. Without the option means removes your jid', 'amsg_unsubscribe <jid>', ['amsg_unsubscribe user@server.tld'])
register_command_handler(amsg_show, 'اظهار-الرساله', ['all','amsg','superadmin'], 100, 'Viewing subscribers.', 'amsg_show', ['amsg_show'])
register_command_handler(amsg_clear, 'تنظيف-الرساله', ['all','amsg','superadmin'], 100, 'Purification of the list of subscribers', 'amsg_clear', ['amsg_clear'])
register_command_handler(amsg_blacklist, 'رساله-القائمه-السوداء', ['all','amsg','superadmin'], 100, 'Block users (the command amsg will be unavailable)', 'amsg_blacklist <add|del|show>', ['amsg_blacklist add user@server.tld','amsg_blacklist add user@server.tld|reason','amsg_blacklist del user@server.tld','amsg_blacklist show'])
