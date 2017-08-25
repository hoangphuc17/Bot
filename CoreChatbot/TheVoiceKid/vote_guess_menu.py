# -*- coding: utf-8 -*-
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.voted_users


def vote_guess_menu(sender_id):
    # page.send(sender_id, "abc")
    voters = db.voters
    check_voter = voters.find_one({'id_user': sender_id})
    if bool(check_voter):
        page.send(sender_id, "User da binh chon")

        space = " "
        a = "Bạn đã dự đoán dự đoán thành công đội có thí sinh đạt được vị trí cao nhất của chương trình. Dự đoán của bạn đang dành cho team của"
        a = a.decode('utf-8')
        b = check_voter["HLV_da_binh_chon"]

        if isinstance(b, str):
            page.send(sender_id, "str")
        elif isinstance(b, unicode):
            page.send(sender_id, "unicode")
        elif isinstance(b, ascii):
            page.send(sender_id, "ascii")

        seq = (a, b)
        text = space.join(seq)
        # page.send(sender_id, "abc")

        # buttons = [
        #     Templates.ButtonPostBack("Bình chọn lại", "revote"),
        #     Templates.ButtonPostBack("Home", "home")
        # ]
        #
        #
        # page.send(sender_id, Template.Buttons(text, buttons))
        buttons = [
            Templates.ButtonWeb("Open Web URL", "https://www.oculus.com/en-us/rift/"),
            Templates.ButtonPostBack("trigger Postback", "DEVELOPED_DEFINED_PAYLOAD"),
            Templates.ButtonPhoneNumber("Call Phone Number", "+16505551234")
        ]
        page.send(sender_id, "abc")
        # you can use a dict instead of a Button class
        #
        # buttons = [{'type': 'web_url', 'title': 'Open Web URL', 'value': 'https://www.oculus.com/en-us/rift/'},
        #          {'type': 'postback', 'title': 'trigger Postback', 'value': 'DEVELOPED_DEFINED_PAYLOAD'},
        #          {'type': 'phone_number', 'title': 'Call Phone Number', 'value': '+16505551234'}]

        page.send(sender_id, Template.Buttons("hello", buttons))
    else:
        page.send(sender_id, "User chua binh chon")
        page.send(sender_id, Attachment.Image(
            "http://210.211.109.211/weqbfyretnccbsaf/home_hinh3_du_doan.jpg"))

        # gui cac quick reply
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
