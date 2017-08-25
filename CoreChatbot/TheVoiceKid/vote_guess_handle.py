# -*- coding: utf-8 -*-
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page

from pymongo import MongoClient
client = MongoClient('localhost', 27017)


def vote_guess_handle(sender_id, quick_reply_payload):

    space = " "
    text = "Bạn đã dự đoán dự đoán thành công đội có thí sinh đạt được vị trí cao nhất của chương trình. Dự đoán của bạn đang dành cho team của"
    text = text.decode('utf-8')
    seq = (text, quick_reply_payload)
    a = space.join(seq)
    page.send(sender_id, a)

    page.send(sender_id, Attachment.Image(
        "http://210.211.109.211/weqbfyretnccbsaf/hinh5_minigame.jpg"))

    # page.send(sender_id, quick_reply_payload)
