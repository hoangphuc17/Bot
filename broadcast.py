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
    # url_broadcast_image = "http://210.211.109.211/weqbfyretnccbsaf/broadcast1310.jpg"
    # page.send(sender_id, Attachment.Image(url_broadcast_image))
    # text = "Hôm nay trời rộng lên cao. Hóng The Voice Kids nôn nao cả ngày !!! Nhớ đón xem Giọng Hát Việt Nhí vào 21h tối nay trên VTV3 nhé bạn đáng yêu ơi ! 💕💕 "
    # text = "CHIẾC VÉ MAY MẮN - BÌNH CHỌN THÍCH SINH BẠN YÊU THÍCH\nTop 18 Giọng hát Việt Nhí 2017 đã lộ diện, Ban Tổ Chức chính thức mở cổng bình chọn 'Chiếc Vé May Mắn'.\nCơ hội 'Đặc Biệt' dành cho các giọng ca nhí bị loại trong vòng Liveshow chương trình có thể trở lại đêm Chung kết nếu nhận được Tổng lượt bình chọn cao nhất từ khán giả thông qua Zalo Page Giọng Hát Việt Nhí và Tạp chí điện tử Saostar.\n🔰 Bình chọn qua Tạp chí điện tử Saostar: http://saostar.vn"
    # page.send(sender_id, text)
    # text2 = "🔰 Bình chọn qua Zalo Giọng Hát Việt Nhí: zalo.me/gionghatvietnhi\n👉 Truy cập Zalo Page Giọng Hát Việt Nhí ➡️ Nhấn 'Quan Tâm'.\n👉 Vào mục tin nhắn ➡️ Bình Chọn ➡️ Click vào ảnh thí sinh bạn yêu thích để bình chọn ➡️ Xác nhận.\n👉 Mỗi tài khoản Zalo có tối đa 18 lượt bình chọn. Lưu ý mỗi thí sinh chỉ nhận được tối đa 1 lượt bình chọn.\n🔰 Bình chọn được mở từ ngày 07/10/2017 đến ngày 18/11/2017.\n#teamVuCatTuong #teamHuongTramTienCookie #teamSoobinHoangSon\nTheo dõi Fanpage và đồng hành cùng Giọng Hát Việt Nhí 2017 tìm ra Quán quân xứng đáng các bạn nhé!"
    # text = "Tèng teng! Tập 9 Giọng Hat Việt Nhí 2017 sẽ lên sóng vào lúc 21h00 ngày 14/10/2017 trên kênh VTV3. Các bạn nhớ đón xem nhé!"
    text = "Chào mừng Ngày Phụ Nữ Việt Nam 20-10. Xin kính chúc các fan của Giọng Hát Việt Nhí thật nhiều sức khỏe, niềm vui và hạnh phúc trong cuộc sống. Nhân đây chúng ta hãy cùng xem lại một màn trình diễn rất hay tại Vòng Đối Đấu nhé - ca khúc Chưa Bao Giờ Mẹ Kể trình bày bởi Quốc Thái, Thiên Thanh, Ái Vy đến từ team Soobin Hoàng Sơn."
    # page.send(sender_id, text)
    # text2 = ""
    buttons = [
        Template.ButtonWeb(
            '👉 Click để xem', 'https://www.youtube.com/watch?v=5aeJgzX7TS0'),
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))


def send_video_broadcast(sender_id):
    text = "Chào mừng Ngày Phụ Nữ Việt Nam 20-10. Xin kính chúc các fan của Giọng Hát Việt Nhí thật nhiều sức khỏe, niềm vui và hạnh phúc trong cuộc sống. Nhân đây chúng ta hãy cùng xem lại một màn trình diễn rất hay tại Vòng Đối Đấu nhé - ca khúc Chưa Bao Giờ Mẹ Kể trình bày bởi Quốc Thái, Thiên Thanh, Ái Vy đến từ team Soobin Hoàng Sơn."
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))

    url_video = "http://210.211.109.211/weqbfyretnccbsaf/video_20_10.mp4"
    page.send(sender_id, Attachment.Video(url_video))


# check = USER.find_one({'id_user': id_phuc})
# if bool(check):
#     send_video_broadcast(id_duc)
# else:
#     pass


# dict_user = []
# for user in USER.find():
#     dict_user.append(user['id_user'])

# for id_user in dict_user:
#     send_broadcast(id_user)
#     print('Co ', len(dict_user), ' user')
#     print('Da gui broadcast cho user thu:', dict_user.index(id_user))


send_broadcast(id_phuc2)
