#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  calendar_plugin.py

#  STORM BOT BY ALI

import calendar

def space2number(number):
	if number <= 9:
		number = ' %s ' % (number)
	else:
		number = '%s ' % (number)
	return number

def month_cal(type, sourse, body):
	text = body.split()
	try:
		month = int(text[0])
	except:
		month = tuple(time.gmtime())[1]
	try:
		year = int(text[1])
	except:
		year = tuple(time.gmtime())[0]
	try:
		smbl = text[2]
	except:
		smbl = '_'
	repl = u'\ NPN تاريخ اليوم\n'
	try:
		for x in calendar.monthcalendar(year, month):
			for y in x:
				if y:
					repl += space2number(y)
				else:
					repl += '   '
			repl = repl[:-1]+'\n'
		repl = u'\هو: %s%s' '' % (time.strftime('%d.%m.%Y (%H:%M:%S)', time.gmtime()), repl[:-1].replace(' ', smbl))
	except:
		repl = u'خطأ!'
	reply(type, sourse, repl)

register_command_handler(month_cal, 'تقويم', ['инфо','все'], 10, 'Показ календаря. Без параметров показывает календарь на текущий месяц\nPorted by WitcherGeralt', 'календарь [месяц][год][символ_разделитель]', ['календарь'])
