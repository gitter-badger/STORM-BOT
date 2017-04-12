#===istalismanplugin===
# -*- coding: utf-8 -*-

#  STORM BOT BY ALI


def telcode(type, source, text):
	if len(text):
		query = urllib.urlencode({'text' : text.encode("windows-1251")})
		url = u'http://www.telcode.ru/mob/select.asp?%s'.encode("utf-8") % (query)
		f = urllib.urlopen(url)
		body = f.read()
		f.close()
		body = html_encode(body)
		if body.count(u'found records'): msg = u'found!'
		else:
			msg = rss_del_html(get_tag(body,'h3'))+' ... '
			city = body.replace('\n','').replace('\r','').split('</h3>')[1].split('<br> <br>')[0].split('<br>')
			for tmp in city: msg += get_tag(tmp,'a')+', '
			msg = msg[:-2]
	else: msg = u'عن ماذا نبحث؟'
	reply(type, source, msg)

def tcode(type, source, text):
	if len(text):
		try: csize = int(text.split('\n')[1])
		except: csize = 3
		if csize < 1: csize = 1
		elif csize > 25: csize = 25
		text = text.split('\n')[0]
		try: url = u'http://www.btk-online.ru/phcode/?srchCId=1&srchTName=&srchCCode=&srchTCode='+str(int(text))
		except: url = u'http://www.btk-online.ru/phcode/?srchCId=1&%s'.encode("utf-8") % (urllib.urlencode({'srchTName': text.encode("windows-1251")}))
		user_agent='Mozilla/5.0 (X11; U; Linux x86_64; ru; rv:1.9.0.4) Gecko/2008120916 Gentoo Firefox/3.0.4'
		req = urllib2.Request(url)
		req.add_header('User-Agent',user_agent)
		body = urllib2.urlopen(req).read()
		body = html_encode(body)
		if body.count('<table id=pcodephones cellspacing=0>\n  <tr><th width'): msg = u'По вашему запросу ничего не найдено.'
		else:
			body = body.split('<table id=pcodephones cellspacing=0>')[1].split('</table>')[0].split('</tr>')[1:]
			if body != [u'\n ']:
				msg = u'Найдено:'
				for tmp in body[:csize]:
					tmp2 = '\n'+replacer(tmp).replace('\n',', ').replace(';',', ')
					tmp3 = tmp2[tmp2.find(u' тариф'):tmp2.find(u',',tmp2.find(u' тариф'))+1]
					msg += tmp2.replace(tmp3,'')
			else: msg = u'بحثك لم يتم'
	else: msg = u'عن ماذا نبحث؟'
	reply(type, source, msg)
	
register_command_handler(telcode, 'كود-رقم', ['все','all','инфо'], 10, 'Определение кода города', 'телкод <слово>', ['телкод анапа'])
