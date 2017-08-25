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


def vote_guess_handle(sender_id, quick_reply_payload):

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

    # insert user vao database
    voters = db.voters
    voter = {
        'first_name': first_name,
        'last_name': last_name,
        'id_user': id_user,
        'HLV_da_binh_chon': quick_reply_payload,
        'thoi_gian': datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
    }
    insert_voter = voters.insert_one(voter)
    print('One post: {0}'.format(insert_voter.inserted_id))
    page.send(sender_id, voter["last_name"])
    return
    # page.send(sender_id, quick_reply_payload)
