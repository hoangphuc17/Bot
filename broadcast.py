# -*- coding: utf-8 -*-
import os
import sys
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
    url_broadcast_image = "http://210.211.109.211/weqbfyretnccbsaf/broadcast1010.jpg"
    page.send(sender_id, Attachment.Image(url_broadcast_image))
    # text = "Hôm nay trời rộng lên cao. Hóng The Voice Kids nôn nao cả ngày !!! Nhớ đón xem Giọng Hát Việt Nhí vào 21h tối nay trên VTV3 nhé bạn đáng yêu ơi ! 💕💕 "
    text = "CHIẾC VÉ MAY MẮN - BÌNH CHỌN THÍCH SINH BẠN YÊU THÍCH\nTop 18 Giọng hát Việt Nhí 2017 đã lộ diện, Ban Tổ Chức chính thức mở cổng bình chọn 'Chiếc Vé May Mắn'.\nCơ hội 'Đặc Biệt' dành cho các giọng ca nhí bị loại trong vòng Liveshow chương trình có thể trở lại đêm Chung kết nếu nhận được Tổng lượt bình chọn cao nhất từ khán giả thông qua Zalo Page Giọng Hát Việt Nhí và Tạp chí điện tử Saostar.\n🔰 Bình chọn qua Tạp chí điện tử Saostar: http://saostar.vn\n🔰 Bình chọn qua Zalo Giọng Hát Việt Nhí: zalo.me/gionghatvietnhi\n👉 Truy cập Zalo Page Giọng Hát Việt Nhí ➡️ Nhấn 'Quan Tâm'.\n👉 Vào mục tin nhắn ➡️ Bình Chọn ➡️ Click vào ảnh thí sinh bạn yêu thích để bình chọn ➡️ Xác nhận.\n👉 Mỗi tài khoản Zalo có tối đa 18 lượt bình chọn. Lưu ý mỗi thí sinh chỉ nhận được tối đa 1 lượt bình chọn.\n🔰 Bình chọn được mở từ ngày 07/10/2017 đến ngày 18/11/2017.\n#teamVuCatTuong #teamHuongTramTienCookie #teamSoobinHoangSon\nTheo dõi Fanpage và đồng hành cùng Giọng Hát Việt Nhí 2017 tìm ra Quán quân xứng đáng các bạn nhé!"
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))


def send_video_broadcast(sender_id):
    text = "Nào nào, trước khi Tập 7 lên sóng, chúng ta hãy cùng dự đoán kết quả đêm nay nhé !!! 😉😉\n\n⭐️ Đón xem Tập 7 - Vòng đối đầu | Giọng Hát Việt Nhí 2017 vào lúc 21h Ngày 30/09/2017 trên kênh VTV3.\n🔰 Livestream phát sóng độc quyền trên Fanpage Giọng Hát Việt Nhí."
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))

    url_video = "http://210.211.109.211/weqbfyretnccbsaf/video_30_9.mp4"
    page.send(sender_id, Attachment.Video(url_video))


# check = USER.find_one({'id_user': id_phuc})
# if bool(check):
#     send_video_broadcast(id_duc)
# else:
#     pass

# send_video_broadcast(id_phuc2)


for user in USER.find():
    # send_video_broadcast(user['id_user'])
    send_broadcast(user['id_user'])
