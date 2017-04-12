#===istalismanplugin===
# -*- coding: utf-8 -*-
#  STORM BOT BY ALI


def roster_sub(type,source,parameters):
        if parameters:
                if not parameters.count('@') or not parameters.count('.'):
                        reply(type,source,u'قراءة الأمر مساعدة!')
                        return
                ROSTER = JCON.getRoster()
                ROSTER.Subscribe(parameters)
                reply(type,source,u'تم ارسال الاضافه:-[')

def roster_unsub(type,source,parameters):
        if parameters:
                if  not parameters.count('@') or not parameters.count('.'):
                        reply(type,source,u'قراءة الأمر مساعدة!')
                        return
                ROSTER = JCON.getRoster()
                ROSTER.Unsubscribe(parameters)
                ROSTER.delItem(parameters)
                reply(type,source,u'تم حذف الاضافه')

def roster_show(type,source,parameters):
        ROSTER = JCON.getRoster()
        list, col = '', 0
        rep = ROSTER.getItems()
        for jid in rep:
                if not jid.count('@conf'):
                    col = col + 1
                    list += '\n'+str(col)+'. '+jid
        if col != 0:
                reply(type, source, (u'\nمجموع: %s الأسماء في قائمتي:' % str(col))+list)
        else:
                reply(type, source, u' قائمتي فارغ ...')
		
register_command_handler(roster_show, 'اظهار-قائمه', ['اونر','الكل'], 90, 'وتظهر الأسماء على قائمة البوت.', 'قائمه-الكل', ['اظهار-قائمه'])		
register_command_handler(roster_sub, 'اضافه-قائمه', ['اونر','الكل'], 90, 'إضافة جهة اتصال في قائمة البوت.', 'اضافه-قائمه <jid>', ['اضافه-قائمه guy@server.tld'])
register_command_handler(roster_unsub, 'مسح-قائمه', ['اونر','الكل'], 90, 'حذف جهة اتصال في قائمة البوت.', 'مسح-قائمه <jid>', ['مسح-قائمه guy@server.tld'])
