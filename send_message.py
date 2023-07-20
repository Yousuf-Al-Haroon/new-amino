from k_amino import SubClient
from login import login

def send_message(comId: int, chatId: str, message: str, file=None, fileType=None,
                 replyTo=None, mentionUserIds=None, stickerId=None, snippetLink=None,
                 ytVideo=None, snippetImage=None, embedId=None, embedType=None,
                 embedLink=None, embedTitle=None, embedContent=None, embedImage=None):
    """
    Send a message with various optional parameters.

    Args:
        comId (int): The ID of the community.
        chatId (str): The ID of the chat.
        message (str): The message to be sent.
        file (Optional[str]): The file to be sent.
        fileType (Optional[str]): The type of the file.
        replyTo (Optional[str]): The ID of the message to reply to.
        mentionUserIds (Optional[List[str]]): The IDs of the users to mention.
        stickerId (Optional[str]): The ID of the sticker to send.
        snippetLink (Optional[str]): The link of the snippet.
        ytVideo (Optional[str]): The YouTube video ID.
        snippetImage (Optional[str]): The image of the snippet.
        embedId (Optional[str]): The ID of the embed.
        embedType (Optional[str]): The type of the embed.
        embedLink (Optional[str]): The link of the embed.
        embedTitle (Optional[str]): The title of the embed.
        embedContent (Optional[str]): The content of the embed.
        embedImage (Optional[str]): The image of the embed.
    """
    ndc_client = SubClient(comId=comId)
    ndc_client.send_message(
        chatId=chatId,
        message=message,
        messageType=0,
        file=file,
        fileType=fileType,
        replyTo=replyTo,
        mentionUserIds=mentionUserIds,
        stickerId=stickerId,
        snippetLink=snippetLink,
        ytVideo=ytVideo,
        snippetImage=snippetImage,
        embedId=embedId,
        embedType=embedType,
        embedLink=embedLink,
        embedTitle=embedTitle,
        embedContent=embedContent,
        embedImage=embedImage
    )