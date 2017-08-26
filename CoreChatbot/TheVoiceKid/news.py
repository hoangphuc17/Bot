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
        Template.GenericElement(title="Sau Thụy Bình, Vũ Cát Tường lại chiêu mộ thành công ‘hoàng tử dân ca’ Tâm Hào ",
                                subtitle=" Dự thi với ca khúc mang âm hưởng dân ca vô cùng mộc mạc nhưng cậu bé Nguyễn Tâm Hào vẫn khiến cả trường quay dậy sóng bởi tiếng hò reo, cổ vũ. ",
                                image_url="https://img.saostar.vn/265x149/2017/08/19/1500005/8.jpg",
                                item_url="https://saostar.vn/tv-show/sau-thuy-binh-vu-cat-tuong-lai-chieu-mo-thanh-cong-hoang-tu-dan-ca-tam-hao-1500005.html",
                                buttons=[
                                    Template.ButtonShare()
                                ]),
        Template.GenericElement(title="Thể hiện hit của diva Hà Trần, ‘thiên thần nhí’ khiến Soobin, Vũ Cát Tường phải tung ‘chiêu’ hết mình chinh phục  ",
                                subtitle="  Lần đầu tiên ở mùa giải năm nay, Giọng hát Việt nhí 2017 đã có một thí sinh khiến các HLV phải tung hết tất cả các chiêu trò để chiêu dụ về đội của mình. ",
                                image_url="https://img.saostar.vn/265x149/2017/08/19/1500621/mg_8085.jpg",
                                item_url="https://saostar.vn/tv-show/hien-hit-cua-diva-ha-tran-thien-nhi-khien-soobin-vu-cat-tuong-phai-tung-chieu-het-minh-chinh-phuc-1500621.html",
                                buttons=[
                                    Template.ButtonShare()
                                ])

    ]
    page.send(sender_id, Template.Generic(elements))

    return
