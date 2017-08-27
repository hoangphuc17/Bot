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
from CoreChatbot.TheVoiceKid.vote import *
from CoreChatbot.TheVoiceKid.greeting import *
from CoreChatbot.TheVoiceKid.news import *
from CoreChatbot.TheVoiceKid.about_us import *


app = Flask(__name__)

danh_sach_HLV = [
    "Vũ Cát Tường",
    "Tiên Cookie và Hương Tràm",
    "Soobin"
]
danh_sach_HLV = [i.decode('UTF-8') if isinstance(i, basestring) else i for i in danh_sach_HLV]

subscribe_options = ["yes", "no"]


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
    # print "PAYLOAD LA: ", payload

    # ghi message ra log file
    old_stdout = sys.stdout
    log_file = open("message.log", "a")  # a la append
    sys.stdout = log_file
    print payload
    sys.stdout = old_stdout
    log_file.close()

    page.handle_webhook(payload, message=message_handler, postback=postback_handler)
    return "ok", 200


# @page.handle_message
def message_handler(event):
    """:type event: fbmq.Event"""
    sender_id = event.sender_id
    message = event.message_text
    quickreply = event.quick_reply_payload
    # quickreply_encode = event.quick_reply_payload.encode('utf-8')

    if message == 'home' or message == 'Home':
        home(sender_id)
        return
    elif message == 'chao' or message == 'hi' or message == 'Hi' or message == 'Chao':
        greeting(sender_id)
        return
    elif danh_sach_HLV.count(quickreply) == 1:
        vote_handle_quick_reply(sender_id, quickreply)
        return
    elif subscribe_options.count(quickreply) == 1:
        handle_subscribe_news(sender_id, quickreply)
        return

    else:
        text = "Ôi, mình chưa hiểu rõ ý bạn lắm ☹. Có lẽ nội dung này đã vượt ngoài bộ nhớ của mình mất rồi 🤖🤖🤖. Bạn nhấn tính năng “Home” bên duới 👇 để xem thêm những thông tin của chương trình nha, biết đâu bạn sẽ tìm ra được câu trả lời cho thắc mắc của mình đấy! 😉"
        buttons = [
            Template.ButtonPostBack(
                "Home", "home")
        ]
        page.send(sender_id, Template.Buttons(text, buttons))

    return


def postback_handler(event):
    sender_id = event.sender_id
    postback = event.postback_payload

    if postback == 'greeting':
        greeting(sender_id)
        return
    elif postback == 'home':
        home(sender_id)
        return
    elif postback == 'read_news':
        read_news(sender_id)
        return
    elif postback == 'subscribe_news':
        subscribe_news(sender_id)
        return
    elif postback == 'vote_menu':
        vote_menu(sender_id)
        return
    elif postback == 'revote':
        revote(sender_id)
        return
    elif postback == 'vote_rule':
        vote_rule(sender_id)
        return
    elif postback == 'timeline':
        timeline(sender_id)
        return
    elif postback == 'introduce':
        introduce(sender_id)
        return

    return


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)
