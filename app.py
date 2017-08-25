# -*- coding: utf-8 -*-

import os
import sys
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


from CoreChatbot.TheVoiceKid.home import *
from CoreChatbot.TheVoiceKid.vote_guess_menu import *
from CoreChatbot.TheVoiceKid.vote_guess_handle import *


app = Flask(__name__)

danh_sach_HLV = [
    "Vũ Cát Tường",
    "Tiên Cookie và Hương Tràm",
    "Soobin"
]


@app.route('/', methods=['GET'])
def verify():
    # Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == CONFIG['VERIFY_TOKEN']:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    log('verify successfully')
    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    payload = request.get_data(as_text=True)
    page.handle_webhook(payload, postback=postback_handler)
    page.handle_webhook(payload, message=message_handler)
    # page.handle_webhook(payload, quick_reply=quickreply_handler)

    return "ok", 200


# @page.handle_message
def message_handler(event):
    """:type event: fbmq.Event"""
    sender_id = event.sender_id
    message = event.message_text
    quickreply = event.quick_reply_payload.decode('utf-8')

    if message == 'home':
        home(sender_id)
        return

    else:
        pass
    # elif message == 'vote':
    #     vote()
    # elif message == 'chao':
    #     greeting(sender_id)
    # else:
    #     print('')

    # if quickreply == "teamcoTuong":
    #     page.send(sender_id, "ban da chon co Tuong")
    #     return
    # else:
    #     pass

    if danh_sach_HLV.count(quickreply) == 1:
        vote_guess_handle(sender_id)
        page.send(sender_id, "ok ok ok")
        # return


# @page.handle_postback
def postback_handler(event):
    sender_id = event.sender_id
    postback = event.postback_payload

    if postback == 'home':
        home(sender_id)
        return
    elif postback == 'vote_guess':
        vote_guess_menu(sender_id)
        return

    return


# def quickreply_handler(event):
#     sender_id = event.sender_id
#     quickreply = event.quick_reply_payload
#
#     if


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)
