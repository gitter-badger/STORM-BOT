#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  google_plugin.py

#  STORM BOT BY ALI


def google_remove_html(text):
	nobold = text.replace('<b>', '').replace('</b>', '')
	nobreaks = nobold.replace('<br>', ' ')
	noescape = nobreaks.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
	return noescape

def google_search(query):
	try:
		req = urllib2.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s' % urllib2.quote(query.encode('utf8')))
	except urllib2.HTTPError, e:
		reply(type,source,str(e))
		return
	answ=json.load(req)
	results=answ['responseData']['results']
	if results:
		titleNoFormatting=results[0]['titleNoFormatting']
		content=results[0]['content']
		url=results[0]['unescapedUrl']
		return google_remove_html(titleNoFormatting+u'\n'+content+u'\n'+url)
	elif answ['responseDetails']:
		return answ['responseDetails']
	else:
		return


def handler_google_google(type, source, parameters):
	results = google_search(parameters)
	if results:
		reply(type, source, results)
	else:
		reply(type, source, u'والله يامعلم مالقيت شي :-D ')

try:
	import json
	register_command_handler(handler_google_google, 'جوجل', ['fun','all'], 0, 'search in google.', 'google <query>', ['search something'])
except ImportError:
	try:
		import simplejson as json
		register_command_handler(handler_google_google, 'جوجل', ['fun','all'], 0, 'search in google.', 'google <query>', ['search something'])
	except:
		print '====================================================\nYou need Python 2.6.x or simple_json package installed to use google_plugin.py!!!\n====================================================\n'
