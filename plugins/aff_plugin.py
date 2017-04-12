#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  ping_plugin.py

#  STORM BOT BY ALI

aff_pending=[]
def handler_aff(typ, source, parameters):
	aff_list={u"مشرف":{'role':'moderator'},u"عضو": {'affiliation':'member'},u"مشارك":{'role':'participant'},u"فصل": {'affiliation':'outcast'},u'اونر':{'affiliation':'owner'},u'مدير':{'affiliation':'admin'}}
	#if typ=="public":
		#reply(typ, source, u"Дурик, это надо писать в приват!")
		#return

	if not aff_list.has_key(parameters):
		reply(typ, source, u"انا لا اعرف هذه الكلمه :-|")
		return

	groupchat=source[1]
	id = 'a'+str(random.randrange(1, 1000))
	globals()['aff_pending'].append(id)
	iq=xmpp.Iq('get',to=groupchat,queryNS=xmpp.NS_MUC_ADMIN,xmlns=None)
	iq.getQueryChildren().append(xmpp.Protocol('item',attrs=aff_list[parameters]))
	iq.setID(id)
	param=''
	JCON.SendAndCallForResponse(iq, handler_aff_answ,{'mtype': typ, 'source': source, 'param': param})
	return

def handler_aff_answ(coze, res, mtype, source, param):
	id = res.getID()
	if id in globals()['aff_pending']:
		globals()['aff_pending'].remove(id)
	else:
		print 'someone is doing wrong...'
		return
	if res:
		if res.getType() == 'result':
		#-=
			aa=res.getTag("query")
                        if aa==None:
                                rep=u"fatal error, unable to query"
                        else:
                                m=aa.getTags("item")
                                if len(m)==0:
                                        rep=u"خالى ياغالي "
                                else:
                                        rep=""
                                        for t in m:
                                                ats=t.getAttrs()
                                                if ats.has_key("jid"):
                                                        rep+=t["jid"]+" "
                                                if ats.has_key("affiliation"):
                                                        rep+=t["affiliation"]+" "
                                                if ats.has_key("role"):
                                                        rep+=t["role"]+" "
                                                reas=t.getTag("reason")
                                                if reas!= None:
                                                        dt=reas.getData()
                                                        if dt!=None:
                                                                rep+=dt+" "
                                                rep+="\n"
		#-=
		else:
			rep = u'لا استطيع :ermm:'
	if mtype=="public":
		reply(mtype, source, u"شوفني بالخاص يلا ياغالي ;-)")
	reply("private", source, rep)
	
register_command_handler(handler_aff, 'قائمة', ['info','muc','admin','all'], 20, 'show affiliation list in the current conference', 'aff <type>', ['aff owner','aff admin','aff moderator','aff member','aff participant','aff outcast'])
