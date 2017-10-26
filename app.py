# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from flask import Flask, request, send_from_directory, render_template

from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG

from CoreChatbot.Preparation.fbpage import page
from CoreChatbot.TheVoiceKid.message import *
from CoreChatbot.TheVoiceKid.postback import *

from CoreChatbot.Preparation.fbpage import cdhh
from CoreChatbot.CapDoiHoanHao.cdhh_message import *
from CoreChatbot.CapDoiHoanHao.cdhh_postback import *


app = Flask(__name__)

danh_sach_HLV = ["Vũ Cát Tường", "Tiên Cookie và Hương Tràm", "Soobin"]
subscribe_options = ["yes1", "yes2", "no"]
fansign_list = ["vct", "sb", "ht", "tc"]

cdhh_vote_list = ['Team Mai Tiến Dũng', 'Team Giang Hồng Ngọc', 'Team Đào Bá Lộc',
                  'Team Tiêu Châu Như Quỳnh', 'Team Erik', 'Team Hòa Mizy', 'Team Đức Phúc']


@app.route('/', methods=['GET'])
def verify():
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
    payload_dict = json.loads(payload)
    # if payload_dict['entry'][0]['id'] == "344510328981706":
    #     print('GIONG HAT VIET NHI')
    #     page.handle_webhook(payload, message=message_handler,
    #                         postback=postback_handler)
    if payload_dict['entry'][0]['id'] == "693691134038165":
        print('CAP DOI HOAN HAO')
        cdhh.handle_webhook(payload, message=message_handler_cdhh,
                            postback=postback_handler_cdhh)
        return "ok", 200
    else:
        return 'no app correspondent'


def postback_handler_cdhh(event):
    print('POSTBACK HANDLER CDHH')
    sender_id = event.sender_id
    postback = event.postback_payload

    postback_list = {
        'cdhh_greeting': greeting,
        'home': home,
        'news': news,
        'subscribe': subscribe,
        'vote': vote,
        'vote_menu': vote_menu
    }

    if postback in postback_list:
        postback_list[postback](sender_id)
    return 'postback ok'


def message_handler_cdhh(event):
    print('MESSAGE HANDLER CDHH')
    sender_id = event.sender_id
    message = event.message_text
    quickreply = event.quick_reply_payload

    if message is not None:
        message = message.lower()
    else:
        pass

    # quickreply_dict = quickreply.split('>')

    keyword_list = {
        'hello': greeting,
        'hi': greeting,
        'home': home
    }

    if message in keyword_list:
        keyword_list[message](sender_id)
    elif cdhh_vote_list.count(quickreply) == 1:
        vote_handler(sender_id, quickreply)

    return 'message ok'


# @page.handle_message
def message_handler(event):
    """:type event: fbmq.Event"""
    sender_id = event.sender_id
    message = event.message_text
    quickreply = event.quick_reply_payload

    if message is not None:
        message = message.lower()
    else:
        pass

    quickreply_dict = quickreply.split('>')

    keyword_list = {
        'home': home,
        'hello': greeting,
        'hi': greeting,
        'chào': greeting,
        'alo': greeting,
        'chao': greeting,
        'xin chào': greeting,
        'xin chao': greeting,
        'Xin chào': greeting,
        'giờ phát sóng': timeline,
        'lịch phát sóng': timeline,
        'giới thiệu': introduce,
        'subscribe': handle_subscribe_1,
        'fansign': fansign_menu
    }
    minigame2_keyword_list = ["đỉnh", "xinh", "bánh bèo", "chất",
                              "phũ", "cá tính", "đẹp trai", "ế", "cao", "hit", "cute", "nhọ"]

    if message in keyword_list:
        # message = message.lo
        keyword_list[message](sender_id)
        return

    elif message in minigame2_keyword_list:
        minigame2_handle_result(message, sender_id)
        return

    elif danh_sach_HLV.count(quickreply) == 1:
        minigame1_handle_quick_reply(sender_id, quickreply)
        return

    elif subscribe_options.count(quickreply) == 1:
        handle_subscribe_news(sender_id, quickreply)
        return

    elif fansign_list.count(quickreply) == 1:
        fansign_handle_quick_reply(sender_id, quickreply)
        return
    elif quickreply_dict[0] == '' and len(quickreply_dict) > 1:
        handle_faq_quickreply(sender_id, quickreply_dict)

    else:
        # luu tin nhan
        save_message(sender_id, message)
        # tra loi tin nhan
        # answer(message, sender_id)
        handle_faq_message(sender_id, message)

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
        'minigame2_menu': minigame2_menu,
        'time line': timeline,
        'introduce': introduce,
        'fansign': fansign_menu
    }

    if postback in postback_list:
        postback_list[postback](sender_id)

    return


if __name__ == '__main__':
    app.run(host='210.211.109.211', port=5000, debug=True, threaded=True)
