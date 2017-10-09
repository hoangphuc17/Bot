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


from underthesea import word_sent

import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
USER = db.USER
FAQ = db.FAQ
NEWS = db.NEWS
NOFAQ = db.NOFAQ


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
            new_nofaq = {'message': message}
            NOFAQ.insert_one(new_nofaq)
            print('khong tim thay cau hoi trong FAQ, vao nofaq de xem')
            # text = "Ôi, mình chưa hiểu rõ ý bạn lắm ☹. Có lẽ nội dung này đã vượt ngoài bộ nhớ của mình mất rồi 🤖🤖🤖. Bạn nhấn tính năng “Home” bên duới 👇 để xem thêm những thông tin của chương trình nha, biết đâu bạn sẽ tìm ra được câu trả lời cho thắc mắc của mình đấy! 😉"
            # text = "Oops…!!! ‘Từ Khóa’ của bạn chưa chính xác. Hãy thử lại với một ‘Từ Khóa’ khác nhé!"
            text = "Oops..!Hiện tại mình chưa có dữ liệu câu hỏi của bạn, mình sẽ cập nhật và trả lời bạn sớm nhất. Hãy tiếp tục kết nối với chương trình qua các tính năng khác bạn nhé!"
            buttons = [
                Template.ButtonPostBack(
                    "Home", "home")
            ]
            page.send(sender_id, Template.Buttons(text, buttons))

    else:
        pass

    return


def find_cat(sender_id, word_dict):
    dict_cat = {}
    count_word_in_cat = 0
    # chosen_cat = {}
    for cat_document in FAQ2.find({'level': '1'}):
        for word in word_dict:
            if word in cat_document['cat_keyword']:
                count_word_in_cat = count_word_in_cat + 1
        dict_cat.update({cat_document['cat_title']: count_word_in_cat})
        count_word_in_cat = 0
        # print (dict_cat)

    # gom cac cat_title co count_word_in_cat giong nhau lai
    flipped = {}
    for key, value in dict_cat.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    # print(flipped)

    # xep lai de thanh maximum
    maximum = max(flipped, key=flipped.get)
    # max_dict = {maximum: flipped[maximum]}

    if len(flipped[maximum]) == 1:  # chi co 1 cat co so luong keyword la max
        # print(flipped[maximum][0])
        chosen_cat = FAQ2.find_one(
            {'level': '1', 'cat_title': flipped[maximum][0]})
        text = 'da chon dc cat ' + chosen_cat['cat_title']
        page.send(sender_id, text)
        return chosen_cat

    elif len(flipped[maximum]) > 1:  # co nhieu cat co so luong keyword max bang nhau
        question = 'cau hoi cua ban lien quan toi khai niem nao'
        quick_replies = []
        for cat_title in flipped[maximum]:
            payload = '>' + \
                FAQ2.find_one({'level': '1', 'cat_title': cat_title})['cat_id']
            quick_replies.append(QuickReply(
                title=cat_title, payload=payload))
        page.send(sender_id,
                  question,
                  quick_replies=quick_replies,
                  metadata="DEVELOPER_DEFINED_METADATA")

    else:  # khong co cat nao, max = 0
        text = 'cat_document: ko tim dc tu khoa'
        page.send(sender_id, text)


def find_subcat(sender_id, word_dict, chosen_cat):
    dict_subcat = {}
    count_word_in_subcat = 0
    for subcat_document in FAQ2.find({'level': '2', 'cat_id': chosen_cat['cat_id']}):
        for word in word_dict:
            if word in subcat_document['subcat_keyword']:
                count_word_in_subcat = count_word_in_subcat + 1
        dict_subcat.update(
            {subcat_document['subcat_title']: count_word_in_subcat})
        count_word_in_subcat = 0
        # print (dict_subcat)

    # gom cac cat_title co count_word_in_cat giong nhau lai
    flipped = {}
    for key, value in dict_subcat.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    print(flipped)

    # xep lai de thanh maximum
    maximum = max(flipped, key=flipped.get)
    # max_dict = {maximum: flipped[maximum]}
    # print(maximum, flipped[maximum])

    if len(flipped[maximum]) == 1:  # chi co 1 cat co so luong keyword la max
        # print(flipped[maximum][0])
        chosen_subcat = FAQ2.find_one(
            {'level': '2', 'subcat_title': flipped[maximum][0], 'cat_id': chosen_cat['cat_id']})
        text = 'da chon dc subcat ' + chosen_subcat['subcat_id']
        page.send(sender_id, text)
        return chosen_subcat

    else:  # len(flipped[maximum]) > 1
        question = 'cau hoi cua ban lien quan toi khai niem nao'
        quick_replies = []
        for subcat_title in flipped[maximum]:
            subcat = FAQ2.find_one(
                {'level': '2', 'cat_id': chosen_cat['cat_id'], 'subcat_title': subcat_title})
            payload = '>' + chosen_cat['cat_id'] + '>' + subcat['subcat_id']
            quick_replies.append(QuickReply(
                title=subcat_title, payload=payload))
        page.send(sender_id,
                  question,
                  quick_replies=quick_replies,
                  metadata="DEVELOPER_DEFINED_METADATA")


def find_qa(sender_id, word_dict, chosen_subcat):
    dict_qa = {}
    count_word_in_qa = 0
    print(chosen_subcat)
    for qa_document in FAQ2.find({'level': '3', 'cat_id': chosen_subcat['cat_id'], 'subcat_id': chosen_subcat['subcat_id']}):
        for word in word_dict:
            if word in qa_document['qa_keyword']:
                count_word_in_qa = count_word_in_qa + 1
        dict_qa.update(
            {qa_document['question']: count_word_in_qa})
        count_word_in_qa = 0
        # print (dict_cat)

    # gom cac cat_title co count_word_in_cat giong nhau lai
    flipped = {}
    for key, value in dict_qa.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    # print(flipped)

    # xep lai de thanh maximum
    maximum = max(flipped, key=flipped.get)
    # max_dict = {maximum: flipped[maximum]}

    if len(flipped[maximum]) == 1:  # chi co 1 cat co so luong keyword la max
        # print(flipped[maximum][0])
        chosen_qa = FAQ2.find_one(
            {'level': '3', 'question': flipped[maximum][0]})
        text = 'da chon dc qa ' + chosen_subcat['question']
        page.send(sender_id, text)
        return chosen_qa

    else:  # len(flipped[maximum]) > 1
        text = 'cau hoi nao dung voi mong muoon cua ban nhat'
        quick_replies = []
        for question in flipped[maximum]:
            text = text + ('\n' + question.get + '. ' + question)
            qa = FAQ2.find_one(
                {'level': '3', 'cat_id': chosen_subcat['cat_id'], 'subcat_id': chosen_subcat['subcat_id']})
            payload = '>' + chosen_subcat['cat_id'] + '>' + \
                chosen_subcat['subcat_id'] + '>' + qa['qa_id']
            quick_replies.append(QuickReply(
                title=question.get, payload=payload))
        page.send(sender_id,
                  text,
                  quick_replies=quick_replies,
                  metadata="DEVELOPER_DEFINED_METADATA")


def handle_faq_quickreply(quickreply_dict):
    length = len(quickreply_dict)
    if length == 2:
        cat_id = quickreply_dict[1]
        if length == 3:
            subcat_id = quickreply_dict[2]
            if length == 4:
                qa_id = quickreply_dict[3]
            else:
                print('co cat_id, co subcat_id, khong co qa_id trong quick_reply')
        else:
            print('co cat_id, khong co subcat_id trong quick_reply')
    else:
        print('khong co cat_id trong quick_reply')


def handle_faq_message(sender_id, message):
    if message is not None:

        # dau tien phai split message thanh 1 list word, neu list[0]==cat, list[2]==subcat thi xu ly tu khoa
        # neu ko co thi xu ly binh thuong

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

        # TACH TU (word_segmentation)
        word_dict = word_sent(message)
        # print(word_dict)

        chosen_cat = find_cat(sender_id, word_dict)
        if chosen_cat is not {}:
            print('da tim thay chosen_cat')
            chosen_subcat = find_subcat(sender_id, word_dict, chosen_cat)
            if chosen_subcat is not {}:
                print('da tim thay chosen_subcat')
                chosen_qa = find_qa(sender_id, word_dict, chosen_subcat)
                if chosen_qa is not None:
                    print('da tim thay chosen_qa')
                else:
                    print(
                        'tim thay chosen_cat,tim thay chosen_subcat, khong tim thay chosen_qa')
            else:
                print('tim thay chosen_cat, khong tim thay chosen_subcat')
        else:
            print('khong tim thay chosen_cat')

    else:
        pass
    return
