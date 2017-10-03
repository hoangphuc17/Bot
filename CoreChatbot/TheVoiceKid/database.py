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

# from CoreChatbot.TheVoiceKid.database import *


import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
USER = db.USER
FAQ = db.FAQ
NEWS = db.NEWS

FAQ2 = db.FAQ2


# collection USER
def insert_new_user(first_name, last_name, id_user):
    new_user = {
        'first_name': first_name,
        'last_name': last_name,
        'id_user': id_user,
        'HLV_da_binh_chon': '',
        'subscribe_news': 'no',
        'message': [
            # {
            #     'content': '',
            #     'time': '',
            #     'type': ''
            # }
        ]
    }
    USER.insert_one(new_user)


def save_message(sender_id, message):
    if message is not None:
        check_user = USER.find_one({'id_user': sender_id})
        if bool(check_user):
            print("Day la ham save_message(). User da co trong database")
        else:
            user_profile = page.get_user_profile(sender_id)
            first_name = user_profile["first_name"]
            last_name = user_profile["last_name"]
            id_user = user_profile["id"]
            insert_new_user(first_name, last_name, id_user)

        USER.update_one(
            {'id_user': sender_id},
            {'$push': {'message': {'content': message,
                                   'time': datetime.datetime.now()}}}
        )
    else:
        pass

# collection FAQ


def insert_question(metadata, question, answer, rank):
    check_question = FAQ.find_one({'metadata': metadata})
    if bool(check_question):
        pass
    else:
        new_question = {
            "metadata": metadata,
            "question": question,
            "answer": answer,
            "rank": rank
        }
        FAQ.insert_one(new_question)


# collection NEWS
def insert_news(title, subtitle, image_url, item_url):
    check_news = NEWS.find_one({'item_url': item_url})
    if bool(check_news):
        pass
    else:
        new_news = {
            'title': title,
            'subtitle': subtitle,
            'image_url': image_url,
            'item_url': item_url
        }
        NEWS.insert_one(new_news)


# collection FAQ2
def add_cat(title, keyword):
    check_cat = FAQ2.find_one({'title': title})
    if bool(check_cat):
        pass
    else:
        new_cat = {
            'title': title,
            'keyword': keyword
        }
        FAQ2.insert_one(new_cat)
