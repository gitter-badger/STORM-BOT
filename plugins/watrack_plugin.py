#===istalismanplugin===
# -*- coding: utf-8 -*-

# Talisman rev84 plugin
#  STORM BOT BY ALI


WATRACKS=[]

def watrack_get():
	global WATRACKS
	return random.choice(WATRACKS)



def watrack_loop(groupchat):
	while 1:
		if GCHCFGS.has_key(groupchat) and GCHCFGS[groupchat].has_key('watrack') and GCHCFGS[groupchat]['watrack'] and not GCHCFGS[groupchat]['autoaway']:
			change_bot_status(groupchat, 'استمع الى الاغاني: ' + watrack_get(), GCHCFGS[groupchat]['status']['show'])
			time.sleep(random.randrange(180, 480))   # Время смены: от и до
		else:
			GCHCFGS[groupchat]['watrack']=0
			break
	

def watrack_init(groupchat):
	if check_file(groupchat,'watrack.txt'):
		if not GCHCFGS.has_key(groupchat):
			GCHCFGS[groupchat]={}
		if read_file('dynamic/'+groupchat+'/watrack.txt')=='on':
			GCHCFGS[groupchat]['watrack']=1
			GCHCFGS[groupchat]['autoaway']=0
			LAST['gch'][groupchat]['autoaway']=0
			LAST['gch'][groupchat]['thr']=None
			watrack_loop(groupchat)
		else:
			GCHCFGS[groupchat]['watrack']=0
			
			
def watrack_call(type, source, parameters):
	global WATRACKS
	global GCHCFGS
	groupchat=source[1]
	PATH='dynamic/'+source[1]+'/watrack.txt'
	if parameters:
		if check_file(source[1],'watrack.txt'):
			if parameters=='تفعيل' or parameters=='1' or parameters==u'вкл':
				if GCHCFGS[groupchat]['watrack']:	
					reply(type, source, u'الاغانى مفعله :-| ')
				else:
					write_file(PATH, 'تغعيل')
					GCHCFGS[groupchat]['watrack']=1
					reply(type, source, u'تم تفعيل الاغانى :THUMBS UP:')					
					GCHCFGS[groupchat]['autoaway']=0
					LAST['gch'][groupchat]['autoaway']=0
					LAST['gch'][groupchat]['thr']=None
					watrack_loop(groupchat)
			elif parameters=='ايقاف' or parameters=='0' or parameters==u'выкл':
				write_file(PATH, 'ايقاف')
				GCHCFGS[groupchat]['watrack']=0
				change_bot_status(groupchat, GCHCFGS[groupchat]['status']['status'], GCHCFGS[groupchat]['status']['show'],)
				reply(type, source, u'تم الغاء تفعيل الاغانى :THUMBS UP: ')
			else:
				reply(type, source, u'اقرا المساعده ;-) ')
	else:
		if not GCHCFGS[groupchat]['watrack']:
			reply(type, source, u'لقد الغيت تفعيل الاغاني!')
		else:
			reply(type, source, u'الاغانى موجوده :-|')

def watrack_load():
	global WATRACKS
	files=[]
	obj = os.listdir('static')
	for x in obj:
		if x[-4:].lower() == '.m3u':
			files.append(x)
	for x in files:
		a = read_file('static/' + x)
		a=a.split('EXTINF')[1:-1]
		for z in a:
			try:
				z = unicode(z,'windows-1251')
				WATRACKS.append(z[(z.find(',') + 1):].strip().split('\n')[0])
			except:
				pass
	if not len(WATRACKS):
		WATRACKS=['no lists loaded']
		print 'لاتوجد قائمه للاغانى'
			

register_stage0_init(watrack_load)			
register_stage1_init(watrack_init)

register_command_handler(watrack_call, 'اغانى', ['all', 'мук'], 20, "Включение/отключение Watrack'a на боте. (Бот периодически меняет статус, указывая в нем рандомную песню)", 'watrack [<on/1/вкл/off/0/выкл>]', ['watrack on','watrack off'])	
	
