# -*- coding: utf-8 -*-
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page


def home(sender_id):

    elements = [
        Template.GenericElement("Tin tức mới nhất từ chương trình “Giọng Hát Việt Nhí” 2017",
                                subtitle="Nơi cập nhật những tin tức mới nhất từ chương trình “Giọng Hát Việt Nhí” 2017",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh1_tin_tuc.jpg",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Xem tin tức 👓", "read_news"),
                                    Template.ButtonPostBack(
                                        "Theo dõi tin tức 📸", "subscribe_news")
                                ]),
        Template.GenericElement("Video Full - The Voice Kids 2017 | Giọng Hát Việt Nhí mùa 5",
                                subtitle="Xem lại bản đầy dủ các tập đã được phát sóng trên Youtube, Live Streaming",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh2_xem_video.jpg",
                                buttons=[
                                    Template.ButtonWeb(
                                        "Xem trên Youtube", "https://www.youtube.com/user/btcgionghatvietnhi"),
                                    Template.ButtonWeb(
                                        "Xem trên Facebook", "https://www.youtube.com/user/btcgionghatvietnhi")
                                ]),
        Template.GenericElement("Dự đoán kết quả và giành lấy cơ hội nhận quà",
                                subtitle="Tham gia dự đoán kết quả của cuộc thi để nhận được những phần quà hấp dẫn nhất từ ban tổ chức",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh3_du_doan.jpg",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Tham gia dự đoán 👍", "vote_menu"),
                                    Template.ButtonPostBack(
                                        "Thể lệ dự đoán 📜", "vote_rule")
                                ]),
        Template.GenericElement("About us",
                                subtitle="Theo dõi chương trình Giọng Hát Việt Nhí 2017 tại các kênh truyền thông",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/home_hinh4_about_us.jpg",
                                buttons=[
                                    # Template.ButtonWeb(
                                    #     "Youtube", "https://www.youtube.com/user/btcgionghatvietnhi"),
                                    Template.ButtonWeb(
                                        "Facebook", "https://www.facebook.com/gionghatvietnhi/"),
                                    Template.ButtonPostBack(
                                        "Giờ phát sóng", "timeline"),
                                    Template.ButtonPostBack(
                                        "Giới thiệu", "introduce")
                                ])
    ]
    page.send(sender_id, Template.Generic(elements))
    return
