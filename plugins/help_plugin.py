#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  help_plugin.py

#  STORM BOT BY ALI

def handler_help_help(type, source, parameters):
	ctglist = []
	if parameters and COMMANDS.has_key(parameters.strip()):
		rep = COMMANDS[parameters.strip()]['desc'].decode("utf-8") + u'\nCategories: '
		for cat in COMMANDS[parameters.strip()]['category']:
			ctglist.append(cat)
		rep += ', '.join(ctglist).decode('utf-8')+u'\nUse: ' + COMMANDS[parameters.strip()]['syntax'].decode("utf-8") + u'\nExample:'
		for example in COMMANDS[parameters]['examples']:
			rep += u'\n  >>  ' + example.decode("utf-8")
		rep += u'\nمرحله الاكسز المطلوبه ' + str(COMMANDS[parameters.strip()]['access'])
		if parameters.strip() in COMMOFF[source[1]]:
			rep += u'\nتم الغاء تفعيل هذا الامر فى هذه الروم'
		else:
			pass
	else:
		rep = u'مـرحـبـا :-)\nانا البوت العربي الجديد\nلمعرفة اوامري اكتب  "commands all" \nمطور بواسطة\nALI .B .OTH'
	reply(type, source, rep)

def handler_help_commands(type, source, parameters):
	date=time.strftime('%a, %d %b %Y', time.gmtime()).decode('utf-8')
	groupchat=source[1]
	if parameters:
		rep,dsbl = [],[]
		total = 0
		param=parameters.encode("utf-8")
		catcom=set([((param in COMMANDS[x]['category']) and x) or None for x in COMMANDS]) - set([None])
		if not catcom:
			reply(type,source,u'هل هي موجوده؟ :-O')
			return
		for cat in catcom:
			if has_access(source, COMMANDS[cat]['access'],groupchat):
				if source[1] in COMMOFF:
					if cat in COMMOFF[source[1]]:
						dsbl.append(cat)
					else:
						rep.append(cat)
						total = total + 1
				else:
					rep.append(cat)
					total = total + 1					
		if rep:
			if type == 'public':
				reply(type,source,u'انظر بالخاص ;-)')
			rep.sort()
			answ=u'اوامري كالتالي ;-) <'+parameters+u'> فى تاريخ '+date+u':\n\n' + u' | '.join(rep) +u' - ('+str(total)+u' )'
			if dsbl:
				dsbl.sort()
				answ+=u'\n\nتم الغاء هذه الاوامر فى هذه الروم:\n\n'+', '.join(dsbl)
			reply('private', source,answ)
		else:
			reply(type,source,u'انت بتحلم ]:->')
	else:
		cats = set()
		for x in [COMMANDS[x]['category'] for x in COMMANDS]:
			cats = cats | set(x)
		cats = ', '.join(cats).decode('utf-8')
		if type == 'public':
			reply(type,source,u'انظر بالخاص ;-)')
		reply('private', source, u'اوامري كالتالي ;-) '+date+u'\n'+ cats+u'\n\n لمعرفه الاوامر كلها :?commands all"')


register_command_handler(handler_help_help, 'مساعدة', ['help','info','all'], 0, 'Show detail information about a certain command.', 'help [command]', ['help', 'help ping'])
register_command_handler(handler_help_commands, 'commands', ['help','info','all'], 0, 'Shows the list of all of categories of commands. At the query of category shows the list of commands being in it.', 'commands [category]', ['commands','commands all'])
