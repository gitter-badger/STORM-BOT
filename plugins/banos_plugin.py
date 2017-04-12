#===istalismanplugin===
# -*- coding: utf-8 -*-
#  STORM BOT BY ALI

version_pendingg=[]

def handler_banos(groupchat, nick, aff, role):
        if check_file(groupchat,'banver.txt'):
                jid=groupchat+'/'+nick
                iq = xmpp.Iq('get')
                id='vers'+str(random.randrange(1000, 9999))
                globals()['version_pendingg'].append(id)
                iq.setID(id)
                iq.addChild('query', {}, [], 'jabber:iq:version');
                jid=groupchat+'/'+nick
                iq.setTo(jid)
                JCON.SendAndCallForResponse(iq, handler_version4_answ, {'groupchat': groupchat, 'nick': nick})
                return

def handler_version4_answ(coze, res, groupchat, nick):
	id=res.getID()
	if id in globals()['version_pendingg']:
		globals()['version_pendingg'].remove(id)
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
			#if name:
				#rep = name
			if version:
                                if os:
                                        gfr = version+' '+os
                                        BANVER = 'dynamic/'+groupchat+'/banver.txt'
                                        fp = open(BANVER, 'r')
                                        banver = eval(fp.read())
                                        tojid = groupchat+'/'+nick
                                        if gfr in banver:
                                                govn=get_true_jid(groupchat+'/'+nick)
                                                node='<item affiliation="outcast" jid="'+govn+u'"><reason>فصل تلقائى للنسخه.</reason></item>'
                                                node=xmpp.simplexml.XML2Node(unicode('<iq from="'+JID+'/'+RESOURCE+'" id="ban1" to="'+groupchat+'" type="set"><query xmlns="http://jabber.org/protocol/muc#admin">'+node+'</query></iq>').encode('utf8'))
                                                JCON.send(node)
                                                return

def banver_subscribe(type, source, parameters):
        #parameters = reewf
        BANVER = 'dynamic/'+source[1]+'/banver.txt'
        fp = open(BANVER, u'r')
        juk = eval(read_file(BANVER))
        if parameters:
                if parameters in juk:
                        reply(type, source, u'هــ♥ــذه النســـ♥ــخه مــ♥ـوجــوده حـــ♥ـاليا فى قائـ♥ـمه الفصـ♥ـــل ;-)')
                        return
                #if parameters in NOBANN5:
                        #reply(type, source, u'низзя')
                        #return
                else:
                        juk[parameters] = {}
                        write_file(BANVER,str(juk))
                        fp.close()
                        reply(type, source, u'هذا الأصدار'+parameters+u' الان فى قائمه الفصل ;-)')

def banver_show(type, source, parameters):
    BANVER = 'dynamic/'+source[1]+'/banver.txt'
    fp = open(BANVER, 'r')
    juk = eval(read_file(BANVER))
    fp.close()
    if len(juk) == 0:
      reply(type, source, u'القائمه خاليه :-|')
      return
    p =1
    spisok = ''
    for usr in juk:
          spisok += str(p)+'. '+usr+'\n'
          p +=1
    reply(type, source, u'(المجموع '+str(len(juk))+u'):\n'+spisok)

def banver_unsubscribe(type, source, parameters):
      BANVER = 'dynamic/'+source[1]+'/banver.txt'
      if parameters:
            fp = open(BANVER, 'r')
            juk = eval(read_file(BANVER))
            fp.close()
            if parameters in juk:
                    del juk[parameters]
            else:
                  reply(type, source, u'غير موجود')
                  return
            write_file(BANVER,str(juk))

            reply(type, source, u'هذا الأصدار '+parameters+u' تمت ازالتها من قائمه الفصل :THUMBS UP:')
	
register_join_handler(handler_banos)
register_command_handler(banver_subscribe, 'فصل-نسخه', ['all'], 20, 'Menambahkan version and OS ke dalam ban list', 'banver+ <version><os>', ['banver+ 9032 Windows XP'])
register_command_handler(banver_show, 'قائمه-فصل-نسخه', ['all'], 20, 'Menampilkan daftar client version ban list', 'banver_show', ['banver_show'])
register_command_handler(banver_unsubscribe, 'الغاء-فصل-نسخه', ['all'], 20, 'Menghapus versi and OS dalam ban list', 'banver- <version>', ['banver- 9032 Windows XP'])

