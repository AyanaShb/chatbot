from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json, pafy
import errno
import os
from flex import flexTemplate
import sys, random, requests
import tempfile
import urllib, urllib3, urllib.parse, codecs
from urllib.parse import quote
from bs4 import BeautifulSoup
from pytube import YouTube
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)
app = Flask(__name__)
line_bot_api = LineBotApi('gnfrKrq5X2IR6bHb5nljFf+hABR7t7+CDoqSsRjgwQd2KWm8dsCHz3xv9DKYNCADeSHwURy/D+EJXfFTF48vyP0rwJh5s2KvxKF/M0likVDLfy1o2cbfY2oceL7ucg6oG55TGM+q2oS/dOPB3/+Z5VGUYhWQfeY8sLGRXgo3xvw=')
handler = WebhookHandler('491da0f79467e0c1a32c8539bf11a8e8')
flex = flexTemplate()
#===================[ LINKE STARTO ]=====================
#source by arsybai
@app.route('/')
def helo():
    return 'Hi there.. this is working :D'
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:handler.handle(body, signature)
    except InvalidSignatureError:abort(400)
    return 'OK'
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	text = event.message.text.lower()
	sender = event.source.user_id
	gid = event.source.sender_id
	line = line_bot_api
#===============================================================================[ ARSYBAI FUNC ]
	def getProfileName(sender):
		profile = line.get_profile(sender).display_name
		return profile
    def getProfileStatus(sender):
        profile = line.get_profile(sender).status_message
        return profile
	def sendMessage(tx):
		ggg = TextSendMessage(text=tx)
		return(line.reply_message(event.reply_token,ggg))
	def sendAudio(audio):
		message = AudioSendMessage(original_content_url=audio,duration=240000)
		line.reply_message(event.reply_token, message)
	def sendVideo(thumb, video):
		message = VideoSendMessage(original_content_url=thumb,preview_image_url=video)
		line_bot_api.reply_message(event.reply_token, message)
	def sendMessageV2(lst):
		return(line_bot_api.reply_message(event.reply_token,lst))

	def carouselMapping(contents):
		this = {"type": "carousel","contents": contents}
		return this
	def sendFlex(alt, contents):
		message = FlexSendMessage(alt_text="{}".format(str(alt)), contents=carouselMapping(contents))
		line.reply_message(event.reply_token,message)
	def sendImage(url):
		message = ImageSendMessage(original_content_url='{}'.format(str(url)),preview_image_url='{}'.format(str(url)))
		line_bot_api.reply_message(event.reply_token, message)
	def quickItem(label, tx):
		qi = QuickReplyButton(action=MessageAction(label=label, text=tx))
		return qi
	def sendMessageWithQuickReply(tx,items):
		message = TextSendMessage(text=tx,quick_reply=QuickReply(items=items))
		line_bot_api.reply_message(event.reply_token, message)
#===============================================================================[ STARTO ]
	if text == 'quickReply':
		"""
		This is for send Text message with quick reply
		"""
		items = [quickItem('Hello','Hello')]
		sendMessageWithQuickReply('hi',items)

	if text == '/creator':
		"""
		this is example if u just want to send a text message
		"""
		sendMessage('Hello Kampank!')
	if text == '/bye':
		if isinstance(event.source, SourceGroup):
           sendMessage('{} selamat tinggal ;)'.format(getProfileName(sender)))
           line.leave_group(event.source.group_id)
	if text == '/help':
	   helpmsg =   "\n    » Line Chat Bot♫ «" + "\n\n" + \
                        "Public Feature"        + "\n" + \
                        "01.   - /bye" + "\n" + \
                        "01.   - /gid" + "\n" + \
                        "01.   - /instagram:(name)" + "\n" + \
                        "02.   - /twitter:(name)"    + "\n" + \
                        "03.   - /facebook:(name)"   + "\n" + \
                        "Settings Bot"        + "\n" + \
                        "04.   - /mode:(1/2/3)" + "\n" + \
                        "05.   - /silent:(on/off)"    + "\n" + \
                        "05.   - /showuid:(on/off)"    + "\n" + \
                        "05.   - /setadmin:(uid)"    + "\n" + \
                        "05.   - /bye:(on/off)"    + "\n" + \
                        "\nversion : 7.0"     + \
                        "\nmaker : ayana"
       ghgg = {"type": "bubble",
                   "size": "micro",
                   "body": {"type": "box",
                            "layout": "vertical",
                            "contents": [{"type": "box",
                                          "layout": "vertical",
                                          "contents": [{"type": "box",
                                                        "layout": "vertical",
                                                        "contents": [{"type": "text",
                                                                      "text": helpmsg,
                                                                      "wrap": True,
                                                                      "size": "lg",
                                                                      "color": "#000000"}],
                                                        "borderWidth": "5px",
                                                        "borderColor": "#FAF0E6"}],
                                          "borderColor": "#00FFFF",
                                          "borderWidth": "5px"}],
                            "backgroundColor": "#FAF0E6"},
                   "styles": {"body": {"separator": True,
                                       "separatorColor": "#000000"}}}
       message = [ghgg] #use []
       sendFlex(alt='THIS IS FLEX MESSAGE', contents=message)
	if text == 'flex':
		"""
		This is example for send a flex message
		( template in flex.py file )
		"""
		message = [flex.contoh()] #use []
		sendFlex(alt='THIS IS FLEX MESSAGE', contents=message)

	if text == 'carousel':
		"""
		This is example for send a flex message carousel
		( template in flex.py file )
		"""
		message = [flex.contoh(), flex.contoh(), flex.contoh(), flex.contoh(), flex.contoh()]
		#just add more template :3 (Max 10)
		sendFlex(alt='THIS IS CAROUSEL MESSAGE', contents=message)

#===============================================================================[ END ]
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

"""ALHAMDULILLAH"""
