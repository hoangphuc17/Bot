# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from flask import Flask, request, send_from_directory, render_template

# from ApiMessenger import Attachment, Template, QuickReply, Page
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page

from CoreChatbot.TheVoiceKid.message import *
from CoreChatbot.TheVoiceKid.postback import *


import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc

USER = db.USER
FAQ = db.FAQ
NEWS = db.NEWS


app = Flask(__name__)

danh_sach_HLV = [
    "Vũ Cát Tường",
    "Tiên Cookie và Hương Tràm",
    "Soobin"
]
danh_sach_HLV = [i.decode('UTF-8') if isinstance(i,
                                                 basestring) else i for i in danh_sach_HLV]

subscribe_options = ["yes", "no"]


@app.route('/', methods=['GET'])
def verify():
    # if request.args.get("hub.verify_token") == 'phuc123':
    #     return request.args["hub.challenge"], 200
    # else:
    #     return "Verification token mismatch", 403
    # Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == CONFIG['VERIFY_TOKEN']:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    else:
        return "trouble in hub.mode or hub.challenge", 200

    return "verify successfully", 200


@app.route('/', methods=['POST'])
def webhook():
    payload = request.get_data(as_text=True)
    page.handle_webhook(payload, message=message_handler,
                        postback=postback_handler)
    a = 0
    if a < 2:
        # print ('a bang 0')
        # dieu kien ve thoi gian, chua giai quyet duoc van de minh la nguoi bat dau message

        # check = USER.find({'subscribe_news': 'yes'})
        # if bool(check):
        #     print('user da subscribe')
        # else:
        #     print('user chua subscribe')

        # for user in USER.find({'subscribe_news': 'yes'}):
        #     print user['id_user']
        #     print('bbbb')
        #     # page.send("dfdafdasfdas", user['id_user'])
        #     # send_news(user['id_user'])
        #     # print("da gui tin tuc moi")
        a = a + 1
        for user in USER.find():
            page.send(user['id_user'], 'alo alo')
    # print('aaaaa')
    return "ok", 200


# @page.handle_message
def message_handler(event):
    """:type event: fbmq.Event"""
    sender_id = event.sender_id
    message = event.message_text
    quickreply = event.quick_reply_payload

    keyword_list = {
        'home': home,
        'hello': greeting,
        'hi': greeting,
        'chào': greeting,
        'alo': greeting,
        'chao': greeting,
        'giờ phát sóng': timeline,
        'lịch phát sóng': timeline,
        'giới thiệu': introduce
    }

    if message in keyword_list:
        keyword_list[message](sender_id)

    elif danh_sach_HLV.count(quickreply) == 1:
        minigame1_handle_quick_reply(sender_id, quickreply)
        return

    elif subscribe_options.count(quickreply) == 1:
        handle_subscribe_news(sender_id, quickreply)
        return

    else:
        # luu tin nhan
        save_message(sender_id, message)
        # tra loi tin nhan
        # answer(message, sender_id)
        page.send(sender_id, "ko hieu tin nhan")

    return


def postback_handler(event):
    sender_id = event.sender_id
    postback = event.postback_payload

    postback_list = {
        'greeting': greeting,
        'home': home,
        'read_news': read_news,
        'subscribe_news': subscribe_news,
        'minigame1': minigame1,
        'minigame1_menu': minigame1_menu,
        'minigame1_vote': minigame1_vote,
        'minigame1_rule': minigame1_rule,
        'minigame2': minigame2,
        'minigame2_rule': minigame2_rule,
        'timeline': timeline,
        'introduce': introduce
    }

    if postback in postback_list:
        postback_list[postback](sender_id)

    return


# @app.route('/', methods=['POST'])
# def handle_subscribe():
#     news_for_subscribe()
#     print('day la handle subscribe')
#     return "ok", 200


def send_news(sender_id):
    element = Template.GenericElement(
        title="Sau Thụy Bình, Vũ Cát Tường lại chiêu mộ thành công ‘hoàng tử dân ca’ Tâm Hào",
        subtitle="Dự thi với ca khúc mang âm hưởng dân ca vô cùng mộc mạc nhưng cậu bé Nguyễn Tâm Hào vẫn khiến cả trường quay dậy sóng bởi tiếng hò reo, cổ vũ.",
        image_url="https://img.saostar.vn/265x149/2017/08/19/1500005/8.jpg",
        buttons=[
            Template.ButtonWeb(
                'Đọc tin', "https://saostar.vn/tv-show/sau-thuy-binh-vu-cat-tuong-lai-chieu-mo-thanh-cong-hoang-tu-dan-ca-tam-hao-1500005.html"),
            Template.ButtonPostBack('Về Home', 'home')
        ])
    page.send(sender_id, Template.Generic(element))
    return


# def news_for_subscribe():
#     for user in USER.find({'subscribe_news': 'yes'}):
#         send_news(user['id_user'])
#         print("da gui")
#     return


if __name__ == '__main__':
    app.run(host='210.211.109.211', port=5000, debug=True, threaded=True)
