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


def greeting(sender_id):
    loi_chao = "Chào bạn. Tại đây bạn có thể cập nhật những tin tức nóng hổi, cũng như tham gia bình chọn cho thí sinh mình yêu thích nhất. Hãy bắt đầu bằng việc nhấn vào nút Home bên dưới hoặc bất cứ lúc nào bạn gõ 'home' hoặc 'menu' để quay về tính năng chính nha."
    buttons = [
        Template.ButtonPostBack(
            "Home", "home")
    ]
    page.send(sender_id, Template.Buttons(loi_chao, buttons))

    # get user info
    user_profile = page.get_user_profile(sender_id)  # return dict
    first_name = user_profile["first_name"]
    last_name = user_profile["last_name"]
    id_user = user_profile["id"]

    check_voter = users.find_one({'id_user': sender_id})
    if bool(check_voter):
        pass
    else:
        new_user = {
            'first_name': first_name,
            'last_name': last_name,
            'id_user': id_user,
            'HLV_da_binh_chon': '',
            'subscribe': 'no'
            # 'thoi_gian': datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        }
        users.insert_one(new_user)

    page.send(sender_id, "da them new_user")
    return
