# -*- coding: utf-8 -*-
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page

import datetime
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Phuc
users = db.user


def subscribe_news(sender_id):

    question = "Bằng cách đồng ý theo dõi tin tức dưới đây, bạn sẽ nhận được thông báo mỗi khi tin tức mới của chương trình “Giọng Hát Việt Nhí” 2017 được cập nhật.\nBạn muốn nhận thông báo chứ?"
    quick_replies = [
        QuickReply(title="Đồng ý luôn 😈", payload="yes"),
        QuickReply(title="Nhắc lại sau 😜", payload="no")
    ]
    page.send(sender_id,
              question,
              quick_replies=quick_replies,
              metadata="DEVELOPER_DEFINED_METADATA")

    return


def handle_subscribe_news(sender_id, quick_reply_payload):
    if quick_reply_payload == 'no':
        text = "Okey. Bất cứ khi nào bạn cần đăng ký nhận tin tức thì quay lại đây nhé!"
        buttons = [
            Template.ButtonPostBack("Home", "home")
        ]

        page.send(sender_id, Template.Buttons(text, buttons))
        users.update_one(
            {'id_user': sender_id},
            {'$set': {'subscribe': quick_reply_payload}}
        )
    else:
        text = "Bạn đã đăng ký nhận tin tức mới thành công. \nMỗi khi có bài viết mới về chương trình The Voice Kid 2017, mình sẽ thông tới bạn."
        buttons = [
            Template.ButtonPostBack("Home", "home")
        ]

        page.send(sender_id, Template.Buttons(text, buttons))
        users.update_one(
            {'id_user': sender_id},
            {'$set': {'subscribe': quick_reply_payload}}
        )
    return


def read_news(sender_id):
    elements = [
        Template.GenericElement(title="Tập 3 The Voice Kids: HLV Hương Tràm trổ tài hát Bolero theo yêu cầu của thí sinh",
                                subtitle="Thí sinh này trong tập 3 sắp tới đây còn muốn các HLV phải hát dòng nhạc không phải sở trường để có thể lựa chọn đội mình thích nhất.",
                                image_url="https://img.saostar.vn/2017/08/25/1518165/animation.gif",
                                item_url="https://saostar.vn/tv-show/tap-3-voice-kids-hlv-huong-tram-tro-tai-hat-bolero-theo-yeu-cau-cua-thi-sinh-1518165.html",
                                buttons=[
                                    Template.ButtonShare()
                                ]),
        Template.GenericElement(title="Vũ Cát Tường thích thú nhún nhảy nghe fan hát ‘Em ơi’ trước giờ ghi hình The Voice Kids ",
                                subtitle=" Bạn sẽ tan chảy với loạt biểu cảm đáng yêu này của HLV Vũ Cát Tường mất thôi! ",
                                image_url="https://img.saostar.vn/2017/08/23/1514781/pastelgranularargusfish.gif",
                                item_url="https://saostar.vn/tv-show/vu-cat-tuong-thich-thu-nhun-nhay-nghe-fan-hat-em-oi-truoc-gio-ghi-hinh-voice-kids-1514781.html",
                                buttons=[
                                    Template.ButtonShare()
                                ])

    ]
    page.send(sender_id, Template.Generic(elements))

    return
