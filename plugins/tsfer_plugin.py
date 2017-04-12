#===istalismanplugin===
# -*- coding: utf-8 -*-
#  STORM BOT BY ALI

def handler_killrooms(type, source, parameters):
   reply(type,source,u'انتظر قليلا....ريثما يتم سحبي من جميع الرومات8-) ')
   if check_file(file='chatrooms.list'):
     killrooms = eval(read_file(GROUPCHAT_CACHE_FILE))
     for groupchat in killrooms:
       leave_groupchat(groupchat, u'تم التصفير بنجاح 8-) ')
   else:
     print 'Error: unable to create chatrooms list file!'
register_command_handler(handler_killrooms, 'تصفير', ['الكل'], 100, 'تصفير البوت', '', [''])
