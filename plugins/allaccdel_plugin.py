#  STORM BOT BY ALI
def handler_delacc(type, source, parameters):
   GLOBACCESS2 = 'dynamic/globaccess.cfg'
   reply(type,source,u'الرجاء الانتظار....ريثما يتم تصفير ملف الاكسز 8-) ')
   if check_file(file='globaccess.cfg'):
     jiddel = eval(read_file(GLOBACCESS2))
     for jid in jiddel:
             del jid
             write_file(GLOBACCESS2, u'{}')
             egproo = [u'تم مسح ايميل']
             eg = jid
             tarek = str(random.choice(egproo))
             egprogrammer = str(type(eg))
             repp = (tarek)+(egprogrammer)
             reply(type,source, repp)
     else:
             reply(type,source,u'لا يوجد ايميلات بقائمة الأكسز')
             print 'Error: unable to create chatrooms list file!'
             reply(type,source,u'تم مسح جميع الايميلات من قائمة الاكسز 8-) ')
register_command_handler(handler_delacc, 'مسح-كل-الاكسز', ['الكل'], 0, 'مسح جميع الايميلات التي تم اعطائها اكسز 8-) ', '', [''])
