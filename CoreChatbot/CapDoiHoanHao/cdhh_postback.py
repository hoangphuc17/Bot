# -*- coding: utf-8 -*-
import os
import sys
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG


from CoreChatbot.Preparation.fbpage import cdhh
from CoreChatbot.CapDoiHoanHao.cdhh_database import *

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
    print(user_profile)
    # first_name = user_profile["first_name"]
    # last_name = user_profile["last_name"]

    # check_user(sender_id)

    # space = " "
    # a = "Chào"
    # b = "đến với Cặp Đôi Hoàn Hảo - Trữ Tình & Bolero. \nMình là LERO, rất vui được gặp bạn. Bạn có thể cùng mình cập nhật thông tin về chương trình một cách nhanh nhất. Cùng khám phá nào! 👇👇"
    # seq = (a, last_name, first_name, b)
    # text = space.join(seq)
    # buttons = [
    #     Template.ButtonPostBack(
    #         "Home", "home")
    # ]
    # cdhh.send(sender_id, Template.Buttons(text, buttons))
    return 'cdhh_greeting OK'


def cdhh_home(sender_id):
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
                                        "Bình chọn", "vote")

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


def news(sender_id):
    elements = []
    for news in NEWS.find():
        element = Template.GenericElement(
            title=news['title'],
            subtitle=news['subtitle'],
            image_url=news['image_url'],
            buttons=[
                Template.ButtonWeb('Đọc tin', news['item_url']),
                Template.ButtonPostBack('Về Home', 'home')
            ])
        elements.append(element)

    cdhh.send(sender_id, Template.Generic(elements))

    return 'news OK'


def subscribe(sender_id):
    question = "Bằng cách đồng ý theo dõi tin tức dưới đây, bạn sẽ nhận được thông báo mỗi khi tin tức mới của chương trình được cập nhật.\nBạn muốn nhận thông báo chứ?"
    quick_replies = [
        QuickReply(title="1 tuần 1 lần 😋", payload="yes1"),
        QuickReply(title="1 tuần 2 lần 😈", payload="yes2"),
        QuickReply(title="Nhắc lại sau 😜", payload="no")
    ]
    cdhh.send(sender_id,
              question,
              quick_replies=quick_replies,
              metadata="DEVELOPER_DEFINED_METADATA")

    return 'subscribe OK'


def subscribe_handler(sender_id, quick_reply_payload):
    if quick_reply_payload == 'no':
        text = "Okey. Bất cứ khi nào bạn cần đăng ký nhận tin tức thì quay lại đây nhé!"
        buttons = [
            Template.ButtonPostBack("Home", "home")
        ]

        cdhh.send(sender_id, Template.Buttons(text, buttons))
        USER.update_one(
            {'id_user': sender_id},
            {'$set': {'subscribe': quick_reply_payload}}
        )
    else:
        text = "Bạn đã đăng ký nhận thông báo thành công. \nMỗi khi có thông báo mới về chương trình, mình sẽ gửi tới bạn."
        buttons = [
            Template.ButtonPostBack("Home", "home")
        ]

        cdhh.send(sender_id, Template.Buttons(text, buttons))
        USER.update_one(
            {'id_user': sender_id},
            {'$set': {'subscribe': quick_reply_payload}}
        )
    return 'subscribe handler OK'


def vote(sender_id):
    check_vote = USER.find_one({'id_user': sender_id})

    if check_vote['vote'] == '':
        # user chua binh chon
        vote_menu(sender_id)
    else:
        # user da binh chon
        space = " "
        a = "Bạn đã dự đoán thành công. Dự đoán của bạn đang dành cho"
        b = check_vote["vote"]
        seq = (a, b)
        text = space.join(seq)

        buttons = [
            Template.ButtonPostBack("Bình chọn lại", "vote_menu"),
            Template.ButtonPostBack("Home", "home")
        ]

        cdhh.send(sender_id, Template.Buttons(text, buttons))

    return 'vote OK'


def vote_menu(sender_id):
    question = 'Bình chọn ngay cho thí sinh bạn yêu thích nhất ngay nào! Bạn thuộc'
    quick_replies = [
        QuickReply(title="Team Mai Tiến Dũng", payload="Team Mai Tiến Dũng"),
        QuickReply(title="Team Giang Hồng Ngọc",
                   payload="Team Giang Hồng Ngọc"),
        QuickReply(title="Team Đào Bá Lộc", payload="Team Đào Bá Lộc"),
        QuickReply(title='Team Tiêu Châu Như Quỳnh',
                   payload='Team Tiêu Châu Như Quỳnh'),
        QuickReply(title='Team Erik', payload='Team Erik'),
        QuickReply(title='Team Hòa Mizy', payload='Team Hòa Mizy'),
        QuickReply(title='Team Đức Phúc', payload='Team Đức Phúc')
    ]
    cdhh.send(sender_id,
              question,
              quick_replies=quick_replies,
              metadata="DEVELOPER_DEFINED_METADATA")
    return 'vote_menu OK'


def vote_handler(sender_id, quickreply):
    space = " "
    a = "Bạn đã dự đoán thành công. Dự đoán của bạn đang dành cho"
    seq = (a, quickreply)
    text = space.join(seq)
    buttons = [
        Template.ButtonPostBack("Bình chọn lại", "vote_menu"),
        Template.ButtonPostBack("Home", "home")
    ]
    cdhh.send(sender_id, Template.Buttons(text, buttons))

    USER.update_one(
        {'id_user': sender_id},
        {'$set': {'vote': quickreply}}
    )
    return 'vote handler OK'
