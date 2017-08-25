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
db = client.voted_users
voters = db.voters


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
    check_voter = voters.find_one({'id_user': sender_id})
    if bool(check_voter):
        page.send(sender_id, "User da binh chon")

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

    else:
        print "user chua binh chon"
        revote(sender_id)
    return


def vote_handle_quick_reply(sender_id, quick_reply_payload):

    # get user info
    user_profile = page.get_user_profile(sender_id)  # return dict
    first_name = user_profile["first_name"]
    last_name = user_profile["last_name"]
    id_user = user_profile["id"]

    space = " "
    text = "Bạn đã dự đoán dự đoán thành công đội có thí sinh đạt được vị trí cao nhất của chương trình. Dự đoán của bạn đang dành cho team của"
    text = text.decode('utf-8')
    seq = (text, quick_reply_payload)
    a = space.join(seq)
    page.send(sender_id, a)

    page.send(sender_id, Attachment.Image(
        "http://210.211.109.211/weqbfyretnccbsaf/hinh5_minigame.jpg"))

    # insert user vao database hoac update database
    check_voter = voters.find_one({'id_user': sender_id})
    voter = {
        'first_name': first_name,
        'last_name': last_name,
        'id_user': id_user,
        'HLV_da_binh_chon': quick_reply_payload,
        'thoi_gian': datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
    }

    if bool(check_voter):
        # update
        voters.update_one({'_id': check_voter}, {"$set": voter}, upsert=False)
        page.send(sender_id, HLV_da_binh_chon)

    else:
        # insert
        insert_voter = voters.insert_one(voter)
        page.send(sender_id, voter["HLV_da_binh_chon"])

    return
