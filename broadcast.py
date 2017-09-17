# -*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page

from CoreChatbot.TheVoiceKid.database import *


import datetime
from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
USER = db.USER
FAQ = db.FAQ
NEWS = db.NEWS

id_phuc = "1588973231176132"
id_phuc2 = "1370330196399177"
id_chau = "1318278091631838"
id_duc = "1627683190629761"


def send_broadcast(sender_id):
    url_broadcast_image = "http://210.211.109.211/weqbfyretnccbsaf/poster-tap5-2.jpg"
    page.send(sender_id, Attachment.Image(url_broadcast_image))

    text = "TADAA !! TUẦN MỚI LẠI ĐẾN Giọng Hát Việt Nhí trở lại với bạn rồi đây !!! Đón xem Tập 5 đầy cảm xúc vào lúc 21h00 Thứ Bảy Ngày 16/09/2017 trên kênh VTV3 các bạn nhé! ;) ;) ahihi"
    text = "BẠN ĐÁNG YÊU ƠI !! Tập 5 | Giọng Hát Việt Nhí 2017 sắp phát sóng rồi đó !!! Bật ngay kênh VTV3 để theo dõi chương trình cùng Gia đình thân yêu bạn nhé !! :*"
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))


# send_broadcast(id_chau)


for user in USER.find():
    send_broadcast(user['id_user'])
    print "da gui"
