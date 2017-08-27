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

danh_sach_hinh_anh_HLV = {
    "Vũ Cát Tường": "hinh5_minigame.jpg",
    "Tiên Cookie và Hương Tràm": "hinh6_minigame.jpg",
    "Soobin": "hinh7_minigame.jpg"
}


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
    check_vote = users.find_one({'id_user': sender_id})
    # check_voter = users.find_one({'HLV_da_binh_chon': ''})

    # page.send(sender_id, check_vote["HLV_da_binh_chon"])

    if check_vote["HLV_da_binh_chon"] == "":
        print "user chua binh chon"
        revote(sender_id)

    else:
        # page.send(sender_id, "User da binh chon")
        space = " "
        a = "Bạn đã dự đoán dự đoán thành công đội có thí sinh đạt được vị trí cao nhất của chương trình. Dự đoán của bạn đang dành cho team của"
        a = a.decode('utf-8')
        b = check_vote["HLV_da_binh_chon"]
        seq = (a, b)
        text = space.join(seq)

        buttons = [
            Template.ButtonPostBack("Bình chọn lại", "revote"),
            Template.ButtonPostBack("Home", "home")
        ]

        page.send(sender_id, Template.Buttons(text, buttons))
    return


def vote_handle_quick_reply(sender_id, quick_reply_payload):
    link_hinh_hlv = "http://210.211.109.211/weqbfyretnccbsaf/" + \
        danh_sach_hinh_anh_HLV[quick_reply_payload]
    page.send(sender_id, Attachment.Image(link_hinh_hlv))

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


def vote_rule(sender_id):
    text = "- Mỗi bạn tham gia sẽ có 01 lựa chọn cho việc dự đoán đội huấn luyện viên có thí sinh đạt được giải quán quân 🎊 của chương trình.\n- Nếu bạn thay đổi ý kiến, dự đoán được BTC ghi nhận là dự đoán cuối cùng mà bạn chọn.\n- Nếu dự đoán đúng và may mắn, bạn sẽ nhận được 01 phần quà 🎁 hấp dẫn từ ban tổ chức.\n Hãy tận dụng “giác quan thứ 6” của mình để 'rinh' quà về nhà nào!\n👉👉👉 “Giọng Hát Việt Nhí” 2017 sẽ chính thức được phát sóng vào lúc 21h10 thứ 7 hằng tuần trên kênh VTV3"

    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]

    page.send(sender_id, Template.Buttons(text, buttons))

    return
