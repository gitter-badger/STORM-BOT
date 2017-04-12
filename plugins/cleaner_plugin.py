#===istalismanplugin===
# -*- coding: utf-8 -*-

#  STORM BOT BY ALI

def handler_cleaner(type, source, parameters):
    groupchat=source[1]
    st = [u'dnd']
    if GROUPCHATS.has_key(groupchat):
      reply(type, source, u'جـاري تنظيف الـروم مـن الـكـلـمـات :-)')
      cleans=xmpp.protocol.Presence(source[1]+'/'+get_bot_nick(source[1]))
      cleans.setShow(random.choice(st))
      cleans.setStatus(u'لآن تنظيف الروم')
      JCON.send(cleans)
      for x in range(1, 20):
        time.sleep(1.5)
        msg(groupchat, u'')
      reply(type, source, u'تـم الـتـنـظـف بـنـجـاح :-)')
      done=xmpp.protocol.Presence(source[1]+'/'+get_bot_nick(source[1]))
      done.setShow('dnd')
      done.setStatus(u'STORM BOT BY ALI')
      JCON.send(done)
    else:
      reply(type, source, u'هذا الأمر ممكن فقط في الرومات')
    
register_command_handler(handler_cleaner, 'نظف', ['muc','admin','all'], 20, 'Invisible cleaning of conference.', 'clean', ['clean'])
