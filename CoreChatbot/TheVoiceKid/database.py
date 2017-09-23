# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
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
    # print 'day la ham save_message cua user'

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

    USER.update_one(
        {'id_user': sender_id},
        {'$push': {'message': {'content': message,
                               'time': datetime.datetime.now()}}}
    )


# collection FAQ
def insert_question(metadata, question, answer, rank):
    check_question = FAQ.find_one({'question': question})
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


# FAQ collection
def first_level(id_first_level, id_node_children, keyword):
    first_level_node = {
        'id_first_level_node': id_first_level,
        'id_node_children': id_node_children,
        'keyword': keyword,
        'priority': 1
    }
    FAQ.insert_one(first_level_node)


def medial_level(id_medial_level, id_node_parent, id_node_children, keyword):
    medial_level_node = {
        'id_medial_level_node': id_medial_level,
        'id_node_parent': id_node_parent,
        'id_node_children': id_node_children,
        'keyword': keyword,
        'priority': 2
    }
    FAQ.insert_one(medial_level_node)


def final_level(id_final_level, id_node_parent, keyword, answer):
    final_level_node = {
        'id_final_level_node': id_final_level,
        'id_node_parent': id_node_parent,
        'keyword': keyword,
        'answer': answer,
        'priority': 3
    }
    FAQ.insert_one(final_level_node)
