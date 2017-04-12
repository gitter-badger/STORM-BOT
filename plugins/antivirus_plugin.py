#===istalismanplugin===
# -*- coding: utf-8 -*-
#  STORM BOT BY ALI
# FAKE SCAN

virus = [u'صافي Worm.Win32.Mytob.bd', u'Worm.ExploreZip', u'Trojan.Generic', u'097/Crown.B', u'I-Worm.Mydoom.q', u'Trojan-Dropper.Win32.Microjoin.l', u'Worm.Win32.Feebs.gen_07', u'Win32.HLLM.Graz.00', u'VBS.Redlof.a', u'Joke.Flipped', u'Program.HiddenAdmin.origin', u'I-Worm.Tanatos.a', u'unknown', u'РІРёСЂСѓСЃРѕРІ РЅРµ РЅР°С€РµР»']
act = [u'[cannot clear]', u'[cleared]',u'[removed]',u'[تحت carantine]']
lic = [u'[blacklist]', u'[whitelist]']

def handler_test_virus(type, source, parameters):

        reply(type,source,u'جاري فحص الروم من الفيروسات...')

        time.sleep(random.randrange(0, 6))

        reply(type,source,u'انتظر قليلا من بعد أذنك ...')

        time.sleep(random.randrange(0, 30))

        ocupants = []

        for i in GROUPCHATS[source[1]]:

                if GROUPCHATS[source[1]][i]['ishere'] == 1:

                        ocupants.append(i)

        if len(ocupants) > 10:

                count = random.randrange(0, 10)

        else:

                count = random.randrange(0, len(ocupants))

        if count == 0:

                res= u'الروم بدون فيروسات'

        else:

                res = u' تحذير : اكتشاف '+str(count)+u' فيروسات:'

                for vir in range(0, count):
                    oc=random.choice(ocupants)
                    vi=random.choice(virus)
                    ac=random.choice(act)
                    if ac == act[2]:
                        order_kick(source[1],oc,u'ستصبح نظيفا من الفيروسات بعد اعاده دخولك الروم')
                    if ac == act[3]:
                        order_visitor(source[1],oc,u'ستصبح نظيفا من الفيروسات بعد اعاده دخولك الروم')
                    res += '\n'+oc+' ('+vi+') '+ac

        reply(type,source, res)
def handler_antivirus_update(type, source, parameters):
        lc=random.choice(lic)
        if lc == lic[1]:
                reply(type,source,u'جارى الاتصال بمركز البوت .....')
                time.sleep(random.randrange(0, 3))
                reply(type,source,u'تم تحديث سكان البوت بنجاح')
                reply(type,source,u'يمكنك الان البحث عن الفيروسات')
        if lc == lic[0]:
                reply(type,source,u'جارى الاتصال بمركز البوت .....')
                time.sleep(random.randrange(0, 3))
                reply(type,source,u'لقد نفذ رصيد تحديث البوت يرجى الاعاده مره اخرى')

register_command_handler(handler_test_virus, 'سكان', ['all'], 30, 'clean room for viruses‚', 'scan', ['scan'])
register_command_handler(handler_antivirus_update, 'تحديث-سكان', ['all'], 30, 'update for bot antivirus‚', 'av_update', ['av_update'])

