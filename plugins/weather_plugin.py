#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  weather_plugin.py

#  STORM BOT BY ALI

import pymetar

WEATHERCODE_FILE = 'static/weather.txt'

def handler_weather_weather(type, source, parameters):
	if not parameters:
		reply(type, source, u'وبعدين مابدك تحل عني ؟')
		return
	try:
		rf=pymetar.ReportFetcher(parameters.strip())
		fr=rf.FetchReport()
	except Exception, ex:
		results = u'هل يوجد كود مماثل؟'
		return
	rp=pymetar.ReportParser()
	pr=rp.ParseReport(fr)
	tm=time.strptime(pr.getISOTime(), '%Y-%m-%d %H:%M:%SZ')
	tm=time.strftime('%H:%M:%S',tm)
	rep = u'احوال جويه in %s (%s) on %s\n%s, درجه حراره: %s° C, رطوبه: %s%%, ' %(pr.getStationName(), parameters.strip(), tm, pr.getWeather(), pr.getTemperatureCelsius(), pr.getHumidity())
	if pr.getWindSpeed():
		rep+='رياح: %s, ' %(pr.getWindSpeed())
	if pr.getPressure():
		rep+='الضغط: %s, ' %(pr.getPressure())
	rep+='حاله السماء: %s' %(pr.getSkyConditions())
	reply(type, source, rep)

def handler_weather_weathercode(type, source, parameters):
	if not parameters:
		reply(type, source, u'في شغله أنت يافهمان ما كتبتا؟؟؟؟')
		return
	if len(parameters)<=2:
		reply(type, source, u'شيء من الهبل؟؟؟')
		return
	results = ''
	query = string.lower(parameters)
	fp = open(WEATHERCODE_FILE, 'r')
	lines = fp.readlines()
	for line in lines:
		if string.count(string.lower(line), query):
			results += string.split(line, '=> ')[0]
	if results:
		reply(type, source, results)
	else:
		reply(type, source, u'*dntknw*')

register_command_handler(handler_weather_weather, 'الطقس', ['info','all'], 10, 'Looks a weather from NOAA', 'weather <4th_letters_code_city>', ['weather wiii'])
register_command_handler(handler_weather_weathercode, 'كود-طقس', ['info','all'], 10, 'Shows the code of city for viewing of weather', 'code <city>', ['code jakarta'])
