# coding: utf-8
import os
import sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

import Core_chatbot.messenger
from flask import Flask, request, send_from_directory, render_template
from Core_chatbot.config import CONFIG
from Core_chatbot.fbpage import page
from fbmq import Attachment, Template, QuickReply, Page

app = Flask(__name__)


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
    page.handle_webhook(payload,
                        postback=postback_handler)
    page.handle_webhook(payload,
                        message=message_handler)
    return "ok", 200


def message_handler(event):
    """:type event: fbmq.Event"""
    sender_id = event.sender_id
    message = event.message_text

    if message == 'home':
        home(sender_id)
    elif message == 'vote':
        vote()
    elif message == 'chao':
        greeting(sender_id)
    else:
        print('dmm, tao lay m, lam on nhap lai tin nhan dung cu phap dum tao, dcmm')


def postback_handler(event):
    sender_id = event.sender_id
    postback = event.postback_payload

    if postback == 'home':
        home(sender_id)
    # elif postback == '':


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
