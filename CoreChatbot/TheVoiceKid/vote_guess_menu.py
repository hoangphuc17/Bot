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
    voters = db.voters
    check_voter = voters.find_one({'id_user': sender_id})
    if bool(check_voter):
        page.send(sender_id, "User da binh chon")
        page.send(sender_id, check_voter["HLV_da_binh_chon"])

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
