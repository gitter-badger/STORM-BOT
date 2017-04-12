#===istalismanplugin===
# -*- coding: utf-8 -*-


#  AvAtAr plugin
#  trans_plugin.py
#  STORM BOT BY ALI
import re, os, math, time

def handler_time_now(type, source, parameters):
	weekday = [u'الجمعة', u'السبت', u'الاحد', u'الاثنين', u'الثلاثاء', u'الاربعاء', u'الخميس']
	mounthall = [u'كانون الثاني', u'شباط', u'اذار', u'نيسان', u'ايار', u'تموز', u'حزيران', u'اب', u'ايلول', u'تشرين الاول', u'تشرين الثاني', u'كانون الاول']
	week_ = time.strftime('%w', time.localtime()).decode('utf-8')
	week = weekday[int(week_)-1]
	month_ = time.strftime('%m', time.localtime()).decode('utf-8')
	month = mounthall[int(month_)-1]
	year = time.strftime('%y', time.localtime()).decode('utf-8')
	day = time.strftime('%d', time.localtime()).decode('utf-8')

	hour = time.strftime('%H', time.localtime()).decode('utf-8')
	min = time.strftime('%M', time.localtime()).decode('utf-8')
	sec = time.strftime('%S', time.localtime()).decode('utf-8')
	
	reply(type, source, u'وقت وتاريخ السيرفر (+6):\n '+week +' '+ day +' '+ month +' '+ year +' '+ hour +':'+min+'.'+sec)

def handler_auto_top(type, source, parameters):
	weekday = [u'الجمعة', u'السبت', u'الاحد', u'الاثنين', u'الثلاثاء', u'الاربعاء', u'الخميس']
	mounthall = [u'كانون الثاني', u'شباط', u'اذار', u'نيسان', u'ايار', u'تموز', u'حزيران', u'اب', u'ايلول', u'تشرين الاول', u'تشرين الثاني', u'كانون الاول']
	week_ = time.strftime('%w', time.localtime()).decode('utf-8')
	week = weekday[int(week_)-1]
	month_ = time.strftime('%m', time.localtime()).decode('utf-8')
	month = mounthall[int(month_)-1]
	year = time.strftime('%y', time.localtime()).decode('utf-8')
	day = time.strftime('%d', time.localtime()).decode('utf-8')

	hour = time.strftime('%H', time.localtime()).decode('utf-8')
	min = time.strftime('%M', time.localtime()).decode('utf-8')
	sec = time.strftime('%S', time.localtime()).decode('utf-8')
	date = week +' '+ day +' '+ month +' '+ year +' '+ hour +':'+min+'.'+sec
	conf = source[1]
	DBPATH='dynamic/'+source[1]+'/autotop.txt'
	if check_file(source[1],'autotop.txt'):
		topdb = eval(read_file(DBPATH))
		top = parameters
		top = top + u'\n' + date
		topdb = top
		node=xmpp.simplexml.XML2Node(unicode("<message to='"+conf+"'  type='groupchat'><subject>"+topdb+"</subject></message>").encode('utf8'))
		JCON.send(node)
		reply(type, source, u'تم تعين الموضوع')

register_command_handler(handler_auto_top, 'الموضوع', [], 20, 'تعين موضوع للغرفة', 'موضوع [نص الموضوع]', ['موضوع'])
register_command_handler(handler_time_now, 'الوقت', [], 0, 'لمعرفة الوقت', 'الوقت', ['الوقت'])
