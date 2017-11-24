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

# SUB_FUNCTION


def list_of_keyword():
    list_keyword = []
    for each_node in FAQ4.find():
        for keyword in each_node['keyword']:
            list_keyword.append({
                'keyword': keyword,
                'level': each_node['level'],
                'id_node': each_node['id_node'],
                'id_node_parents': each_node['id_node_parents']
            })

    return list_keyword


# hàm này để giúp tìm nhánh
def check_node_in_list_branch(node_a, node_b, list_branch):
    # kiểm tra xem node đã có trong list_branch chưa
    # nếu chưa thì return False
    # nếu đã có rồi, return True

    check_node_in_list = False

    for item in list_branch:
        if any(c in item for c in (node_a['id_node'], node_b['id_node'])):
            check_node_in_list = True
        else:
            check_node_in_list = False

    return check_node_in_list


def check_a_perfect_branch(chosen_branch):
    check_perfection = False
    found = False

    for id_node in chosen_branch:
        if found:
            break
        abc = FAQ4.find({'id_node': id_node})
        for id_node_parents in abc['id_node_parents']:
            if id_node_parents in chosen_branch:
                check_perfection = True
            else:
                check_perfection = False
                found = True

    return check_perfection


def find_answer_in_a_perfect_branch(chosen_branch):
    for id_node in chosen_branch:
        abc = FAQ4.find({'id_node': id_node})
        if abc['answer'] != '':
            return abc['answer']


# MAIN FUNCTION
def find_node(word_list):
    # tìm các node có keyword trùng với word trong message
    # dùng hash table
    list_keyword = list_of_keyword()
    list_node_in_message = []
    for word in word_list:
        for item in list_keyword:
            if word == item['keyword']:
                list_node_in_message.append(item)

    return list_node_in_message


def find_branch(word_list):
    list_node_in_message = find_node(word_list)
    list_branch = []

    # task 1: tìm ra các node cùng nhánh với nhau, thêm các node đó vào cùng 1 nhánh trong list_branch
    # task 2: chọn ra nhánh có số node nhiều nhất

    # task 1:
    for node_a in list_node_in_message:
        for node_b in list_node_in_message:
            if node_b['id_node_parents'] == node_a['id_node']:
                # đã tìm ra 2 node cùng nhánh
                if check_node_in_list_branch(node_a, node_b, list_branch):
                    # cập nhật list_branch
                    for item in list_branch:
                        if node_a in item:
                            item.append(node_b['id_node'])
                        elif node_b in item:
                            item.append(node_a['id_node'])

                else:
                    # tạo mới 1 branch trong list_branch
                    list_branch.append([node_a, node_b])

    # task 2:
    chosen_branch = max(list_branch, key=len)

    return chosen_branch


def handle_mess_2(sender_id, message):
    if message is not None:
        print('mess is not none')
        word_list = word_sent(message)

        find_node(word_list)
        chosen_branch = find_branch(word_list)

        if check_a_perfect_branch(chosen_branch):
            answer = find_answer_in_a_perfect_branch(chosen_branch)
            cbtest.send(sender_id, answer)
        else:
            print('abc')
    else:
        print('message is none')
