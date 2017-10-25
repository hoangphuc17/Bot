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
from CoreChatbot.Preparation.fbpage import cdhh


from CoreChatbot.CapDoiHoanHao.database import *

import PIL

from PIL import Image, ImageDraw, ImageFont


import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
USER = db.CDHH_USER
FAQ = db.CDHH_FAQ
NEWS = db.CDHH_NEWS


def cdhh_greeting(sender_id):
    # get user info
    user_profile = cdhh.get_user_profile(sender_id)  # return dict
    first_name = user_profile["first_name"]
    last_name = user_profile["last_name"]
    id_user = user_profile["id"]
    print (user_profile)

    # kiem tra user, neu chua co thi them vao database
    check_user = USER.find_one({'id_user': sender_id})
    if bool(check_user):
        # pass
        # cdhh.send(sender_id, "user da co trong database")
        print('day la ham greeting, user da co trong database')
    else:
        insert_new_user(first_name, last_name, id_user)

    space = " "
    a = "Chào"
    b = "đến với Cặp Đôi Hoàn Hảo - Trữ Tình & Bolero. \nMình là LERO, rất vui được gặp bạn. Bạn có thể cùng mình cập nhật thông tin về chương trình một cách nhanh nhất. Cùng khám phá nào! 👇👇"
    seq = (a, first_name, b)
    text = space.join(seq)
    buttons = [
        Template.ButtonPostBack(
            "Home", "cdhh_home")
    ]
    cdhh.send(sender_id, Template.Buttons(text, buttons))


def cdhh_home(sender_id):
    user_profile = cdhh.get_user_profile(sender_id)  # return dict
    first_name = user_profile["first_name"]
    last_name = user_profile["last_name"]
    id_user = user_profile["id"]

    # kiem tra user, neu chua co thi them vao database
    check_user = USER.find_one({'id_user': sender_id})
    if bool(check_user):
        print('user da co trong database')
    else:
        insert_new_user(first_name, last_name, id_user)

    elements = [
        Template.GenericElement("Đăng ký nhận tin",
                                subtitle="Nhấn theo dõi ngay để nhận được thông báo mỗi khi Cặp Đôi Hoàn Hảo cập nhật tin tức mới nhất nhé.",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh1_tin_tuc.jpg",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "fda", "fansign")
                                ]),
        Template.GenericElement("Tin tức",
                                subtitle="Tin tức mới nhất từ Cặp Đôi Hoàn Hảo - Trữ Tình & Bolero",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh1_tin_tuc.jpg",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Xem tin tức 👓", "read_news"),
                                    Template.ButtonPostBack(
                                        "Theo dõi tin tức 📸", "subscribe_news")
                                ]),
        Template.GenericElement("Xem chương trình",
                                subtitle="Chương trình phát sóng 20:30 thứ 5 hàng tuần trên VTV3.\nBạn có thế xem lại tập Full với các bản tình ca siêu ngọt ngào tại đây nha!",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh2_xem_video.jpg",
                                buttons=[
                                    Template.ButtonWeb(
                                        "Xem lại tập đã phát", "https://www.youtube.com/user/btcgionghatvietnhi"),
                                    Template.ButtonWeb(
                                        "Oh my kids", "https://www.youtube.com/playlist?list=PLEhBV4sOYnBml5RPOlILDvj5DqNwmG9AI"),
                                    Template.ButtonWeb(
                                        "Off the air", "https://www.youtube.com/playlist?list=PLEhBV4sOYnBk1BX8Jks9152rkNTIZQWuK")
                                ]),
        Template.GenericElement("Bình chọn thí sinh",
                                subtitle="Tin tức mới nhất từ Cặp Đôi Hoàn Hảo - Trữ Tình & Bolero",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh1_tin_tuc.jpg",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Xem tin tức 👓", "read_news"),
                                    Template.ButtonPostBack(
                                        "Theo dõi tin tức 📸", "subscribe_news")
                                ]),
        Template.GenericElement("Tìm hiểu thêm thông tin",
                                subtitle="Theo dõi Cặp Đôi Hoàn Hảo ngay nhé",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh4_about_us.jpg",
                                buttons=[
                                    Template.ButtonWeb(
                                        "Facebook", "https://www.facebook.com/gionghatvietnhi/"),
                                    Template.ButtonPostBack(
                                        "Giờ phát sóng", "time line"),
                                    Template.ButtonPostBack(
                                        "Giới thiệu", "introduce")
                                ])
    ]
    cdhh.send(sender_id, Template.Generic(elements))
