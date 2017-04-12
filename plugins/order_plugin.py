#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  order_plugin.py

#  STORM BOT BY ALI

order_stats = {}
order_obscene_words = [u'مصيت', u'اير ', u'شرفونى', u'سرفر', u'بزاز', u'كسك', u'منيوكات', u'منتاكات', u'شراميط', u'قحبات', u'كساس', u'زباب', u'.sk', u'.ru', u'.tk', u'.am', u'ايور', u'.im', u'.org', u'http', u'www', u'.uk', u'.id', u'.net', u'.fr', u'.cz', u'.cn', u'.jp', u'fuck', u'.mobi', u'.de', u'.eu', u'.at', u'نايك', u'conference', u'ايري', u'أيري', u'إيري', u'كس امك', u'كس اختك', u'جحش', u'حمار', u'عاهر', u' امك', u' أمك', u'عرص', u'‏ كس ', u'شرموط', u'شرموطة', u'بدي نيك', u'ا ي ر ', u'ك س ', u'ش ر م و', u'org', u'com', u'حقير', u'تافه', u'بندوق', u'شر فو نا', u'يلعن', u'تلحس', u'سكساوية', u'سكس', u'حلمه', u'حلمة', u'طوبزي', u'شلحك', u'جنس', u'منتاكا', u'مليطا', u'طوبزتك', u'بلاعا', u'رضع', u'ارضع', u'برضعك', u'عاهرة', u'ممحونة', u'ممحونه', u'عاهره', u' زب', u'ايري باختك', u'بزاز', u'طيزك', u'عرصة', u'منايك', u'متناك', u'نايك', u'فاشخ', u'كسمك', u'منيوك', u'fuck', u'*FUCK*', u':FUCK:', u'ممحون', u'السكس', u'أمكن', u'اختكن', u'ب ز ا ز', u'ع ر ص', u'ن ا ي', u'ع ا ه', u'عاهر', u'قحبه', u'قحبة', u'إالحس', u'طيزى', u'طيزي', u'إيري', u'إيرى', u'أيرى', u'أيري', u'متناكين', u'ايري ', u'زوبرى', u'دعاره', u'دعارة', u'أختك', u'زورونا', u'زورونى', u'زوروني', u'نورونا', u'شرفونا', u'رومنا', u'عرصا', u'امك شرموطة', u'زورنا', u'زورو', u'ش ر ف', u'بروم', u'ق ح ب', u'عاهر', u'ز و ر', u'ا خ ت', u'أ م ك', u'ا م ك', u'نيك ‏']
order_obscene1_words = [u'']


def order_check_obscene_words(body):
	body=body.lower()
	body=u' '+body+u' '
	for x in order_obscene_words:
		if body.count(x):
			return True
	return False

def order_check_obscene1_words(body):
	body=body.lower()
	body=u' '+body+u' '
	for x in order_obscene1_words:
		if body.count(x):
			return True
	return False
	
	
def order_check_time_flood(gch, jid, nick):
	lastmsg=order_stats[gch][jid]['msgtime']
	if lastmsg and time.time()-lastmsg<=2.2:
		order_stats[gch][jid]['msg']+=1
		if order_stats[gch][jid]['msg']>3:
			order_stats[gch][jid]['devoice']['time']=time.time()
			order_stats[gch][jid]['devoice']['cnd']=1
			order_stats[gch][jid]['msg']=0
			order_kick(gch, nick, u'وقت الرسال سريع جدا :kicked: ')
			return True
		return False

def order_check_len_flood(mlen, body, gch, jid, nick):			
	if len(body)>mlen:
		order_stats[gch][jid]['devoice']['time']=time.time()
		order_stats[gch][jid]['devoice']['cnd']=1
		order_kick(gch, nick, u'فلتر الفلود 8-) ')
		return True
	return False
				
def order_check_obscene(body, gch, jid, nick):
	if order_check_obscene_words(body):
		order_stats[gch][jid]['devoice']['time']=time.time()
		order_stats[gch][jid]['devoice']['cnd']=1
		order_ban(gch, nick, u'فلتر السب & الاعـلان ;-) ')
		return True
	return False

def order_check_obscene1(body, gch, jid, nick):
	if order_check_obscene1_words(body):
		order_stats[gch][jid]['devoice']['time']=time.time()
		order_stats[gch][jid]['devoice']['cnd']=1
		order_kick(gch, nick, u'فلتر السياسة :RTFM: ')
		return True
	return False
	
def order_check_caps(body, gch, jid, nick):
	ccnt=0
	nicks = GROUPCHATS[gch].keys()
	for x in nicks:
		if body.count(x):
			body=body.replace(x,'')
	for x in [x for x in body.replace(' ', '')]:
		if x.isupper():
			ccnt+=1
	if ccnt>=len(body)/2 and ccnt>9:
		order_stats[gch][jid]['devoice']['time']=time.time()
		order_stats[gch][jid]['devoice']['cnd']=1
		order_kick(gch, nick, u'فلتر الكابيتال ;-) ')
		return True
	return False
		
def order_check_like(body, gch, jid, nick):		
	lcnt=0
	lastmsg=order_stats[gch][jid]['msgtime']
	if lastmsg and order_stats[gch][jid]['msgbody']:
		if time.time()-lastmsg>60:
			order_stats[gch][jid]['msgbody']=body.split()
		else:
			for x in order_stats[gch][jid]['msgbody']:
				for y in body.split():
					if x==y:
						lcnt+=1
			if lcnt:
				lensrcmsgbody=len(body.split())
				lenoldmsgbody=len(order_stats[gch][jid]['msgbody'])
				avg=(lensrcmsgbody+lenoldmsgbody/2)/2
				if lcnt>avg:
					order_stats[gch][jid]['msg']+=1
					if order_stats[gch][jid]['msg']>=3:
						order_stats[gch][jid]['devoice']['time']=time.time()
						order_stats[gch][jid]['devoice']['cnd']=1
						order_stats[gch][jid]['msg']=0
						order_kick(gch, nick, u'فلتر اعادة الرسالة ;-) ')
						return True
			order_stats[gch][jid]['msgbody']=body.split()
	else:
		order_stats[gch][jid]['msgbody']=body.split()
	return False

####################################################################################################

def order_kick(groupchat, nick, reason):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	kick=query.addChild('item', {'nick':nick, 'role':'none'})
	kick.setTagData('reason', get_bot_nick(groupchat)+': '+reason)
	iq.addChild(node=query)
	JCON.send(iq)
	
def order_visitor(groupchat, nick, reason):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	visitor=query.addChild('item', {'nick':nick, 'role':'visitor'})
	visitor.setTagData('reason', get_bot_nick(groupchat)+u': '+reason)
	iq.addChild(node=query)
	JCON.send(iq)
	
def order_ban(groupchat, nick, reason):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	ban=query.addChild('item', {'nick':nick, 'affiliation':'outcast'})
	ban.setTagData('reason', get_bot_nick(groupchat)+u': '+reason)
	iq.addChild(node=query)
	JCON.send(iq)
	
def order_unban(groupchat, jid):
	iq = xmpp.Iq('set')
	iq.setTo(groupchat)
	iq.setID('kick'+str(random.randrange(1000, 9999)))
	query = xmpp.Node('query')
	query.setNamespace('http://jabber.org/protocol/muc#admin')
	query.addChild('item', {'jid':jid, 'affiliation':'none'})
	iq.addChild(node=query)
	JCON.send(iq)
	
def order_check_idle():
	for gch in GROUPCHATS.keys():
		if GCHCFGS[gch]['filt']['idle']['cond']==1:
			timee=GCHCFGS[gch]['filt']['idle']['time']
			now=time.time()
			for nick in GROUPCHATS[gch].keys():
				if GROUPCHATS[gch][nick]['ishere']==1:
					if user_level(gch+'/'+nick,gch)<11:
						idle=now-GROUPCHATS[gch][nick]['idle']
						if idle > timee:
							order_kick(gch, nick, u'فلتر الصمت في الروم لفترة طويلة ;-) '+timeElapsed(idle))
	threading.Timer(120,order_check_idle).start()
	
####################################################################################################

def handler_order_message(type, source, body):
	nick=source[2]
	groupchat=source[1]
	if groupchat in GROUPCHATS.keys() and user_level(source,groupchat)<11:
		if get_bot_nick(groupchat)!=nick:
			jid=get_true_jid(groupchat+'/'+nick)
			if groupchat in order_stats and jid in order_stats[groupchat]:
				if GCHCFGS[groupchat]['filt']['time']==1:
					if order_check_time_flood(groupchat, jid, nick):	return
				if GCHCFGS[groupchat]['filt']['len']==1:
					if order_check_len_flood(900, body, groupchat, jid, nick):	return
				if GCHCFGS[groupchat]['filt']['arabic']==1:
					if order_check_obscene(body, groupchat, jid, nick):	return
				if GCHCFGS[groupchat]['filt']['caps']==1:
					if order_check_caps(body, groupchat, jid, nick):	return
				if GCHCFGS[groupchat]['filt']['like']==1:
					if order_check_like(body, groupchat, jid, nick):	return
				order_stats[groupchat][jid]['msgtime']=time.time()
							
def handler_order_join(groupchat, nick, aff, role):
	jid=get_true_jid(groupchat+'/'+nick)
	if nick in GROUPCHATS[groupchat] and user_level(groupchat+'/'+nick,groupchat)<11:
		now = time.time()
		if not groupchat in order_stats.keys():
			order_stats[groupchat] = {}
		if jid in order_stats[groupchat].keys():
			if order_stats[groupchat][jid]['devoice']['cnd']==1:
				if now-order_stats[groupchat][jid]['devoice']['time']>300:
					order_stats[groupchat][jid]['devoice']['cnd']=0
				else:
					order_visitor(groupchat, nick, u'voting rights stripped for previous violations')

			if GCHCFGS[groupchat]['filt']['kicks']['cond']==1:
				kcnt=GCHCFGS[groupchat]['filt']['kicks']['cnt']
				if order_stats[groupchat][jid]['kicks']>kcnt:
					order_ban(groupchat, nick, u'تم طردك عدة مرات ;-) ')
					return

			if GCHCFGS[groupchat]['filt']['fly']['cond']==1:
				lastprs=order_stats[groupchat][jid]['prstime']['fly']
				order_stats[groupchat][jid]['prstime']['fly']=time.time()	
				if now-lastprs<=70:
					order_stats[groupchat][jid]['prs']['fly']+=1
					if order_stats[groupchat][jid]['prs']['fly']>4:
						order_stats[groupchat][jid]['prs']['fly']=0
						fmode=GCHCFGS[groupchat]['filt']['fly']['mode']
						ftime=GCHCFGS[groupchat]['filt']['fly']['time']
						if fmode=='ban':
							order_ban(groupchat, nick, u'هدي ولو فايت طالع حولتنا >:-( ')
							time.sleep(ftime)
							order_unban(groupchat, jid)
						else:
							order_kick(groupchat, nick, u'هدي ولو فايت طالع حولتنا >:-( ')
							return
				else:
					order_stats[groupchat][jid]['prs']['fly']=0
			
			if GCHCFGS[groupchat]['filt']['arabic']==1:		
				if order_check_obscene(nick, groupchat, jid, nick):	return
			
			if GCHCFGS[groupchat]['filt']['len']==1:	
				if order_check_len_flood(20, nick, groupchat, jid, nick):	return
			
		elif nick in GROUPCHATS[groupchat]:
			order_stats[groupchat][jid]={'kicks': 0, 'devoice': {'cnd': 0, 'time': 0}, 'msgbody': None, 'prstime': {'fly': 0, 'status': 0}, 'prs': {'fly': 0, 'status': 0}, 'msg': 0, 'msgtime': 0}

	elif groupchat in order_stats and jid in order_stats[groupchat]:
		del order_stats[groupchat][jid]
	else:
		pass			

def handler_order_presence(prs):
	ptype = prs.getType()
	if ptype=='unavailable' or ptype=='error':
		return
	groupchat = prs.getFrom().getStripped()
	nick = prs.getFrom().getResource()
	stmsg = prs.getStatus()
	jid=get_true_jid(groupchat+'/'+nick)
	item=findPresenceItem(prs)
	
	if groupchat in order_stats and jid in order_stats[groupchat]:
		if item['affiliation'] in ['member','admin','owner']:
			del order_stats[groupchat][jid]
			return
	else:
		if item['affiliation']=='none':
			order_stats[groupchat][jid]={'kicks': 0, 'devoice': {'cnd': 0, 'time': 0}, 'msgbody': None, 'prstime': {'fly': 0, 'status': 0}, 'prs': {'fly': 0, 'status': 0}, 'msg': 0, 'msgtime': 0}
	
	if nick in GROUPCHATS[groupchat] and user_level(groupchat+'/'+nick,groupchat)<11:
		if groupchat in order_stats and jid in order_stats[groupchat]:
			now = time.time()
			if now-GROUPCHATS[groupchat][nick]['joined']>1:
				if item['role']=='participant':
					order_stats[groupchat][jid]['devoice']['cnd']=0
				lastprs=order_stats[groupchat][jid]['prstime']['status']
				order_stats[groupchat][jid]['prstime']['status']=now

				if GCHCFGS[groupchat]['filt']['presence']==1:
					if now-lastprs>300:
						order_stats[groupchat][jid]['prs']['status']=0
					else:
						order_stats[groupchat][jid]['prs']['status']+=1
						if order_stats[groupchat][jid]['prs']['status']>5:
							order_stats[groupchat][jid]['prs']['status']=0
							order_kick(groupchat, nick, u'presence flood!')
							return

				if GCHCFGS[groupchat]['filt']['arabic']==1:		
					if order_check_obscene(nick, groupchat, jid, nick):	return
				
				if GCHCFGS[groupchat]['filt']['prsstlen']==1 and stmsg:
					if order_check_len_flood(200, nick, groupchat, jid, nick):	return

def handler_order_leave(groupchat, nick, reason, code):
	jid=get_true_jid(groupchat+'/'+nick)
	if nick in GROUPCHATS[groupchat] and user_level(groupchat+'/'+nick,groupchat)<11:
		if groupchat in order_stats and jid in order_stats[groupchat]:
			if GCHCFGS[groupchat]['filt']['presence']==1:
				if reason=='Replaced by new connection':
					return
				if code:
					if code=='307': # kick
						order_stats[groupchat][jid]['kicks']+=1
						return
					elif code=='301': # ban
						del order_stats[groupchat][jid]
						return
					elif code=='407': # members-only
						return
			if GCHCFGS[groupchat]['filt']['fly']['cond']==1:
				now = time.time()
				lastprs=order_stats[groupchat][jid]['prstime']['fly']
				order_stats[groupchat][jid]['prstime']['fly']=time.time()
				if now-lastprs<=70:
					order_stats[groupchat][jid]['prs']['fly']+=1
				else:
					order_stats[groupchat][jid]['prs']['fly']=0

######################################################################################################################

def handler_order_filt(type, source, parameters):
	if parameters:
		parameters=parameters.split()
		if len(parameters)<2:
			reply(type,source,u'امر خاطئ')
			return
		if GCHCFGS[source[1]].has_key('filt'):
			if parameters[0]=='time':
				if parameters[1]=='0':
					reply(type,source,u'تم تعطيل فلتر الوقت ;-) ')
					GCHCFGS[source[1]]['filt']['time']=0
				elif parameters[1]=='1':
					reply(type,source,u'تم تفعيل فلتر الوقت ;-) ')
					GCHCFGS[source[1]]['filt']['time']=1
				else:
					reply(type,source,u'امر خاطئ !!')
			elif parameters[0]=='presence':
				if parameters[1]=='0':
					reply(type,source,u'تم تعطيل فلتر الوجود ;-) ')
					GCHCFGS[source[1]]['filt']['presence']=0
				elif parameters[1]=='1':
					reply(type,source,u'تم تفعيل فلتر الوجود ;-) ')
					GCHCFGS[source[1]]['filt']['presence']=1
				else:
					reply(type,source,u'امر خاطئ !!')
			elif parameters[0]=='len':
				if parameters[1]=='0':
					reply(type,source,u'تم تعطيل فلتر الفلود ;-) ')
					GCHCFGS[source[1]]['filt']['len']=0
				elif parameters[1]=='1':
					reply(type,source,u'تم تفعيل فلتر الفلود ;-) ')
					GCHCFGS[source[1]]['filt']['len']=1
				else:
					reply(type,source,u'امر خاطئ !!')
			elif parameters[0]=='like':
				if parameters[1]=='0':
					reply(type,source,u'تم تعطيل فلتر الشك ;-) ')
					GCHCFGS[source[1]]['filt']['like']=0
				elif parameters[1]=='1':
					reply(type,source,u'تم تفعيل فلتر الشك ;-) ')
					GCHCFGS[source[1]]['filt']['like']=1
				else:
					reply(type,source,u'امر خاطئ !!')
			elif parameters[0]=='caps':
				if parameters[1]=='0':
					reply(type,source,u'تم تعطيل فلتر الكابيتال ;-) ')
					GCHCFGS[source[1]]['filt']['caps']=0
				elif parameters[1]=='1':
					reply(type,source,u'تم تفعيل فلتر الكابيتال ;-) ')
					GCHCFGS[source[1]]['filt']['caps']=1
				else:
					reply(type,source,u'امر خاطئ !!')	
			elif parameters[0]=='prsstlen':
				if parameters[1]=='0':
					reply(type,source,u'تم تعطيل فلتر رسالة الحالة الطويلة ;-) ')
					GCHCFGS[source[1]]['filt']['prsstlen']=0
				elif parameters[1]=='1':
					reply(type,source,u'تم تفعيل فلتر رسالة الحالة الطويلة ;-) ')
					GCHCFGS[source[1]]['filt']['prsstlen']=1
				else:
					reply(type,source,u'امر خاطئ !!')
			elif parameters[0]=='arabic':
				if parameters[1]=='0':
					reply(type,source,u'تم تعطيل فلتر السب والشتايم ;-) ')
					GCHCFGS[source[1]]['filt']['arabic']=0
				elif parameters[1]=='1':
					reply(type,source,u'تم تفعيل فلتر السب والشتايم ;-) ')
					GCHCFGS[source[1]]['filt']['obscene']=1
				else:
					reply(type,source,u'امر خاطئ !!')
			elif parameters[0]=='matrix':
				if parameters[1]=='0':
					reply(type,source,u'تم تعطيل فلتر السياسة ;-) ')
					GCHCFGS[source[1]]['filt']['arabic']=0
				elif parameters[1]=='1':
					reply(type,source,u'تم تفعيل فلتر السياسة ;-) ')
					GCHCFGS[source[1]]['filt']['obscene']=1
				else:
					reply(type,source,u'امر خاطئ !!')
			elif parameters[0]=='fly':
				if parameters[1]=='cnt':
					try:
						int(parameters[2])
					except:
						reply(type,source,u'امر خاطئ !!')
					if int(parameters[2]) in xrange(0,121):
						reply(type,source,u'filt fly for '+parameters[2]+u' seconds')
						GCHCFGS[source[1]]['filt']['fly']['time']=int(parameters[2])	
					else:
						reply(type,source,u'no more than two minutes (120 seconds)')
				elif parameters[1]=='mode':
					if parameters[2] in ['kick','ban']:
						if parameters[2] == 'ban':
							reply(type,source,u'flying will be banned')
							GCHCFGS[source[1]]['filt']['fly']['mode']='ban'
						else:
							reply(type,source,u'flying will be kicked')
							GCHCFGS[source[1]]['filt']['fly']['mode']='kick'	
					else:
						reply(type,source,u'امر خاطئ !!')		
				elif parameters[1]=='0':
					reply(type,source,u'تم تعطيل فلتر الدخول المتكرر للروم ;-) ')
					GCHCFGS[source[1]]['filt']['fly']['cond']=0
				elif parameters[1]=='1':
					reply(type,source,u'تم تفعيل فلتر الدخول المتكرر للروم ;-) ')
					GCHCFGS[source[1]]['filt']['fly']['cond']=1
				else:
					reply(type,source,u'امر خاطئ !!')
			elif parameters[0]=='kicks':
				if parameters[1]=='cnt':
					try:
						int(parameters[2])
					except:
						reply(type,source,u'امر خاطئ !!')
					if int(parameters[2]) in xrange(2,10):
						reply(type,source,u'autoban after '+parameters[2]+u' kicks')
						GCHCFGS[source[1]]['filt']['kicks']['cnt']=int(parameters[2])	
					else:
						reply(type,source,u'from 2 to 10 kicks')
				elif parameters[1]=='0':
					reply(type,source,u'تم تعطيل فلتر الطرد ;-) ')
					GCHCFGS[source[1]]['filt']['kicks']['cond']=0
				elif parameters[1]=='1':
					reply(type,source,u'تم تفعيل فلتر الطرد ;-) ')
					GCHCFGS[source[1]]['filt']['kicks']['cond']=1
				else:
					reply(type,source,u'امر خاطئ !!')
			elif parameters[0]=='idle':
				if parameters[1]=='time':
					try:
						int(parameters[2])
					except:
						reply(type,source,u'امر خاطئ !!')			
					reply(type,source,u'طرد تلقائى لمدة '+parameters[2]+u' ثانية ('+timeElapsed(int(parameters[2]))+u')')
					GCHCFGS[source[1]]['filt']['idle']['time']=int(parameters[2])
				elif parameters[1]=='0':
					reply(type,source,u'تم تعطيل فلتر الصمت ;-) ')
					GCHCFGS[source[1]]['filt']['idle']['cond']=0
				elif parameters[1]=='1':
					reply(type,source,u'تم تفعيل فلتر الصمت ;-) ')
					GCHCFGS[source[1]]['filt']['idle']['cond']=1
			else:
				reply(type,source,u'امر خاطئ !!')
				return					
			DBPATH='dynamic/'+source[1]+'/config.cfg'
			write_file(DBPATH, str(GCHCFGS[source[1]]))
		else:
			reply(type,source,u'خطأ فى البوت يرجى التوجة الى مديرين البوت')
	else:
		rep,foff,fon=u'',[],[]
		time=GCHCFGS[source[1]]['filt']['time']
		prs=GCHCFGS[source[1]]['filt']['presence']
		flen=GCHCFGS[source[1]]['filt']['len']
		like=GCHCFGS[source[1]]['filt']['like']
		caps=GCHCFGS[source[1]]['filt']['caps']
		prsstlen=GCHCFGS[source[1]]['filt']['prsstlen']
		obscene=GCHCFGS[source[1]]['filt']['arabic']
		fly=GCHCFGS[source[1]]['filt']['fly']['cond']
		flytime=str(GCHCFGS[source[1]]['filt']['fly']['time'])
		flymode=GCHCFGS[source[1]]['filt']['fly']['mode']
		kicks=GCHCFGS[source[1]]['filt']['kicks']['cond']
		kickscnt=str(GCHCFGS[source[1]]['filt']['kicks']['cnt'])
		idle=GCHCFGS[source[1]]['filt']['idle']['cond']
		idletime=GCHCFGS[source[1]]['filt']['idle']['time']
		if time:
			fon.append(u'فلتر الوقت هو فلتر لايقاف الرسائل السريعة برومك')
		else:
			foff.append(u'filt time')
		if prs:
			fon.append(u'فلتر الوجود هو لايقاف سرعة تغيير الحالة')
		else:
			foff.append(u'filt presence')
		if flen:
			fon.append(u'فلتر الفلود هو لايقاف الفلود بالروم')
		else:
			foff.append(u'filt len')
		if like:
			fon.append(u'فلتر الشك هو لايقاف اى شخص مشتبة او مشكوك فيه بالروم')
		else:
			foff.append(u'filt like')
		if caps:
			fon.append(u'فلتر الكابيتال لايقاف التكلم فى الروم بحروف كابيتال')
		else:
			foff.append(u'filt caps')
		if prsstlen:
			fon.append(u'فلتر الحاله الطويلة وهو لايقاف الحالة الطويلة')
		else:
			foff.append(u'filt prsstlen')
		if obscene:
			fon.append(u'فلتر ارابيك وهو لايقاف السب والشتيمة فى الروم')
		else:
			foff.append(u'filt arabic')
		if fly:
			fon.append(u'فلتر التحليق وهو لمنع الدخول والخروج المتكرر لشخص فى الروم')
		else:
			foff.append(u'filt fly')
		if kicks:
			fon.append(u'فلتر الطرد يقوم بفصل من يتم طرده ثلاث مرات')
		else:
			foff.append(u'filt kicks')
		if idle:
			fon.append(u'فلتر الصمت وهو لايقاظ الصامتين فى الروم لمده معينة عن طريق طردهم')
		else:
			foff.append(u'filt idle')
		fon=u', '.join(fon)
		foff=u', '.join(foff)
		if fon:
			rep+=u'الفعالين\n'+fon+u'\n\n'
		if foff:
			rep+=u'المعطلين\n'+foff
		reply(type,source,rep.strip())


def get_order_cfg(gch):
	if not 'filt' in GCHCFGS[gch]:
		GCHCFGS[gch]['filt']={}		
	for x in ['time','presence','len','like','caps','prsstlen','arabic','kicks','fly','excess','idle']:
		if x == 'excess':
			if not x in GCHCFGS[gch]['filt']:
				GCHCFGS[gch]['filt'][x]={'cond':0, 'mode': 'kick'}
			continue		
		if x == 'kicks':
			if not x in GCHCFGS[gch]['filt']:
				GCHCFGS[gch]['filt'][x]={'cond':1, 'cnt': 2}
			continue
		if x == 'fly':
			if not x in GCHCFGS[gch]['filt']:
				GCHCFGS[gch]['filt'][x]={'cond':1, 'mode': 'ban', 'time': 60}
			continue
		if x == 'idle':
			if not x in GCHCFGS[gch]['filt']:
				GCHCFGS[gch]['filt'][x]={'cond':0, 'time': 3600}
			continue
		if not x in GCHCFGS[gch]['filt']:
			GCHCFGS[gch]['filt'][x]=1

register_message_handler(handler_order_message)
register_join_handler(handler_order_join)
register_leave_handler(handler_order_leave)
register_presence_handler(handler_order_presence)
register_command_handler(handler_order_filt, 'filt', ['ادمن','عام','all'], 20, 'تفعيل او تعطيل امر من هذة الاوامر فى الروم.\ntime = فلتر لايقاف الرسائل السريعة برومك\nlen = فلتر ايقاف اى فلود على رومك\npresence = فلتر لايقاف وجود اى شك للفود برومك\nlike = فلتر لايقاف اى خطأ بالروم\ncaps = فلتر لايقاف الحروف الكابيتال بالروم\nprsstlen = فلتر لايقاف الحالة الطويلة برومك\narabic = فلتر يمنع اى زائر بالروم من الاعلان او السب\nfly = فلتر لايقاف دخول وخروج متكرر لزائر فى الروم, ولها حالتان الطرد او الفصل\nidle = فلتر لايقاف الزوار الصامتين بالروم اى متواجدين بالروم اكتر من عشر دقائق ;-) ', 'filt [filt] [mode] [status]', ['filt arabic 1', 'filt arabic 0','filt fly mode ban'])

register_stage1_init(get_order_cfg)
register_stage2_init(order_check_idle)
