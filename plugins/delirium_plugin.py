#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  commoff_plugin.py

#  STORM BOT BY ALI

poke_nicks={}

def handler_poke(type, source, parameters):
	if type=='private':
		reply(type,source,u':-P')
		return
	groupchat = source[1]
	if parameters:
		if parameters==u'مشاركة 10':
			cnt=0
			rep=''
			nicks = set()
			for x in [poke_nicks[source[1]] for x in poke_nicks]:
				nicks = nicks | set(x)
			for x in nicks:
				cnt=cnt+1
				rep += str(cnt)+u') '+x+u'\n'
			reply('private',source,rep[:-1])
			return
		if not poke_nicks.has_key(source[1]):
			poke_nicks[source[1]]=source[1]
			poke_nicks[source[1]]=[]
		if len(poke_nicks[source[1]])==10:
			poke_nicks[source[1]]=[]
		else:
			poke_nicks[source[1]].append(source[2])
		if not parameters == get_bot_nick(source[1]):
			if parameters in GROUPCHATS[source[1]]:
				pokes=[]
				pokes.extend(poke_work(source[1]))
				pokes.extend(eval(read_file('static/delirium.txt'))['poke'])
				rep = random.choice(pokes)
				msg(source[1],u'/أنا '+rep % parameters)
			else:
				reply(type, source, u'اين هو؟ :-O')
		else:
			reply(type, source, u'ذكى, صعبه, صح؟ ]:->')	
	else:
		reply(type, source, u'ما في:-|')
		
def handler_poke_add(type, source, parameters):
	if not parameters:
		reply(type, source, u'وبعدين:-?')
	if not parameters.count('%s'):
		reply(type, source, u'ما عم شوفو:BOTAN: %s')
		return
	res=poke_work(source[1],1,parameters)
	if res:
		reply(type, source, u'تمت الاضافه')
	else:
		reply(type, source, u'غير ظاهر')
		
def handler_poke_del(type, source, parameters):
	if not parameters:
		reply(type, source, u'و؟ :-|')
	if parameters=='*':
		parameters='0'
	else:
		try:
			int(parameters)
		except:
			reply(type,source,u'تم الغاء الامر')
	res=poke_work(source[1],2,parameters)
	if res:
		reply(type, source, u'تم المسح')
	else:
		reply(type, source, u'غير ظاهر')
		
def handler_poke_list(type, source, parameters):
	rep,res=u'',poke_work(source[1],3)
	if res:
		res=sorted(res.items(),lambda x,y: int(x[0]) - int(y[0]))
		for num,phrase in res:
			rep+=num+u') '+phrase+u'\n'
		reply(type,source,rep.strip())
	else:
		reply(type,source,u'لاتوجد عبارات مخصصه')
		
def handler_test(type, source, parameters):
	reply(type,source,u'شغال وبقوة:THUMBS UP: ')
	
def handler_clean_conf(type, source, parameters):
	if GROUPCHATS.has_key(source[1]):
		for x in range(1, 21):
			msg(source[1], '')
			time.sleep(1.3)
		reply('private',source,u'تم تنظيف الروم ;-)')
		
def handler_afools_control(type, source, parameters):
	if parameters:
		try:
			int(parameters)
		except:
			reply(type,source,u'تم الغاء الامر')
		if int(parameters)>1:
			reply(type,source,u'تم الغاء الامر')
		if parameters=="1":
			GCHCFGS[source[1]]['afools']=1
			reply(type,source,u'تم تفعيل امر المسح')
		else:
			GCHCFGS[source[1]]['afools']=0
			reply(type,source,u'تم الغاء تفعيل امر المسح')			
	else:
		if GCHCFGS[source[1]]['afools']==1:
			reply(type,source,u'تم تفعيل امر المسح')
		else:
			reply(type,source,u'تم الغاء تفعسل امر المسح')
	
			
def get_afools_state(gch):
	if not 'afools' in GCHCFGS[gch]:
		GCHCFGS[gch]['afools']=0
		
def poke_work(gch,action=None,phrase=None):
	DBPATH='dynamic/'+gch+'/delirium.txt'
	if check_file(gch,'delirium.txt'):
		pokedb = eval(read_file(DBPATH))
		if action==1:
			for x in range(1, 21):
				if str(x) in pokedb.keys():
					continue
				else:
					pokedb[str(x)]=phrase
					write_file(DBPATH, str(pokedb))
					return True
			return False
		elif action==2:
			if phrase=='0':
				pokedb.clear()
				write_file(DBPATH, str(pokedb))
				return True
			else:
				try:
					del pokedb[phrase]
					write_file(DBPATH, str(pokedb))
					return True
				except:
					return False
		elif action==3:
			return pokedb
		else:
			return pokedb.values()
	else:
		return None
		
def remix_string(parameters):
	remixed=[]
	for word in parameters.split():
		tmp=[]
		if len(word)<=1:
			remixed.append(word)
			continue
		elif len(word)==2:
			tmp=list(word)
			random.shuffle(tmp)
			remixed.append(u''.join(tmp))
		elif len(word)==3:
			tmp1=list(word[1:])
			tmp2=list(word[:-1])
			tmp=random.choice([tmp1,tmp2])
			if tmp==tmp1:
				random.shuffle(tmp)
				remixed.append(word[0]+u''.join(tmp))
			else:
				random.shuffle(tmp)
				remixed.append(u''.join(tmp)+word[-1])					
		elif len(word)>=4:
			tmp=list(word[1:-1])
			random.shuffle(tmp)
			remixed.append(word[0]+u''.join(tmp)+word[-1])
	return u' '.join(remixed)

def handler_kick_ass(type, source, parameters):
	if GROUPCHATS.has_key(source[1]):
		if len(parameters.split()) == 3:
			splitdata = string.split(parameters)
			rep,jid,msgnum,smlnum = '','',int(splitdata[1]),int(splitdata[2])
			if msgnum>500 or smlnum>500:
				reply(type,source,u'اسف :-(')
				return
			reply(type,source,u'جارى الاسباااااام :CRAZY:')
			if splitdata[0]==u':)':
				for x in range(0, msgnum):
					for y in range(0, smlnum):
						rep += u'*CRAZY* '
					msg(source[1], rep)
					rep = ''
#					time.sleep(0.5)
			else:
				if splitdata[0].count('@'):
					jid=splitdata[0]
				else:
					jid=source[1]+'/'+splitdata[0]
				print jid
				for x in range(0, msgnum):
					for y in range(0, smlnum):
						rep += u'*CRAZY* '
					msg(jid, rep)
					rep=''
#					time.sleep(0.5)
			reply(type,source,u'تم :THUMBS UP:')
		else:
			reply(type,source,u'امر خاطئ. اقرا الاوامر')
	
register_command_handler(handler_poke, 'صحصح', ['مرح','الكل','صحصح'], 10, ' كزة للمستخدم. يجبره على إيلاء اهتمام لكم /في دردشة.\nlast10 وسوف تظهر آخر قائمة النكات مطعون بدلا من الاسم المستعار.', 'صحصح <الاسم>|<параметр>', ['صحصح qwerty','صحصح + пришиб %s','صحصح - 2','صحصح *'])
register_command_handler(handler_poke_add, 'صحصح+', ['مرح','الكل','صحصح'], 20, ' إضافة عبارات مخصصة. المتغير %s في هذه العبارة يشير إلى مكان لادخال اسم مستعار (معيار إلزامي). يجب أن تكتب هذه العبارة من قبل شخص ثالث، فإنه سيتم استخدام النموذج التالي "/لي عبارتك". أقصى عدد من العبارات العرف هو 20 حرفا.', 'صحصح+ <phrase>', ['صحصح+ sing %s'])
register_command_handler(handler_poke_del, 'صحصح-', ['مرح','الكل','صحصح'], 20, 'حذف عبارة مخصص. كتابة عدد من عبارة لمحو الكلمات، فإن بوت حذفه بشكل دائم. كتابة الأوامر "صحصح*" لعرض قائمة. من أجل حذف كل العبارات تحديد فقط "*" بدلا من عدد العبارة.', 'صحصح- <رقم>', ['صحصح- 5','صحصح- *'])
register_command_handler(handler_poke_list, 'صحصح*', ['مرح','الكل','صحصح'], 20, 'عرض قائمة من جميع العبارات العرف ورقمه.', 'صحصح*', ['صحصح*'])
register_command_handler(handler_test, 'اختبار', ['مرح','معلومات','الكل'], 0, 'مرت الأجوبة ببساطة.', 'اختبار', ['اختبار'])
register_command_handler(handler_test, 'تست', ['مرح','معلومات','الكل'], 0, 'للتأكد من عمل البوت.', 'تست', ['تست'])
register_command_handler(handler_clean_conf, 'تنظيف', ['مرح','عام','الكل'], 30, 'المؤتمر الحالي نظيفة (مع حرف فارغة).', 'تنظيف', ['تنظيف'])
register_command_handler(handler_afools_control, 'النكت', ['مرح','عام','الكل'], 30, 'ويمكن تعطيل النكات والسير، والتي بوت أحيانا بدائل (يتم تنفيذ الأمر دائما!) استجابة قياسي من أوامر.', 'النكت <1|0>', ['النكت 1','النكت 0'])

#  listed below command handler are not recommended
register_command_handler(handler_kick_ass, 'سبام', ['مرح','اونر','عام','الكل'], 100, 'البريد الالكتروني غير المرغوب 1 JID في المؤتمر الحالي مع ابتسامات ( :) ).\nالهدف من الرسائل غير المرغوب فيها وتحديد من قبل المعلمة الأولى <الاسم>.\nتكرار الرسائل غير المرغوب فيها وتحديد من قبل المعلمة الثانية <كمية>.\nكمية الرسائل غير المرغوب فيها التي تحددها المعلمة الثالث<كمية>.\nاكتب هذا الأمر في القطاع الخاص.', 'سبام <الاسم> <كمية> <كمية>', ['سبام شخص 1000 10','سبام شخص 500 8'])

register_stage1_init(get_afools_state)
