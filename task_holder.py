from numpy import random

from send_message import send_message
from login import login

# from fancy_text import fancy as fan
# import mishkal.tashkeel as tashkeel

# vocalizer = tashkeel.TashkeelClass()
# def tashkeel(text):
#     return vocalizer.tashkeel(text)

# TASK: ZAKHRAFAH - start

# zakhrafah fonts
fonts = [
    '𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘 ',
    '𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ1234567890 ',
    '𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅1234567890 ',
    '𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢 ',
    '𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩1234567890 ',
    'ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ１２３４５６７８９０ ',
    '🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉1234567890 ',
    '🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉1234567890 ',
    'ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ①②③④⑤⑥⑦⑧⑨⓪ ',
    'ค๒ς๔єŦﻮђเןкɭ๓ภ๏קợгรՇยשฬאץչค๒ς๔єŦﻮђเןкɭ๓ภ๏קợгรՇยשฬאץչ1234567890 ',
    'ᏗᏰፈᎴᏋᎦᎶᏂᎥᏠᏦᏝᎷᏁᎧᎮᎤᏒᏕᏖᏬᏉᏇጀᎩፚᏗᏰፈᎴᏋᎦᎶᏂᎥᏠᏦᏝᎷᏁᎧᎮᎤᏒᏕᏖᏬᏉᏇጀᎩፚ1234567890 ',
    'ΛBᄃDΣFGΉIJKᄂMПӨPQЯƧƬЦVЩXYZΛBᄃDΣFGΉIJKᄂMПӨPQЯƧƬЦVЩXYZ1234567890 ',
    '₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩ӾɎⱫ₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩ӾɎⱫ1234567890 ',
    'ﾑ乃ᄃり乇ｷムんﾉﾌズﾚﾶ刀のｱゐ尺丂ｲひ√Wﾒﾘ乙ﾑ乃ᄃり乇ｷムんﾉﾌズﾚﾶ刀のｱゐ尺丂ｲひ√Wﾒﾘ乙1234567890 ',
    '卂乃匚ᗪ乇千Ꮆ卄丨ﾌҜㄥ爪几ㄖ卩Ɋ尺丂ㄒㄩᐯ山乂ㄚ乙卂乃匚ᗪ乇千Ꮆ卄丨ﾌҜㄥ爪几ㄖ卩Ɋ尺丂ㄒㄩᐯ山乂ㄚ乙1234567890 ',
    'ąҍçժҽƒցհìʝҟӀʍղօքզɾʂէմѵա×վՀȺβ↻ᎠƐƑƓǶįلҠꝈⱮហටφҨའϚͲԱỼచჯӋɀ𝟙ϩӠ५ƼϬ7𝟠९⊘ ',
    '𝒶𝒷¢𝕕єⓕᎶʰίנＫＬ𝓜η𝓞ƤɊ𝐫𝐬𝓉𝕌𝕍𝕎ⓧⓨＺⒶᗷc𝕕ᗴᶠᎶнιנＫℓ𝓂𝐧ｏρ𝔮ŕѕт𝐔νｗx𝔂z１➁❸４➄➅➆➇９０ ',
    'ᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭YᘔᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭Yᘔ1234567890 ',
    ['a░', 'b░', 'c░', 'd░', 'e░', 'f░', 'g░', 'h░', 'i░', 'j░', 'k░', 'l░', 'm░', 'n░', 'o░', 'p░', 'q░', 'r░', 's░', 't░', 'u░', 'v░', 'w░', 'x░', 'y░', 'z░', 'A░', 'B░', 'C░', 'D░', 'E░', 'F░', 'G░', 'H░', 'I░', 'J░', 'K░', 'L░', 'M░', 'N░', 'O░', 'P░', 'Q░', 'R░', 'S░', 'T░', 'U░', 'V░', 'W░', 'X░', 'Y░', 'Z░','1░', '2░', '3░', '4░', '5░', '6░', '7░', '8░', '9░', '0░', ' ']
]

# english letters
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "

# zakhrafah function
def fancy(text: str):
    if len(text) < 15:
        words = ""
        text = text.strip()
        try:
            if text.strip() != "":
                for font in fonts:
                    word = ""
                    for letter in text:
                        letter_index = letters.index(letter)
                        try: word += font[letter_index]
                        except: word += letter
                    words += f"{word}  "
                return words
            else: return "أدخل نصاً لزخرفته"
        except: return text
    else: return "النص طويل جداً!"

# TASK: ZAKHRAFAH - end

# TASK: INSULT - start

insulted_messages = ["😂", "😂😂", "😂😂😂", "🤣", "🤣🤣", "🤣🤣🤣", "😹", "😹😹", "😹😹😹"]
insulting_responses = [
    "لا أستطيع أن أبتسم مثلك، ربما يجب عليك تعلم الفكاهة الحقيقية. 😒",
    "هل هذا كان مضحكًا بالنسبة لك؟ يبدو أن معاييرك منخفضة جدًا. 😒",
    "أعتقد أنني أضحك أكثر منك بكثير دون الحاجة إلى استخدام الإيموجي. 😒",
    "يبدو أن فكرتك الرائعة للفكاهة هي وضع إيموجي ضاحك بدلًا من استخدام عقلك. 😒",
    "أعتقد أنك تحاول جاهدًا أن تكون مضحكًا، لكنك بالتأكيد لست كذلك. 😒",
    "لقد رأيت الكثير من النكات الأفضل من هذا، هل هذا كل ما عندك؟ 😒",
    "أعتقد أنني بحاجة للبحث عن مقياس جديد للفكاهة بعد رؤية ما قمت به. 😒",
    "من المدهش كيف يمكنك أن تجد مثل هذه النكت السطحية مضحكة. 😒",
    "هذا مستوى جديد من الفكاهة السيئة، لقد خيبت آمالي. 😒",
    "هل تعتقد أن وضع إيموجي ضاحك يجعلك مضحكًا؟ لا يا صديقي، لا يعمل هكذا. 😒",
    "أعتقد أن هذا النوع من النكات يناسب أذواقك المتواضعة. 😒",
    "هذا كان أقرب إلى الزهق من أن يكون مضحكًا. حاول مرة أخرى. 😒",
    "أنا آسف، لم أستطع أن أفهم كيف يمكن أن تجد ذلك مضحكًا. 😒",
    "أعتقد أنك بحاجة لبعض الدروس في الفكاهة قبل المحاولة مرة أخرى. 😒",
    "إذا كنت تعتقد أن هذا مضحك، فأنا أعتقد أنك تحتاج إلى تطوير gevoel للفكاهة. 😒",
]

# TASK: INSULT - end

# TASK: ANSWER - start

calling_phrases = ["بوت", "bot", "روبوت", "robot"]
act_calling_phrases = ["mickey", "ميكي"]




client = login()

toggle = 0

def task_holder(data):
    global toggle
    community_id = data.json.get("ndcId")
    chat_id = data.json.get("chatMessage", {}).get("threadId")
    message_id = data.json.get("chatMessage", {}).get("messageId")
    nickname = data.json.get("chatMessage", {}).get("author", {}).get("nickname")
    user_id = data.json.get("chatMessage", {}).get("author", {}).get("uid")
    message_content: str = data.json.get("chatMessage", {}).get("content")
    content = message_content.replace(message_content.split(":")[0], "")[1:]
    
    # ZAKHRAFAH
    if message_content.startswith("زخرفة:"): 
        if toggle == 1:
            send_message(community_id, chat_id, fancy(content), replyTo=message_id)
            toggle = 0
        else: toggle = 1
    

    # INSULTING
    random_number = random.randint(0, len(insulting_responses)-1)
    if message_content in insulted_messages:
        if toggle == 1:
            send_message(community_id, chat_id, insulting_responses[random_number], replyTo=message_id)
            toggle = 0
        else: toggle = 1

    # Calling
    if message_content.lower() in calling_phrases:
        if toggle == 1:
            send_message(community_id, chat_id, 'نادني باسم "ميكي"' , replyTo=message_id)
            toggle = 0
        else: toggle = 1
    elif message_content.lower() in act_calling_phrases:
        if toggle == 1:
            send_message(community_id, chat_id, 'تعم؟' , replyTo=message_id)
            toggle = 0
        else: toggle = 1


client.launch()