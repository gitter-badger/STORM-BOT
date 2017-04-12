#===istalismanplugin===
# -*- coding: utf-8 -*-

#  talisman plugin
#  net_plugin.py

#  STORM BOT BY ALI

import os, urllib
from urlparse import urlsplit

def download_file(url, file):
	resp = urllib.urlretrieve(url, file)
	
	if resp and len(resp) == 2:
		return resp[1].get('Content-Length')
	else:
		return 0

def si_gf_request(frm,fjid,sid,name,size,site):
	iq = xmpp.Protocol(name = 'iq', to = fjid,
		typ = 'set')
	ID = 'si'+str(random.randrange(1000, 9999))
	iq.setID(ID)
	si = iq.setTag('si')
	si.setNamespace(xmpp.NS_SI)
	si.setAttr('profile', xmpp.NS_FILE)
	si.setAttr('id', sid)
	file_tag = si.setTag('file')
	file_tag.setNamespace(xmpp.NS_FILE)
	file_tag.setAttr('name', name)
	file_tag.setAttr('size', size)
	desc = file_tag.setTag('desc')
	desc.setData(u'File from "%s".' % (site))
	file_tag.setTag('range')
	feature = si.setTag('feature')
	feature.setNamespace(xmpp.NS_FEATURE)
	_feature = xmpp.DataForm(typ='form')
	feature.addChild(node=_feature)
	field = _feature.setField('stream-method')
	field.setAttr('type', 'list-single')
	field.addOption(xmpp.NS_IBB)
	field.addOption('jabber:iq:oob')
	return iq

def handler_get_file(type, source, parameters):
	groupchat=source[1]
	nick = source[2]

	if not GROUPCHATS.has_key(groupchat):
		reply(type, source, u'ويمكن استخدام هذا الأمر فقط في المؤتمر!')
		return
	
	if parameters:
		url = parameters.strip()
		
		to = ''
		
		if GROUPCHATS[groupchat].has_key(nick):
			to = GROUPCHATS[groupchat][nick]['jid']
		
		if not to:
			reply(type, source, u'خطأ داخلي، لا يمكن تنفيذ العملية!')
			return
		
		sid = 'file'+str(random.randrange(10000000, 99999999))
		name = sid
		path = 'dynamic/'+name
		site = 'unknown'
		
		spurl = urlsplit(url)
		
		if spurl[2] != '':
			spname = spurl[2].split('/')
			name = spname[-1]
				
		if spurl[1] != '':
			site = spurl[1]
			
			if spurl[0] != '':
				site = spurl[0]+'://'+site		
		
		dlsize = download_file(url, path)
		
		if dlsize == 0:
			reply(type, source, u'غير قادر على الحصول على الملف!')

			if os.path.exists(path):
				os.remove(path)
			return
		
		try:
			fp = open(path,'rb')
		except:
			reply(type, source, u'غير قادر على الحصول على الملف!')
			
			if os.path.exists(path):
				os.remove(path)
			return
		
		frm = JID+'/'+RESOURCE
		
		sireq = si_gf_request(frm,to,sid,name,dlsize,site)
		JCON.SendAndCallForResponse(sireq, handler_get_file_answ, args={'type':type,'source':source,'sid':sid,'to':to,'fp':fp})
	else:
		reply(type, source, u'بناء الجملة غير صالحة!')
		
def handler_get_file_answ(coze,resp,type,source,sid,to,fp):
	rtype = resp.getType()
	
	if rtype == 'result':
		JCON.IBB.OpenStream(sid,to,fp,1024)
		name = fp.name
		os.remove(name)
	else:
		name = fp.name
		fp.close()
		os.remove(name)
		reply(type, source, u'بناء الجملة غير صالحة!')

register_command_handler(handler_get_file, '.الحصول-على-ملف', ['info','wtf','all','*'], 11, 'Downloaded a file from the network via Jabber.', '.get_file <URL>', ['.get_file http://files.com/file.ext'])
