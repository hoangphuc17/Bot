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
    user_profile = cdhh.get_user_profile(sender_id)
    first_name = user_profile["first_name"]
    last_name = user_profile["last_name"]
    # id_user = user_profile["id"]

    check_user(sender_id)

    space = " "
    a = "Chào"
    b = "đến với Cặp Đôi Hoàn Hảo - Trữ Tình & Bolero. \nMình là LERO, rất vui được gặp bạn. Bạn có thể cùng mình cập nhật thông tin về chương trình một cách nhanh nhất. Cùng khám phá nào! 👇👇"
    seq = (a, last_name, first_name, b)
    text = space.join(seq)
    buttons = [
        Template.ButtonPostBack(
            "Home", "cdhh_home")
    ]
    cdhh.send(sender_id, Template.Buttons(text, buttons))
    return 'cdhh_greeting OK'


def cdhh_home(sender_id):
    # user_profile = cdhh.get_user_profile(sender_id)
    # first_name = user_profile["first_name"]
    # last_name = user_profile["last_name"]
    # id_user = user_profile["id"]

    check_user(sender_id)

    elements = [
        Template.GenericElement("Tin tức",
                                subtitle="Tin tức mới nhất từ Cặp Đôi Hoàn Hảo - Trữ Tình & Bolero",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/cdhh_tintuc.jpg",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Xem tin tức 👓", "news"),
                                    Template.ButtonPostBack(
                                        "Theo dõi tin tức 📸", "subscribe")
                                ]),
        Template.GenericElement("Xem chương trình",
                                subtitle="Chương trình phát sóng 20:30 thứ 5 hàng tuần trên VTV3.\nBạn có thế xem lại tập Full với các bản tình ca siêu ngọt ngào tại đây nha!",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/cdhh_xemtintuc.jpg",
                                buttons=[
                                    Template.ButtonWeb(
                                        "Tập 2", "https://www.youtube.com/watch?v=Ynu6u0WSxrU"),
                                    Template.ButtonWeb(
                                        "Tập 1", "https://www.youtube.com/watch?v=6xE6VOkRr4Qv")
                                ]),
        Template.GenericElement("Bình chọn thí sinh",
                                subtitle="Tin tức mới nhất từ Cặp Đôi Hoàn Hảo - Trữ Tình & Bolero",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/cdhh_binhchon.jpg",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Xem tin tức 👓", "read_news"),
                                    Template.ButtonPostBack(
                                        "Theo dõi tin tức 📸", "subscribe_news")
                                ]),
        Template.GenericElement("Tìm hiểu thêm thông tin",
                                subtitle="Theo dõi Cặp Đôi Hoàn Hảo ngay nhé",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/cdhh_lienhe.jpg",
                                buttons=[
                                    Template.ButtonWeb(
                                        "Facebook", "https://www.facebook.com/capdoihoanhaotrutinhbolero/"),
                                    Template.ButtonWeb(
                                        "Youtube", "https://www.youtube.com/channel/UCF5RuEuoGrqGtscvLGLOMew/featured")

                                ])
    ]
    cdhh.send(sender_id, Template.Generic(elements))
    return 'cdhh_home OK'
