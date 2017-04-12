#===istalismanplugin===
# -*- coding: utf-8 -*-

#  STORM BOT BY ALI

def handler_salam_1(type, source, parameters):
	replies = [u'هايات ياغالي نورت @}->--', u'قهلا بالحبيب قهلا @}->--', u' @}->-- هايات ياورد']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_2(type, source, parameters):
	replies = [u'الله معك حبيبنا نورت رومك @}->--', u'لاتطول ياغالي ناطرينك ها :-P', u'بايات نورت @}->--']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_3(type, source, parameters):
	replies = [u'أحلى كأسة مته لعيونك معلمي :-D', u'تفضل من تحت أيدي كأسة هل المته  :-P', u'وك مته عيني ربك أي تكرم :-(']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)		

def handler_salam_4(type, source, parameters):
	replies = [u'كأس ربك وكأس الأسد تفضل :beer: ', u'لعيونك كأس للصبح :beer: ', u'كأسك ع الصافي :beer: ']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_5(type, source, parameters):
	replies = [u'تمام أنت كيفك ياغالي :nose:', u'أناتمام اذا انت تمام @}->--', u'وك تمام وهنت كيفك 8-D']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_6(type, source, parameters):
	replies = [u'نايس ياغالي  :nose:', u'نايساتك ياغالي  @}->--', u'وك دخيل البك منك انا نايسك 8-D']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_7(type, source, parameters):
	replies = [u'صباحك عسل ياعسل  :nose:', u'صباح الورد ياورد أنت  @}->--', u'ودخيل هل الصباح منك 8-D']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_8(type, source, parameters):
	replies = [u'مساك فل يافل  :nose:', u'مسا الورد ياورد أنت  @}->--', u'ودخيل هل مساك ياغالي 8-D']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_9(type, source, parameters):
	replies = [u' وعليكم☼السـلام☼ورحــمہ☼اللـہ☼وبرکـاتـہ ', u' وعليكم☼السـلام☼ورحــمہ☼اللـہ☼وبرکـاتـہ', u'وعليكم☼السـلام☼ورحــمہ☼اللـہ☼وبرکـاتـہ']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_10(type, source, parameters):
	replies = [u'أضربلك صحن أندومي لتمك :-D', u'وأحلى برميل أندومي خليك تشبع وتحل عني :-D ', u'روح لعند بيتك أهلك شو عنا مطعم:-D ']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_11(type, source, parameters):
	replies = [u'اللهمَّ لا تحرمني وأنا أدعوك… ولا تخيبني وأنا أرجوك	 ', u'الله أكبر ليس كمثله شيء في الأرض ولا في السماء وهو السميع البصير', u'اللهم احسن عاقبتنا في الأمور كلها ، وأجرنا من خزي الدنيا وعذاب الآخرة'u'اللهمَّ إني أسألك يا فارج الهم، ويا كاشف الغم، يا مجيب دعوة المضطرين، يا رحمن الدنيا، يا رحيم الآخرة، أرحمني برحمتك'u'اللهمَّ إني أسألكَ الصبر عند القضاء، ومنازل الشهداء، وعيش السعداء، والنصر على الأعداء، ومرافقة الأنبياء، يا رب العالمين'u'اللهم إني أسألك عيش السعداء وموت الشهداء والحشر مع الأتقياء ومرافقة الأنبياء'u'اللهم إني أعوذ بك من زوال نعمتك ومن فجاءة نقمتك ومن جميع سخطك'u'ربنا اصرف عنا عذاب جهنم ا ن عذابها كان غراما انها ساءت'u'اللهم يا من دَلَعَ لسان الصباح بِنُطْقِ تبَلُّجِهِ، وسَرَّح قِطع الليل المظلم بغياهب تلجلُجه'u'اللهم إني أعوذ بك من الهم والخزن، والعجز والكسل والبخل والجبن، وضلع الدين وغلبة الرجال']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_12(type, source, parameters):
	replies = [u'وك قدي بدك انا جاهزلعيونك	 ', u'وك قدي بدك انا جاهزلعيونك	', u'وك قدي بدك انا جاهزلعيونك	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_13(type, source, parameters):
	replies = [u':-Dروح ع السوق وأشتري تياب', u':-Dروح ع السوق وأشتري تياب', u':-Dروح ع السوق وأشتري تياب	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_14(type, source, parameters):
	replies = [u' أن تضيء شمعة صغيرة خير لك من أن تنفق عمرك تلعن الظلام	 ', u' لا يحزنك إنك فشلت مادمت تحاول الوقوف على قدميك من جديد', u'الألقاب ليست سوى وسام للحمقى والرجال العظام ليسوا بحاجة لغير اسمهم'u' لو امتنع الناس عن التحدث عن أنفسهم وتناوُل الغير بالسوء لأصيب الغالبية الكبرى من البشر بالبكم'u'ليس الفقير من ملك القليل .. إنما الفقير من طلب الكثير'u'من أذنب وهو يضحك دخل النار وهو يبكي'u'الزواج يأتى بدون سابق إنذار كما تقع نقطة من الحبر الأسود على ملابس الإنسان'u'قليل من العلم مع العمل به .. أنفع من كثير من العلم مع قلة العمل به'u' تكلم وأنت غاضب .. فستقول اعظم حديث تندم عليه طوال حياتك']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_15(type, source, parameters):
	replies = [u':-( وأنا بدي صندويشة فلافل ', u':-( وأنا بدي صندويشة فلافل', u':-( وأنا بدي صندويشة فلافل	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_16(type, source, parameters):
	replies = [u'أحلى سيكارة للمعلم', u'شونوع دخانك :-P', u'ممنوع التدخين بالروم :-P	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_17(type, source, parameters):
	replies = [u'حل عني شو بدك ها', u'نعم شو بدك :-P', u'شو مافي حدا غير البوت نعم شو بدك:-P	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_18(type, source, parameters):
	replies = [u'قديم عندي بطح سرعتوا 450 ياماها', u'قديم عندي بطح سرعتوا 450 ياماها :-P', u'قديم عندي بطح سرعتوا 450 ياماها:-P	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_19(type, source, parameters):
	replies = [u'ضل ما شبعنا منك 8(', u'ضل ما شبعنا منك 8(', u'ضل ما شبعنا منك 8(	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_20(type, source, parameters):
	replies = [u'ماشي انا طابات ملونة وانت سادة :JOKINGLY', u'ماشي انا طابات ملونة وانت سادة :JOKINGLY', u'ماشي انا طابات ملونة وانت سادة :JOKINGLY	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_21(type, source, parameters):
	replies = [u'وانا كمان @}->-- /حبيبتي', u'وانا كمان @}->-- /حبيبتي', u'وانا كمان @}->-- /حبيبتي	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_22(type, source, parameters):
	replies = [u'ريال مدريد', u'real madrid', u'real madrid	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_23(type, source, parameters):
	replies = [u' لا تقل كلمتك إلا امام من يحترمها', u' لا تعطي الحب إلا لمن يستحق', u'لا تذرف الدموع إلا عندما تحاول الفشل	', u'من يحارب يحارب كالأسد ولا يصمت كالحمل', u'- لا تخفض رأسك و تخجل من خيانة الأخر', u'- تذكر بأنك فعلت كل ما بيدك فرط فيك الأخرون', u'لا تصدق اي شئ يقال عنه إلا عندما تراه', u'- إذا غلط مرة وسامحته على طول تأكد انك أعطيته فرصة الغلط مئة مرة']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_24(type, source, parameters):
	replies = [u'أحسست بشعور غريب ؟؟ وفجأة نزلت دمعة انقبض قلبي و اهتز فؤادي عندما استوعبت أنه كان أخر لقاء التف الكون من حولي ومرت حياتي كلها كفيلم قصير أمام مقلتي فبدأت الدموع تنهمر فأخذت أصارع حرقة قلبي رحلت .......رحلت و تركتني تركتني سجينة الماضي تركتني حبيسة أفكاري أصارع الأمرين أملت أن تبقى معي دعوت من الرب أن يتركك معي لتشاركني أفراحي و أحزاني كما في السابق لأرتمي في حضنك عندما أحس بالخوف لأنام على صدرك اذا تعبت لأقبل يديك صباحا و مساءا شوقا وليس ذلا لأركع لك حبا و احتراما وليس كفرا فأنت حبيبي و مهجة قلبي فأنت نور مقلتي اللتان أبكاهما فراقك أحببتك لأنك أسمى شئ وهبه الخالق لي أتذكرك رغم أنني لا أنساك ولن أنساك أراك في صحوتي ومنامي فصورتك مطبوعة في مخيلتي وابتسامتك تساوي حياتي أحبك....', u'من ثراء لغتنا العربية الجميلة أن مفرداتها تستقل بمعاني خاصة بها،لا يناسب وضع غيرها محلها والعربي الفصيح  والمتكلم البليغ يراعي كل حالة وكل معنى ويعطيه حقه ولفظه وهذه بعض الأمثلة على مفردات مترادفة ؛ لكنها في الحقيقة ذات فروق دقيقة..', u'أَخَيَّ لا يُغريكّ سربالُ الـرَّخاْ وسرابُ دنيا بالغرور تفخّـخا فلسوف تتركـُها لتُسكن َ فرسخا فاصرخ معاذ الله من درب مشين ** إني أخافُ الله ربَّ العالمين   فإذا سعت فتنُ الحياةِ تبـشُّ لكْ وتبرّجت في خلوة الرُّقباء ِ لكْ وأتت تدندنُ في المكان ِ بهيت لكْ فاصرخ معاذ الله من درب مشين ** إني أخافُ الله ربَّ العالمين إنْ ضجّت القنواتُ في صدرِ البيوتْ 	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_25(type, source, parameters):
	replies = [u'واحد شاف جاره قال له ليك وحياتك تبقى انزل الستارة بس تكون مع مرتك مبارح شفتكم عم بتبوسو بعض.جاوب الجار  هيدا الكلام كله كذب ومش صحيح انا مبارح كان عندي شغل بالليل وما نمت بالبيت ', u'مرة سألوا واحد أحول شو أمنيتك بالحياة جاوبن شوف واحد ماشي لوحدو عالطريق', u'مرة واحد راكب على حمار قام شاف وحدة حلوة قام قلة أول مرة بشوف القمر على الارض قامت قالتلوا وأنا اول مرة بشوف حمار طابقين	'u'ضل ما شبعنا منك 8(', u'*مرة واحد راح ينشر الغسيل أخذ معاه منشار', u'خاروفين واقفين حد بعض قلو الاول بااااااااء قلو التاني عمرك اطول من عمري كنت لح قولها	'u'واحد ندل قعد لمده سنه يتحايل على حبيبته مشان تخرج معاه', u'وحدة جوزها حمصي نايمين بالليل حست بحركة بالصالون فيقت جوزها قالتلو قوم يمكن في حرامي بالصالون قلها قومي انتي يمكن تطلع حرامية', u'قال ثبت عيد الفطر بحمص بعد رؤية هلال شوال على سيارة الاسعاف	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_26(type, source, parameters):
	replies = [u'كيف عنك أتوب والقلب حضرتك تملكه .. بتوب عن كل الذنوب وذنب  حبك حشى ما اتركه', u'دلوني على قلب .. يحب ما يخون .. وعلى عين .. تشوف واحد .. مب مليون ', u'ممنوع التدخين بالروم :-P	'u'الثلج هدية الشتاء .. والشمس هدية الصيف .. والزهور هدية الربيع .. وأنت هدية العمر ', u'شونوع دخانك :-P', u'ممنوع التدخين بالروم :-P	'u'أحلى سيكارة للمعلم', u'شونوع دخانك :-P', u'ما أصعب أن تبكي بلا .. " دموع" .. وما أصعـــــب أن تذهب بلا .. " رجوع " .. وما اصعب أن تشعر .. " بالضيق" وكأن المكان من حولك .. "يضــــــيق " ..	'u'قطعني حتة حتة وأرميني لأي قطة ... أنا كنت بأحب واحد دلوقتي بأحب ستة ..', u'الرسالة دي ليك .... على الله يطمر فيك ... وتجيب الفلوس اللي عليك يامعفن', u'حبيبي ياللي أحبه قلتله أتنيل ... جربتك في الحب طلعت أكبر عيل 	'u'قالوا القمر .. قلت عالي .. قالوا الذهب .. قلت غالي .. قالوا حبيبي ..قلت دوم في بالي ', u'الاسم : مجنونك .. العمر : أنت عمري .. الهواية : أهواك .. النهاية : أحبك', u'معلى ذوقي اخترت لك اسم .. أول حرف (ر) .. الثاني (و) .. الثالث  (ح) .. الرابع (ي) .. (روحي)	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_27(type, source, parameters):
	replies = [u'تفضل أحلى كأسة شاي لعيونك', u'تفضل شي ريتو صحة وهنا', u'أنشالله صحة معلم	']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_28(type, source, parameters):
	replies = [u'حب--نكتة--ادب--نصيحة--شواسم فريقك--بوت بحبك--بدي اطلع--فلافل--دخان--دعاء--السلام--مته--وسكي--تصميم--']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

def handler_salam_29(type, source, parameters):
	replies = [u'{мαғια•тєaм™ 2ό13-2ό14 ©} By M3do@xmpp.ru :-)']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)			
		
def handler_pamit(type, source, parameters):
	replies = [u'نورت الله معك @}->-- ', u'بايات نورت @}->--', u'بايات نورت @}->-- ']
	balas = random.choice(replies)
	if type == 'public':
		if source[1]:
			reply(type, source, balas)
	elif type == 'private':
		reply(type, source, balas)

register_command_handler(handler_pamit, 'asssssssssssss', ['new'], 0, '', '', [''])
register_command_handler(handler_pamit, 'باي', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_1, 'هااي', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_1, 'هلو', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_1, 'هاي', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_1, 'هاي', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_1, 'هاي', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_2, 'بررب', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_2, 'برب', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_3, 'متة', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_3, 'مته', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_4, 'وسكي', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_4, 'كأس', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_4, 'كاس', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_5, 'كيفكن', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_5, 'كيفك', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_6, 'بااك', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_6, 'باك', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_7, 'صباحكن', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_7, 'صباحو', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_8, 'مساو', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_8, 'مساء', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_8, 'مسا', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_9, 'س ع', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_9, 'سلام', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_9, 'السلام', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_4, 'بيرة', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_4, 'فلاش', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_4, 'عرق', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_5, 'ك', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_7, 'ص خ', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_10, 'اندومي', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_10, 'أندومي', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_5, 'ك', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_8, 'مسالخير', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_11, 'دعاء', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_12, 'مصاري', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_13, 'تياب', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_14, 'حكم', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_15, 'فلافل', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_16, 'دخان', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_17, 'يابوت', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_18, 'بطح', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_19, 'بدي اطلع', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_20, 'بلياردو', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_21, 'بوت بحبك', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_22, 'شواسم فريقك', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_23, 'نصيحة', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_24, 'ادب', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_25, 'نكتة', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_25, 'نكته', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_26, 'حب', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_27, 'شاي', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_28, 'تكلم', ['new'], 0, '', '', [''])
register_command_handler(handler_salam_29, 'تصميم', ['new'], 0, '', '', [''])
