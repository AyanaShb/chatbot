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
line_bot_api = LineBotApi('ITF2pYlsmRnvUtRSFmsAMXiwyRgnoInBXAWeDKrkRJFGFe3xO+J7kkBDbqdaKUskZXA93BjbXKZGF5F58FlxFkf32Rnd7GQA6TI/Tx2b47TKYzuxqA47GdLnzmXGKrerGtbknzaNoZHzuWipYuo2XAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c3d3e3ed1a47113b2271b3103691e133')
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
@handler.add(JoinEvent)
print("hhh")
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text.lower()
    sender = event.source.user_id
    gid = event.source.sender_id
    line = line_bot_api
#===============================================================================[ ARSYBAI FUNC ]
    def getProfileName(sender):
        profile = line_bot_api.get_profile(sender).display_name
        return profile
    def getProfileStatus(sender):
        profile = line_bot_api.get_profile(sender).status_message
        return profile
    def sendMessage(tx):
        ggg = TextSendMessage(text=tx)
        return(line_bot_api.reply_message(event.reply_token,ggg))
    def sendAudio(audio):
        message = AudioSendMessage(original_content_url=audio,duration=240000)
        line_bot_api.reply_message(event.reply_token, message)
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
        line_bot_api.reply_message(event.reply_token,message)
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
    if text == 'quickreply':
       items = [quickItem('Hello','Hello')]
       sendMessageWithQuickReply('hi',items)
    if text == '/creator':
       sendMessage('Hello Kampank!')
    if text == '/bye':
       if isinstance(event.source, SourceGroup):
          sendMessage('{} selamat tiinggal ;)'.format(getProfileName(sender)))
          line.leave_group(event.source.group_id)
    if text.startswith("/say:"):
       separate = text.split(":")
       number = text.replace(separate[0] + ":","")
       sendMessage('{} selamat tinggal ;)'.format(getProfileName(sender)))
       line.leave_group(event.source.group_id)
    if text == '/main':
       data = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://i.pinimg.com/originals/b4/a5/b4/b4a5b49dc155887837eab74e4ab545a4.png",
        "position": "absolute",
        "size": "full",
        "aspectMode": "cover",
        "offsetTop": "-55px",
        "offsetBottom": "0px",
        "offsetStart": "0px",
        "offsetEnd": "0px"
      },
      {
        "type": "text",
        "text": "Pilih yang mana?",
        "size": "lg",
        "weight": "bold",
        "color": "#FFFFFF",
        "offsetTop": "-15px"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Buta 40k",
              "text": "/buta40k"
            },
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Buta 100k",
              "text": "/buta100k"
            },
            "style": "primary"
          }
        ],
        "spacing": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Buta 500k",
              "text": "/buta500k"
            },
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Buta 1jt",
              "text": "/buta1jt"
            },
            "style": "primary"
          }
        ],
        "spacing": "md"
      }
    ],
    "spacing": "md"
  }
}
       message = [data] #use []
       sendFlex(alt='....', contents=message)
    if text == 'help':
       ghgg = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.pinimg.com/originals/b4/a5/b4/b4a5b49dc155887837eab74e4ab545a4.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Game Lobby",
        "size": "lg",
        "weight": "bold",
        "color": "#000000"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Daftar",
              "text": "/daftar"
            },
            "style": "primary",
            "color": "#00cec9"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Main",
              "text": "/main"
            },
            "style": "primary",
            "color": "#00cec9"
          }
        ],
        "spacing": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "saldoku",
              "text": "/saldo"
            },
            "style": "primary",
            "color": "#00cec9"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "Reset",
              "text": "/reset"
            },
            "style": "primary",
            "color": "#00cec9"
          }
        ],
        "spacing": "md"
      }
    ],
    "spacing": "md"
  },
  "styles": {
    "body": {
      "backgroundColor": "#0984e3"
    }
  }
}
       message = [ghgg] #use []
       sendFlex(alt='....', contents=message)
    if text == 'flex':
       message = [flex.contoh()] #use []
       sendFlex(alt='THIS IS FLEX MESSAGE', contents=message)
    if text == 'carousel':
       message = [flex.contoh(), flex.contoh(), flex.contoh(), flex.contoh(), flex.contoh()]
       sendFlex(alt='THIS IS CAROUSEL MESSAGE', contents=message)

#===============================================================================[ END ]
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
