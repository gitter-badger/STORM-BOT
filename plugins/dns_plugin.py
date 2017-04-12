#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  dns_plugin.py

#  STORM BOT BY ALI

import socket

def dns_query(query):
	try:
		int(query[-1])
	except ValueError:
		try:
			(hostname, aliaslist, ipaddrlist) = socket.gethostbyname_ex(query)
			return u', '.join(ipaddrlist)
		except socket.gaierror:
			return u'لم اجدها'
	else:
		try:
			(hostname, aliaslist, ipaddrlist) = socket.gethostbyaddr(query)
		except socket.herror:
			return u'لم اجدها'
		return hostname + ' ' + string.join(aliaslist) + ' ' + string.join(aliaslist)

def handler_dns_dns(type, source, parameters):
	if parameters.strip():
		result = dns_query(parameters)
		reply(type, source, result)
	else:
		reply(type, source, u'عن شو عم تحكي أنت ؟')

register_command_handler(handler_dns_dns, 'كود-سرفر', ['info','all'], 10, 'Shows an answer from DNS for a certain host or IP of address.', 'dns <host/IP>', ['dns server.tld', 'dns 127.0.0.1'])
