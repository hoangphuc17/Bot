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
SESSION = db.SESSION


# def handle_mess(sender_id, message):
#     if message is not None:
#         print('Message gui toi la:\n', message)

#         # tach tu
#         word_dict = word_sent(message)
#         print('Word Segmentation: ', word_dict)

#         for record in FAQ3.find():
#             count_lv1 = 0
#             count_lv2 = 0
#             print('1')
#             for word in word_dict:
#                 print(record['list_array'][0])
#                 if word in record['list_array'][0]:
#                     print('2')
#                     print(record['list_array'], ' co chua ', word)
#                     for word in word_dict:
#                         if word in record['list_array'][1]:
#                             cbtest.send(sender_id, record['list_array'][2])

#     else:
#         print('Message is None')


def find_node():
    # tìm các node có keyword trùng với word trong message
    # dùng hash table
    list_keyword = list_of_keyword()


def find_branch():
    # tìm các nhánh dựa trên list các node đã có


def check_parent():
    # kiểm tra 1 node có đủ các node parent hay không


def check_final_node_in_branch():
    # kiểm tra có node cuối cùng trên nhánh không
    # nếu có, có nghĩa là có 'answer'


def request_for_helping_from_user():
    # hỏi user


def send_answer(chatbot, id_node, sender_id):
    node = FAQ4.find({'id_node': id_node})
    chatbot.send(sender_id, node['answer'])


def check_child(id_node_parent):
    node_child = FAQ4.find({'id_node_parent': id_node_parent})
    if bool(node_child):
        list_node_child = []

        for i in node_child:
            list_node_child.append(i)

        if len(list_node_child) > 1:
            # co nhieu child
            return 'n'
        else:
            # chi co 1 child
            return '1'
    else:
        # khong co child
        return '0'


def check_final_node(id_node):
    # kiểm tra node nhập vào có câu trả lời trong node đó hay không
    # nếu có, có nghĩa là node đó là node cuối cùng của cây
    # nếu không, có nghĩa là nó có node sau, và sau đó ta cần check_child của node nhập vào
    node = FAQ4.find({'id_node': id_node})
    if node['answer'] != '':
        # có câu trả lời, nên node này là node cuối của cây
        return True
    else:
        # không có câu trả lời, check xem có child hay không
        return False


def find_document(level, id_node_parent, word_list):
    # tìm trong tất cả các node có cùng level và cùng id_node_parent, document nào chứa message trong keyword của mình

    # kiểm tra xem message trong word_list có trong keyword của node hay không
    # nếu có, thì return về document là node có chứa word trong keyword của node đó
    # nếu không, thì document sẽ rỗng, tức là {}
    document = {}
    for node in FAQ4.find({'level': level, 'id_node_parent': id_node_parent}):
        for word in word_list:
            if word in node['keyword']:
                document = node

    return document


def message_with_no_session(sender_id, message):
    cbtest.send(sender_id, 'message with no session')
    word_list = word_sent(message)
    lv_1 = {}
    lv_2 = {}
    lv_3 = {}

    # tìm document lv1, lv1 có ý nghĩa là intent của user
    lv_1 = find_document('1', '', word_list)

    if lv_1 != {}:
        # a. 2 level
        #     a1. đủ
        #     a2. thiếu
        # b. 3 level
        #     b1. đủ
        #     b2. thiếu

        # a1
        if check_child(lv_1['id_node']):
            lv_2 = find_document('2', lv_1['id_node'], word_list)

        else:
            # thiếu lv_2
            # nhưng có 2 trường hợp thiếu
            # 1. thiếu hơp

    else:
        cbtest.send(sender_id, 'khong tim duoc lv_1')


def get_all_child_node(id_node_parent):
    list_id_child_node = []
    for child in FAQ4.find({'id_node_parent': id_node_parent}):
        list_id_child_node.append(child['id_node'])

    return list_id_child_node


# def get_document_by_id(id_node):
#     FAQ4.find({'id'})


def message_with_session(sender_id, message):
    # mình cần biết node đầu tiên nào sesion đã đi qua
    # sau đó liệt kê và tìm tất cả các nhánh thuộc lv giữa
    # sau đó search tiếp ở lv cuối
    # nếu sau khi search mà không có keyword trùng thì sẽ xử lý như 1 message_with_no_session
    # có session có nghĩa là có tree = yes, có nghĩa là câu hỏi trước là 1 câu hỏi được duyệt qua cây
    cbtest.send(sender_id, 'message with session')
    user_with_session = SESSION.find_one({'sender_id': sender_id})
    id_lv_dau = user_with_session['node']['lv_dau']
    id_lv_giua = user_with_session['node']['lv_giua']
    id_lv_cuoi = user_with_session['node']['lv_cuoi']
    word_list = word_sent(message)

    # node_dau = FAQ4.find_one({'level': '1', 'id_node': id_lv_dau})
    list_id_child_node_dau = get_all_child_node(id_lv_dau)
    for id_child_node_dau in list_id_child_node_dau:
        for child_node_dau in FAQ4.find({'id_node': id_child_node_dau}):
            for word in word_list:
                if word in child_node_dau['keyword']:
                    lv_giua = child_node_dau


def new_user_session(sender_id):
    new_user_ss = {
        'sender_id': sender_id,
        'tree': 'no',  # kiem tra xem lan truoc no co o trong cay hay khong
        'node': {
            'lv_dau': '',
            'lv_giua': '',
            'lv_cuoi': ''
        },
        'flag': ''
    }
    SESSION.insert_one(new_user_ss)


def handle_mess_2(sender_id, message):
    if message is not None:
        print('mess is not none')
        cbtest.send(sender_id, 'day la ham handle mess 2')

        user_session = SESSION.find({'sender_id': sender_id})

        if bool(user_session):
            # user đã từng được check qua tree

            if user_session['tree'] == 'yes':
                # câu hỏi lần trước của user ở trong 1 tree,
                # nên lần này sẽ kiểm tra các nhánh của tree đó có chứa keyword này không
                message_with_session(sender_id, message)
            else:
                # nếu không sẽ xử lý như 1 câu hỏi bình thường, sẽ check qua các node đầu, giữa, cuối
                message_with_no_session(sender_id, message)

        else:
            # chưa có user trong database SESSION
            # tạo 1 record trong SESSION và tiến hành xử lý như message_with_no_session()
            new_user_session(sender_id)
            message_with_no_session(sender_id, message)

        # if bool(user_session):
        #     SESSION.update_one(
        #         {'sender_id': sender_id},
        #         {'$push': {'flag': '1'}}
        #     )
        # flag = {}

    else:
        print('message is none')
