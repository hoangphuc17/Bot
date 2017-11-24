# -*- coding: utf-8 -*-
import os
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
# from ApiMessenger import Attachment, Template
# from ApiMessenger.payload import QuickReply
# from ApiMessenger.fbmq import Page

# import CoreChatbot.Preparation.messenger
# from CoreChatbot.Preparation.config import CONFIG
# from CoreChatbot.Preparation.fbpage import page

# from underthesea import word_sent


import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
FAQ4 = db.FAQ4
SESSION = db.SESSION


def node(level, id_node, list_id_node_parents, keyword, answer):
    new_node = {
        'level': level,
        'id_node': id_node,
        'list_id_node_parents': list_id_node_parents,
        'keyword': keyword,
        'answer': answer
    }
    FAQ4.insert_one(new_node)


def add_node():
    node('1', '1', [], 'mua', '')
    node('2', '11', ['1'], 'áo', '')
    node('3', '111', ['1', '11'], 'm', 'A')
    node('3', '112', ['1', '11'], 'l', 'B')

    node('2', '12', ['1'], 'giày', '')
    node('3', '121', ['1', '12'], '8', 'C')
    node('3', '122', ['1', '12'], '9', 'D')

    node('1', '2', [], 'bán', '')
    node('2', '21', ['2', '21'], 'áo', '')
    node('3', '211', ['2', '21'], 'm', 'E')
    node('3', '212', ['2', '21'], 'l', 'F')

    node('2', '22', ['2'], 'giày', '')
    node('3', '221', ['2', '22'], '8', 'G')
    node('3', '222', ['2', '22'], '9', 'H')


add_node()
