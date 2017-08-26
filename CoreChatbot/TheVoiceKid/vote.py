# -*- coding: utf-8 -*-
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page

import datetime
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Phuc
users = db.user


check_voter = users.find_one({'HLV_da_binh_chon': ''})


def revote(sender_id):
    question = "Bạn dự đoán thí sinh thuộc đội của huấn luyện viên nào sẽ xuất sắc giành lấy ngôi vị quán quân của chương trình?"
    quick_replies = [
        QuickReply(title="#teamcôTường", payload="Vũ Cát Tường"),
        QuickReply(title="#teamcôTiênvàcôTràm", payload="Tiên Cookie và Hương Tràm"),
        QuickReply(title="#teamchúSoobin", payload="Soobin")
    ]
    page.send(sender_id,
              question,
              quick_replies=quick_replies,
              metadata="DEVELOPER_DEFINED_METADATA")

    return


def vote_menu(sender_id):
    if bool(check_voter):
        print "user chua binh chon"
        revote(sender_id)

    else:
        # page.send(sender_id, "User da binh chon")
        space = " "
        a = "Bạn đã dự đoán dự đoán thành công đội có thí sinh đạt được vị trí cao nhất của chương trình. Dự đoán của bạn đang dành cho team của"
        a = a.decode('utf-8')
        b = check_voter["HLV_da_binh_chon"]
        seq = (a, b)
        text = space.join(seq)

        buttons = [
            Template.ButtonPostBack("Bình chọn lại", "revote"),
            Template.ButtonPostBack("Home", "home")
        ]

        page.send(sender_id, Template.Buttons(text, buttons))
    return


def vote_handle_quick_reply(sender_id, quick_reply_payload):

    space = " "
    a = "Bạn đã dự đoán dự đoán thành công đội có thí sinh đạt được vị trí cao nhất của chương trình. Dự đoán của bạn đang dành cho team của"
    a = a.decode('utf-8')
    seq = (a, quick_reply_payload)
    text = space.join(seq)
    # page.send(sender_id, text)
    buttons = [
        Template.ButtonPostBack("Bình chọn lại", "revote"),
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))

    users.update_one(
        {'id_user': sender_id},
        {'$set': {'HLV_da_binh_chon': quick_reply_payload}}
    )

    return
