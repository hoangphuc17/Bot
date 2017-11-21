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
FAQ4 = db.FAQ4


def handle_mess(sender_id, message):
    if message is not None:
        # cbtest.send(sender_id, message)
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
            count_lv1 = 0
            count_lv2 = 0
            print('1')
            # print(record['list_array'][1])
            for word in word_dict:
                print(record['list_array'][0])
                if word in record['list_array'][0]:
                    print('2')
                    print(record['list_array'], ' co chua ', word)
                    # count_lv1 = count_lv1 + 1
                    for word in word_dict:
                        if word in record['list_array'][1]:
                            cbtest.send(sender_id, record['list_array'][2])

    else:
        print('Message is None')


def handle_mess_2(sender_id, message):
    if message is not None:
        print('mess is not none')
        cbtest.send(sender_id, 'day la ham handle mess 2')

        word_list = word_sent(message)
        lv1 = {}
        lv2 = {}
        lv3 = {}

        for lv1_node in FAQ4.find({'level': '1'}):
            for word_lv1 in word_list:
                if word_lv1 in lv1_node['keyword']:
                    print('tim thay level 1, id la: ', lv1_node['id_node'])
                    lv1 = lv1_node

        if lv1 != {}:
            # tim thay lv1 node
            for lv2_node in FAQ4.find({'id_node_parent': lv1['id_node'], 'level': '2'}):
                for word_lv2 in word_list:
                    if word_lv2 in lv2_node['keyword']:
                        print('tim thay level 2, id la: ', lv2_node['id_node'])
                        lv2 = lv2_node

            if lv2 != {}:
                # tim thay lv2 node
                for lv3_node in FAQ4.find({'id_node_parent': lv2['id_node'], 'level': '3'}):
                    for word_lv3 in word_list:
                        if word_lv3 in lv3_node['keyword']:
                            print('tim thay level 3, id la: ',
                                  lv3_node['id_node'])
                            lv3 = lv3_node

                if lv3 != {}:
                    # tim thay lv3 node
                    cbtest.send(sender_id, lv3['answer'])
                else:
                    # khong tim thay lv3 node
                    cbtest.send(sender_id, 'khong tim thay lv3 node')
            else:
                # khong tim thay lv2 node
                cbtest.send(sender_id, 'khong tim thay lv2 node')
        else:
            cbtest.send(sender_id, 'khong tim thay cau hoi')

    else:
        print('message is none')
