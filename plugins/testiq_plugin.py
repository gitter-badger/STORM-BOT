#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  testiq_plugin.py

#  STORM BOT BY ALI

TESTIQP = {}

ORDERMODE = {}

TESTIQBDTEXT = {}
TESTIQBDTEXTWELCOME = {}
TESTIQBDTEXTNOT = {}
TESTIQBDTEXTNOTRESON = {}
TESTIQBD = {}
TESTIQTRIALS = {}
TESTIQONOFFDEF = 0

TESTIQCONF = {}
                        



def testiq_visitor(groupchat, nick):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	visitor=query.addChild('item', {'nick':nick, 'role':'visitor'})
	iq.addChild(node=query)
	JCON.send(iq)

def testiq_participant(groupchat, nick):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	visitor=query.addChild('item', {'nick':nick, 'role':'participant'})
	iq.addChild(node=query)
	JCON.send(iq)

def testiq_kick(groupchat, nick, reason):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	kick=query.addChild('item', {'nick':nick, 'role':'none'})
	kick.setTagData('reason', reason)
	iq.addChild(node=query)
	JCON.send(iq)




def testiq_join(groupchat, nick, aff, role):
        global ORDERMODE
        if aff == 'none':
                DBPATH='dynamic/'+groupchat+'/testiq.txt'
                try:
                        db = eval(read_file(DBPATH))
                        
                        if not TESTIQCONF.has_key(groupchat):
                                TESTIQCONF[groupchat] = {}
                        TESTIQCONF[groupchat] = db

                except:
                        if not TESTIQCONF.has_key(groupchat):
                                TESTIQCONF[groupchat] = {}
                        TESTIQCONF[groupchat] = {'TESTIQBDTEXT': u'_للحصول على حق التحدث فى الروم_',
                                                 'TESTIQBDTEXTWELCOME': u'الأن يمكنك التحدث فى الروم',
                                                 'TESTIQBDTEXTNOT': u'اجابه خاطئه :-( , محاوله: %s',
                                                 'TESTIQBDTEXTNOTRESON': u'اسف, اجابه خاطئه !',
                                                 'TESTIQBD': {u'أكــتب كلمة |سوريا|':'سوريا'},
                                                 'TESTIQONOFF': TESTIQONOFFDEF,
                                                 'TESTIQTRIALS': 3}
                        write_file(DBPATH, str(TESTIQCONF[groupchat]))


                if not ORDERMODE.has_key(groupchat):
                        ORDERMODE[groupchat] = {}
                if not ORDERMODE[groupchat].has_key(nick):
                        ORDERMODE[groupchat][nick] = {'order':0}
                if ORDERMODE[groupchat][nick]['order'] == 1:
                        return

                if TESTIQCONF[groupchat]['TESTIQONOFF']:
                        q = random.choice(TESTIQCONF[groupchat]['TESTIQBD'].keys())
                        a = TESTIQCONF[groupchat]['TESTIQBD'][q]
                        jid = get_true_jid(groupchat+'/'+nick)
                        if not TESTIQP.has_key(groupchat):
                                TESTIQP[ groupchat ] = {}
                        TESTIQP[ groupchat ][ jid ] = {'question':q, 'answer':a, 'trials':TESTIQCONF[groupchat]['TESTIQTRIALS']}
                        testiq_visitor(groupchat, nick)
                        msg(groupchat+'/'+nick, TESTIQCONF[groupchat]['TESTIQBDTEXT']+'\n'+TESTIQP[ groupchat ][ jid ]['question'])

def testiq_deluser(groupchat, jid):
        global TESTIQP

        time.sleep(1)

        try:
                del TESTIQP[groupchat][jid]
        except:
                pass

def testiq_message(type, source, parameters):
        if type == 'private':
                groupchat = source[1]
                jid = get_true_jid(source[1]+'/'+source[2])
                if TESTIQP.has_key(source[1]):
                        if TESTIQP[source[1]].has_key(jid):
                                a = TESTIQP[source[1]][jid]['answer']
                                if parameters.lower() == a.lower():
                                        testiq_participant(source[1], source[2])
                                        
                                        threading.Thread(None,testiq_deluser,'iqs'+str(random.randrange(0,9999)),(groupchat, jid,)).start()
                                        
                                        msg(source[1]+'/'+source[2], TESTIQCONF[groupchat]['TESTIQBDTEXTWELCOME'])
                                else:
                                        if TESTIQP[source[1]][jid]['trials'] > 0:
                                                msg(source[1]+'/'+source[2], TESTIQCONF[groupchat]['TESTIQBDTEXTNOT'] % str(TESTIQP[source[1]][jid]['trials']))
                                                TESTIQP[source[1]][jid]['trials'] -= 1
                                        else:
                                                testiq_kick(source[1], source[2], TESTIQCONF[groupchat]['TESTIQBDTEXTNOTRESON'])

def testiq_check(type, source, parameters):
        DBPATH='dynamic/'+source[1]+'/testiq.txt'
        if not parameters:
                if TESTIQCONF.has_key(source[1]):
                        if TESTIQCONF[source[1]]['TESTIQONOFF']:
                                a = u'on'
                        else:
                                a = u'off'
                else:
                        a = u'UNDEFINED'
                if TESTIQONOFFDEF:
                        b = u'on'
                else:
                        b = u'off'
                #res = u'IQ тест v0.3\nAuthor: Gigabyte\nIdea: ManGust\nStatus of plugin: '+a+u'\nQuestions in the IQ database: '+str(len(TESTIQCONF[source[1]]['TESTIQBD'].keys()))+u'\nStatus of the plugin by default: '+b+u'\nNumber of attempts: '+str(TESTIQCONF[source[1]]['TESTIQTRIALS'])
                res = u'Status of plugin: '+a+u'\nQuestions in the IQ database: '+str(len(TESTIQCONF[source[1]]['TESTIQBD'].keys()))+u'\nStatus of the plugin by default: '+b+u'\nNumber of attempts: '+str(TESTIQCONF[source[1]]['TESTIQTRIALS'])
        else:
                if parameters == 'info':
                        #res = u'IQ test v0.3\nAuthor: Gigabyte\nIdea: ManGust\nHow this plugin works:\nThe bot give avisitor to any nick that do not have membership at the entrance, if user reply correct answer, then gets voice, if wrong reply in few times then gets kicked. The plugin has a setting in the configuration file (for admins bot)'
                        res = u'How this plugin works:\nThe bot give avisitor to any nick that do not have membership at the entrance and submit a question, if the user reply correct answer, then gets voice, if wrong reply in few times then gets kicked. The plugin has a setting in the configuration file (for admins bot)'
                elif parameters == 'on':
                        if not TESTIQCONF.has_key(source[1]):
                                TESTIQCONF[source[1]] = {'TESTIQBDTEXT': u'_للحصول على حق التحدث فى الروم_',
                                                 'TESTIQBDTEXTWELCOME': u'الأن يمكنك التحدث فى الروم',
                                                 'TESTIQBDTEXTNOT': u'اجابه خاطئه :-( , محاوله: %s',
                                                 'TESTIQBDTEXTNOTRESON': u'اسف, اجابه خاطئه !',
                                                 'TESTIQBD': {u'أكــتب كلمة |سوريا|':'سوريا'},
                                                 'TESTIQONOFF': 1,
                                                 'TESTIQTRIALS': 3}
                        else:
                                TESTIQCONF[source[1]]['TESTIQONOFF'] = 1
                        write_file(DBPATH, str(TESTIQCONF[source[1]]))
                        res = u'تم تفعيل سؤال الخاص'
                elif parameters == 'off':
                        if not TESTIQCONF.has_key(source[1]):
                                TESTIQCONF[source[1]] = {'TESTIQBDTEXT': u'_للحصول على حق التحدث فى الروم_',
                                                 'TESTIQBDTEXTWELCOME': u'الأن يمكنك التحدث فى الروم',
                                                 'TESTIQBDTEXTNOT': u'اجابه خاطئه :-( , محاوله: %s',
                                                 'TESTIQBDTEXTNOTRESON': u'اسف, اجابه خاطئه !',
                                                 'TESTIQBD': {u'أكــتب كلمة |سوريا|':'سوريا'},
                                                 'TESTIQONOFF': 0,
                                                 'TESTIQTRIALS': 3}
                        else:
                                TESTIQCONF[source[1]]['TESTIQONOFF'] = 0
                        write_file(DBPATH, str(TESTIQCONF[source[1]]))
                        res = u'تم الغاء سؤال الخاص'
                else:
                        res = u'صيغه غير معروفه'
        reply(type, source, res)

def testiq_test(groupchat, nick):
        if groupchat in TESTIQP.keys():
                if get_true_jid(groupchat+'/'+nick) in TESTIQP[groupchat].keys():
                        return 1
        return 0

def testiq_set(type, source, parameters):
        if not parameters:
                reply(type, source, u'صيغه ناقصه')
                return

        DBPATH='dynamic/'+source[1]+'/testiq.txt'
        mas = parameters.split(' ', 1)
        if len(mas) < 2:
                reply(type, source, u'Missing key')
                return

        if mas[0] in ['TESTIQBDTEXT', 'TESTIQBDTEXTWELCOME', 'TESTIQBDTEXTNOT', 'TESTIQBDTEXTNOTRESON', 'TESTIQTRIALS']:
                if TESTIQCONF.has_key(source[1]):
                        if mas[0] == 'TESTIQTRIALS':
                                try:
                                        a = int(mas[1])
                                        a = a + 2
                                        TESTIQCONF[source[1]][mas[0]] = int(mas[1])
                                except:
                                        reply(type, source, u'This parameter accepts numeric only')
                                        return
                        else:
                                TESTIQCONF[source[1]][mas[0]] = mas[1]

                        write_file(DBPATH, str(TESTIQCONF[source[1]]))
                        reply(type, source, u'تم الحفظ')
        elif mas[0] == 'BD':
                if TESTIQCONF.has_key(source[1]):
                        # iq.set BD ADD tes tes tes|5
                        if 1==1:
                                bd1 = mas[1].split(' ', 1)
                                bd_param = bd1[0]
                                
                                
                                if bd_param == 'ADD':
                                        bd_otvet = bd1[1].split('|', 1)[1]
                                        bd_vopros = bd1[1].split('|', 1)[0]
                                        TESTIQCONF[source[1]]['TESTIQBD'][bd_vopros] = bd_otvet
                                        reply(type, source, u'وأضاف')
                                        write_file(DBPATH, str(TESTIQCONF[source[1]]))
                                elif bd_param == 'GET':
                                        if len(bd1) >=2:
                                                try:
                                                        res = TESTIQCONF[source[1]]['TESTIQBD'].keys()[int(bd1[1])-1]
                                                        res += '|'+TESTIQCONF[source[1]]['TESTIQBD'][res]
                                                        reply(type, source, res)
                                                except:
                                                        reply(type, source, u'أي قضية من هذا القبيل')
#                        except:
#                                reply(type, source, u'What is missing')
#                                return
                        
#register_command_handler(testiq_set, 'برمجه-سؤال-الخاص', ['admin','all'], 20, 'Setup test IQ: edit configuration. Available keys:\nTESTIQBDTEXT - Greeting text\nTESTIQBDTEXTWELCOME - greeting text in the case of a correct answer\nTESTIQBDTEXTNOT - text in the case not the correct answer. May contain "%s" it will be replaced by number of remaining attempts\nTESTIQBDTEXTNOTRESON - text reason of kick\nTESTIQTRIALS - number of attempts to answer', 'iq', ['iq','iq yes'])
register_command_handler(testiq_check, 'سؤال-الخاص', ['admin','all'], 20, 'Setup IQ tests for all incoming users.\n * iq - common information\n * iq on/off -  on / off the system\n * iq info - about the system', 'iq', ['iq','iq yes'])
register_message_handler(testiq_message)
register_join_handler(testiq_join)
