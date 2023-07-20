from numpy import random

from send_message import send_message

# List of welcome messages
goodbye_messages = [
    "[BC] وداعًا! نشكرك على تواجدك معنا، أتمنى لك حياة سعيدة.",
    "[BC] إلى اللقاء! سنفتقدك، تمتع ببقية يومك.",
    "[BC] أراك لاحقًا! حظًا سعيدًا في مغامراتك القادمة.",
    "[BC] وداعًا وأتمنى لك الأفضل! استمتع برحلتك.",
    "[BC] إلى اللقاء! نأمل أن تعود قريبًا، فرصة سعيدة لك.",
    "[BC] أراك قريبًا! نشكرك على مساهمتك، استمتع بوقتك.",
    "[BC] وداعًا وحظًا سعيدًا! كن دائمًا مبتسمًا وسعيدًا.",
    "[BC] إلى اللقاء ونأمل أن تعود قريبًا! ابقَ بخير.",
    "[BC] أراك في وقت لاحق! استمتع بباقي يومك.",
    "[BC] وداعًا! كن دائمًا موجودًا ومشرقًا كالشمس.",
    "[BC] إلى اللقاء وأتمنى لك أوقاتًا سعيدة! استمتع بحياتك.",
    "[BC] أراك قريبًا! شكرًا لمشاركتك وتفاعلك، حظًا سعيدًا.",
    "[BC] وداعًا وأتمنى لك كل التوفيق! ابقَ سعيدًا ومبتسمًا.",
    "[BC] إلى اللقاء! تمنياتنا لك بيوم رائع وسعيد.",
    "[BC] أراك لاحقًا! نشكرك على وقتك ومساهماتك.",
    "[BC] وداعًا! كن مستمتعًا بالحياة وابقَ في أمان الله.",
]



toggle = 0

def on_group_member_leave(data):
    try:
        global toggle
        if toggle == 1:
            community_id = data.json.get("ndcId")
            chat_id = data.json.get("chatMessage", {}).get("threadId")
            message_id = data.json.get("chatMessage", {}).get("messageId")
            nickname = data.json.get("chatMessage", {}).get("author", {}).get("nickname")
            user_id = data.json.get("chatMessage", {}).get("author", {}).get("uid")
            
            random_number = random.randint(0, len(goodbye_messages)-1)

            # Send a welcome message with the nickname
            send_message(community_id, chat_id, goodbye_messages[random_number])

            toggle = 0
        else:
            toggle = 1
    except Exception as e:
        print(e)