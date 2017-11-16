# -*- coding: utf-8 -*-
import os
import sys

from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG

from CoreChatbot.Preparation.fbpage import cbtest
from CoreChatbot.cbtest.cbtest_database import *


from underthesea import word_sent

import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
FAQ3 = db.FAQ3


def handle_mess(sender_id, message):
    if message is not None:
        print('Message gui toi la:\n', message)

        # tach tu
        word_dict = word_sent(message)
        print('Word Segmentation: ', word_dict)

        # level1_document = {}
        # for level1 in FAQ3.find({'chatbot': 'test', 'level': '1'}):
        #     for word in word_dict:
        #         if word in level1['keyword']:
        #             print(level1['id_node_level_1'], ' level1 co chua ', word)

        for record in FAQ3.find():
            print(record[1])
            # for word in word_dict:
            #     if
    else:
        print('Message is None')
