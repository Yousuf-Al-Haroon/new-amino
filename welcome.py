from numpy import random

from send_message import send_message


# List of welcome messages
welcome_messages = [
    "مرحبًا @! نورت المجموعة، أتمنى لك قضاء وقت ممتع معنا.",
    "أهلاً وسهلاً بك @! نورت المجموعة، نحن سعداء بانضمامك إلينا.",
    "مرحباً @! نورت المجموعة، نتمنى أن تجد هنا ما يسعدك ويفيدك.",
    "أهلاً ومرحبًا بك @! نورتنا بحضورك في المجموعة.",
    "مرحبًا بك @! نتمنى لك إقامة ممتعة ومفيدة معنا.",
    "أهلاً @! سعداء بانضمامك إلى المجموعة، فأهلاً بك بيننا.",
    "مرحبًا وأهلاً بك @! نحن سعداء بتواجدك معنا.",
    "أهلاً وسهلاً @! نتمنى لك أوقاتاً سعيدة ومفيدة في المجموعة.",
    "مرحبًا بك @! نحن في انتظار مشاركاتك وإسهاماتك القيمة.",
    "أهلًا بك @! نورت المجموعة، نتمنى لك تجربة ممتعة ومثمرة.",
    "مرحبًا @! نحن سعداء بتواجدك، استمتع بوقتك معنا.",
    "أهلاً وسهلاً بك @! نورتنا بحضورك، نتمنى لك إقامة سعيدة.",
    "مرحبًا بك @! نتمنى أن تجد هنا ما يسعدك ويفيدك.",
    "أهلاً @! نحن سعداء بانضمامك إلى المجموعة، استمتع بوقتك.",
    "مرحبًا وأهلاً بك @! نورت المجموعة، نتمنى لك إقامة ممتعة."
]


toggle = 0

def on_group_member_join(data):
    try:
        global toggle
        if toggle == 1:
            community_id = data.json.get("ndcId")
            chat_id = data.json.get("chatMessage", {}).get("threadId")
            message_id = data.json.get("chatMessage", {}).get("messageId")
            nickname = data.json.get("chatMessage", {}).get("author", {}).get("nickname")
            user_id = data.json.get("chatMessage", {}).get("author", {}).get("uid")
            user_icon = data.json.get("chatMessage", {}).get("author", {}).get("icon")

            random_number = random.randint(0, len(welcome_messages)-1)

            # Send a welcome message with the nickname
            send_message(community_id, chat_id, welcome_messages[random_number].replace("@", nickname), embedImage=user_icon, embedTitle=nickname)

            toggle = 0
        else:
            toggle = 1
    except Exception as e:
        print(e)