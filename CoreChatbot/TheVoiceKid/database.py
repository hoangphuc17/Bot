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
def add_cat(cat_id, cat_title, cat_keyword):
    check_cat_id = FAQ2.find_one({'cat_id': cat_id})
    if bool(check_cat_id):
        print('cat_id giong nhau')
    else:
        new_cat = {
            'level': '1',
            'cat_id': cat_id,
            'cat_title': cat_title,
            'cat_keyword': cat_keyword
        }
        FAQ2.insert_one(new_cat)


def add_subcat(cat_id, subcat_id, subcat_title, subcat_keyword):
    check_subcat_id = FAQ2.find_one({'subcat_id': subcat_id})
    if bool(check_subcat_id):
        print('subcat_id giong nhau')
    else:
        new_subcat = {
            'level': '2',
            'subcat_id': subcat_id,
            'subcat_title': subcat_title,
            'subcat_keyword': subcat_keyword,
            'cat_id': cat_id
        }
        FAQ2.insert_one(new_subcat)


def add_qa(cat_id, subcat_id, qa_id, question, qa_keyword, answer):
    check_keyword = FAQ2.find_one({'qa_keyword': qa_keyword})
    if bool(check_keyword):
        print('qa_keyword giong nhau')
    else:
        new_qa = {
            'level': '3',
            'qa_id': qa_id,
            'question': question,
            'answer': answer,
            'qa_keyword': qa_keyword,
            'subcat_id': subcat_id,
            'cat_id': cat_id
        }
        FAQ2.insert_one(new_qa)
