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

from underthesea import word_sent


import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
FAQ3 = db.FAQ3
FAQ4 = db.FAQ4
SESSION = db.SESSION


# def faq3_level_1(chatbot, id_node_level_1, keyword):
#     node_level_1 = {
#         'chatbot': chatbot,
#         'id_node_level_1': id_node_level_1,
#         'level': '1',
#         'keyword': keyword
#     }
#     FAQ3.insert_one(node_level_1)


# def faq3_level_2(chatbot, id_node_level_1, id_node_level_2, keyword):
#     node_level_2 = {
#         'chatbot': chatbot,
#         'level': '2',
#         'node_level_1': id_node_level_1,
#         'id_node_level_2': id_node_level_2,
#         'keyword': keyword
#     }
#     FAQ3.insert_one(node_level_2)


# def faq3_answer(chatbot, id_node_level_2, answer):
#     node_answer = {
#         'chatbot': chatbot,
#         'level': 'answer',
#         'node_level_2': id_node_level_2,
#         'answer': answer
#     }
#     FAQ3.insert_one(node_answer)


# def faq3_list(lv1, lv2, ans):
#     new_lv1 = []
#     new_lv2 = []

#     for item in lv1:
#         new_item = word_sent(item)
#         for it in new_item:
#             new_lv1.append(it)

#     for item in lv2:
#         new_item = word_sent(item)
#         for it in new_item:
#             new_lv2.append(it)

#         # new_lv1.append(item)

#     lst = {
#         'list_array': [new_lv1, new_lv2, ans]
#     }
#     FAQ3.insert_one(lst)


def lv_1(id_node, id_node_parent, keyword, answer):
    new_lv1 = {
        'level': '1',
        'id_node': id_node,
        'id_node_parent': id_node_parent,
        'keyword': keyword,
        'answer': answer
    }
    FAQ4.insert_one(new_lv1)


def lv_2(id_node, id_node_parent, keyword, answer):
    new_lv2 = {
        'level': '2',
        'id_node': id_node,
        'id_node_parent': id_node_parent,
        'keyword': keyword,
        'answer': answer
    }
    FAQ4.insert_one(new_lv2)


def lv_3(id_node, id_node_parent, keyword, answer):
    new_lv3 = {
        'level': '3',
        'id_node': id_node,
        'id_node_parent': id_node_parent,
        'keyword': keyword,
        'answer': answer
    }
    FAQ4.insert_one(new_lv3)


# def check_session():


def node(level, id_node, list_id_node_parents, keyword, answer):
    new_node = {
        'level': level,
        'id_node': id_node,
        'list_id_node_parents': list_id_node_parents,
        'keyword': keyword,
        'answer': answer
    }
    FAQ4.insert_one(new_node)


def list_of_keyword():
    list_keyword = []
    for each_node in FAQ4.find():
        for keyword in each_node['keyword']:
            list_keyword.append({
                'keyword': keyword,
                'id_node': each_node['id_node'],
                'id_node_parents': each_node['id_node_parents']
            })

    return list_keyword
