# -*- coding: utf-8 -*-
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page


def vote_guess(sender_id):
    page.send(sender_id, Attachment.Image(
        "http://210.211.109.211/weqbfyretnccbsaf/home_hinh3_du_doan.jpg"))

    # gui cac quick reply
    question = "Bạn dự đoán thí sinh thuộc đội của huấn luyện viên nào sẽ xuất sắc giành lấy ngôi vị quán quân của chương trình?"
    quick_replies = [
        QuickReply(title="#teamcôTường", payload="teamcoTuong"),
        QuickReply(title="#teamcôTiênvàcôTràm", payload="teamcoTienvacoTram"),
        QuickReply(title="#teamchúSoobin", payload="teamchuSoobin")
    ]
    page.send(sender_id,
              question,
              quick_replies=quick_replies,
              metadata="DEVELOPER_DEFINED_METADATA")
