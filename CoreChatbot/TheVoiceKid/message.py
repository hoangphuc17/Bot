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


def new_faq_answer(message, sender_id):
    if message is not None:
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

        found_question = False
        final_data = {}

        count_word_in_cat = 0
        count_cat = 0
        count_word_in_subcat = 0
        count_subcat = 0
        count_word_in_qa = 0
        count_qa = 0
        chosen_cat = {}
        chosen_subcat = {}
        chosen_qa = {}
        dict_cat = {}

        # TACH TU (word_segmentation)
        word_dict = word_sent(message)
        print(word_dict)

        # - voi moi tu trong word_dict, xet xem tu do co trong cat_keyword hay ko
        # - vi 1 tu co the o trong nhieu cat khac nhau, nen ta dat 1 bien ten la chosen_cat,
        # khi word co trong cat, thi choose_cat se tang 1 don vi, sau khi tim tat ca cat,
        # ta chon cat nao co choose_cat lon nhat de tiep tuc hanh trinh
        for cat_document in FAQ2.find({'level': '1'}):
            for word in word_dict:
                if word in cat_document['cat_keyword']:
                    count_word_in_cat = count_word_in_cat + 1
            dict_cat.update({cat_document['cat_title']: count_word_in_cat})
            count_word_in_cat = 0
        print (dict_cat)

        # gom cac cat co count_word_in_cat giong nhau lai
        flipped = {}
        for key, value in dict_cat.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                flipped[value].append(key)
        # print(flipped)

        # xep lai de thanh maximum
        maximum = max(flipped, key=flipped.get)
        max_dict = {maximum: flipped[maximum]}
        print(max_dict.keys())
        print(max_dict.values())

        #     if count_cat < count_word_in_cat:
        #         chosen_cat = cat_document
        #         count_cat = count_word_in_cat
        #     elif count_cat == count_word_in_cat:
        #         # 1. khong tim thay cat_document phu hop
        #         # 2. co 2 cat_document phu hop
        #         if chosen_cat != {}:  # co 2 cat_document phu hop
        #             text = chosen_cat['cat_id']
        #             page.send(sender_id, text)
        #         else:  # khong tim thay cat_document phu hop
        #             text = 'truong hop 2 chua co du lieu cho cau hoi nay'
        #             page.send(sender_id, text)

        #     else:  # count_cat > count_word_in_cat
        #         # khong tim thay hoac khong phai cat_document nay
        #         text = "chua co du lieu cho cau hoi nay"
        #         page.send(sender_id, text)

        # for subcat_document in FAQ2.find({'level': '2', 'cat_id': chosen_cat['cat_id']}):
        #     for word in word_dict:
        #         if word in subcat_document['subcat_keyword']:
        #             print(word + ' in subcat_document ' +
        #                   subcat_document['subcat_title'])
        #             count_word_in_subcat = count_word_in_subcat + 1
        #     if count_subcat < count_word_in_subcat:
        #         chosen_subcat = subcat_document
        #         count_subcat = count_word_in_subcat

        #     elif count_subcat == count_word_in_subcat:
        #         if chosen_subcat != {}:  # co 2 subcat_document phu hop
        #             text = chosen_subcat['subcat_id']
        #             page.send(sender_id, text)
        #         else:  # khong tim thay cat_document phu hop
        #             text = 'truong hop 2 chua co du lieu cho cau hoi nay, subcat'
        #             page.send(sender_id, text)

        #     else:  # count_cat > count_word_in_cat
        #         # khong tim thay hoac khong phai cat_document nay
        #         text = "chua co du lieu cho cau hoi nay"
        #         page.send(sender_id, text)

        # for qa_document in FAQ2.find({'level': '3', 'subcat_id': chosen_subcat['subcat_id']}):
        #     for word in word_dict:
        #         if word in qa_document['qa_keyword']:
        #             count_word_in_qa = count_word_in_qa + 1
        #     if count_qa < count_word_in_qa:
        #         chosen_qa = qa_document
        #         count_qa = count_word_in_qa
        #         found_question = True
        #         final_data = chosen_qa
        #     elif count_qa == count_word_in_qa:
        #         if chosen_qa != {}:  # co 2 qa_document phu hop
        #             text = chosen_qa['question']
        #             page.send(sender_id, text)
        #         else:  # khong tim thay qa_document phu hop
        #             text = 'truong hop 2 chua co du lieu cho cau hoi nay, subcat'
        #             page.send(sender_id, text)

        #     else:  # count_cat > count_word_in_cat
        #         # khong tim thay hoac khong phai qa_document nay
        #         text = "chua co du lieu cho cau hoi nay"
        #         page.send(sender_id, text)

        if found_question:
            page.send(sender_id, final_data['answer'])
        else:
            new_nofaq = {'message': message}
            NOFAQ.insert_one(new_nofaq)
            print('khong tim thay cau hoi trong FAQ, vao nofaq de xem')
            text = "Oops..!Hiện tại mình chưa có dữ liệu câu hỏi của bạn, mình sẽ cập nhật và trả lời bạn sớm nhất. Hãy tiếp tục kết nối với chương trình qua các tính năng khác bạn nhé!"
            buttons = [
                Template.ButtonPostBack(
                    "Home", "home")
            ]
            page.send(sender_id, Template.Buttons(text, buttons))

    else:
        pass

    return
