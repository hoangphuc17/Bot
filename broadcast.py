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
    url_broadcast_image = "http://210.211.109.211/weqbfyretnccbsaf/poster-tap6.jpg"
    page.send(sender_id, Attachment.Image(url_broadcast_image))
    text = "Cốc... Cốc... Bạn đẹp trai xinh gái gì đó ơi!!! Bạn còn nhớ cái hẹn tối thứ Bảy với Giọng Hát Việt Nhí đúng không nè?? Đón xem Tập đầu tiên Vòng đối đầu sẽ được phát sóng lúc 21h ngày 23/09/2017 trên kênh VTV3."
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))


def send_video_broadcast(sender_id):
    text = "Phiên bản Tài Smile Giọng Hát Việt Nhí 2017 đã xuất hiện thách thức phiên bản người lớn với màn Cover ca khúc HIT 'Phía Sau Một Cô Gái' siêu hài !!! 😁😁"
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))

    url_video = "http://210.211.109.211/weqbfyretnccbsaf/video_phiasaumotcogai_bolero.mp4"
    page.send(sender_id, Attachment.Video(url_video))


# check = USER.find_one({'id_user': id_phuc})
# if bool(check):
#     send_video_broadcast(id_duc)
# else:
#     pass

for user in USER.find():
    # send_video_broadcast(user['id_user'])
    send_broadcast(user['id_user'])
