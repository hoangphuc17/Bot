# -*- coding: utf-8 -*-
import os
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page
from CoreChatbot.TheVoiceKid.database import *


import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
USER = db.USER
FAQ = db.FAQ
NEWS = db.NEWS


def answer(message, sender_id):
    if message is not None:

        # kiem tra user, neu chua co thi them vao database
        check_user = USER.find_one({'id_user': sender_id})
        if bool(check_user):
            # pass
            # page.send(sender_id, "user da co trong database")
            print('user da co trong database')
        else:
            user_profile = page.get_user_profile(sender_id)  # return dict
            first_name = user_profile["first_name"]
            last_name = user_profile["last_name"]
            id_user = user_profile["id"]
            insert_new_user(first_name, last_name, id_user)

        found_question = False

        for data in FAQ.find():
            final_data = {}
            count = 0
            metadata = data['metadata']
            for word in metadata:
                if word in message:
                    count = count + 1

            if count == len(data['metadata']):
                final_data = data
                found_question = True
                break

        if found_question:
            page.send(sender_id, final_data['answer'])
        else:
            print('khong tim thay cau hoi trong FAQ')
            # text = "Ôi, mình chưa hiểu rõ ý bạn lắm ☹. Có lẽ nội dung này đã vượt ngoài bộ nhớ của mình mất rồi 🤖🤖🤖. Bạn nhấn tính năng “Home” bên duới 👇 để xem thêm những thông tin của chương trình nha, biết đâu bạn sẽ tìm ra được câu trả lời cho thắc mắc của mình đấy! 😉"
            text = "Oops…!!! ‘Từ Khóa’ của bạn chưa chính xác. Hãy thử lại với một ‘Từ Khóa’ khác nhé!"
            buttons = [
                Template.ButtonPostBack(
                    "Home", "home")
            ]
            page.send(sender_id, Template.Buttons(text, buttons))

    else:
        pass

    return


def new_faq_answer(message, sender_id):
    if message is not None:
        # kiem tra user, neu chua co thi them vao database
        check_user = USER.find_one({'id_user': sender_id})
        if bool(check_user):
            # pass
            # page.send(sender_id, "user da co trong database")
            print("day la ham new_faq_answer")
            print('user da co trong database')
        else:
            user_profile = page.get_user_profile(sender_id)  # return dict
            first_name = user_profile["first_name"]
            last_name = user_profile["last_name"]
            id_user = user_profile["id"]
            insert_new_user(first_name, last_name, id_user)

        found_question = False
        final_data = {}

        if found_question:
            page.send(sender_id, final_data['answer'])
        else:
            print('khong tim thay cau hoi trong FAQ')
            # text = "Ôi, mình chưa hiểu rõ ý bạn lắm ☹. Có lẽ nội dung này đã vượt ngoài bộ nhớ của mình mất rồi 🤖🤖🤖. Bạn nhấn tính năng “Home” bên duới 👇 để xem thêm những thông tin của chương trình nha, biết đâu bạn sẽ tìm ra được câu trả lời cho thắc mắc của mình đấy! 😉"
            text = "Oops…!!! ‘Từ Khóa’ của bạn chưa chính xác. Hãy thử lại với một ‘Từ Khóa’ khác nhé!"
            buttons = [
                Template.ButtonPostBack(
                    "Home", "home")
            ]
            page.send(sender_id, Template.Buttons(text, buttons))

    else:
        pass

    return
