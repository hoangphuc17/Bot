# -*- coding: utf-8 -*-
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page


def home(sender_id):
    page.send(sender_id, "ham home")
    elements = [
        Template.GenericElement("Tin tức mới nhất từ chương trình “Giọng Hát Việt Nhí” 2017",
                                subtitle="Nơi cập nhật những tin tức mới nhất từ chương trình “Giọng Hát Việt Nhí” 2017",
                                image_url="http://210.211.109.211/weqbfyretnccbsaf/hinh2_home_tin_tuc.jpg",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Xem tin tức 👓", "news_read"),
                                    Template.ButtonPostBack(
                                        "Theo dõi tin tức 📸", "news_follow")
                                ]),
        Template.GenericElement("Video Full - The Voice Kids 2017 | Giọng Hát Việt Nhí mùa 5",
                                subtitle="Xem lại bản đầy dủ các tập đã được phát sóng trên Youtube, Live Streaming",
                                image_url="http://2sao.vietnamnetjsc.vn/images/2017/06/14/08/58/the-face-2017.png",
                                buttons=[
                                    Template.ButtonWeb(
                                        "Xem trên Youtube", "https://www.youtube.com/playlist?list=PLEhBV4sOYnBmMRpojxlAB4pcOA9V18B8J"),
                                    Template.ButtonWeb(
                                        "Xem trên Youtube", "https://www.youtube.com/playlist?list=PLEhBV4sOYnBmMRpojxlAB4pcOA9V18B8J")
                                ]),
        Template.GenericElement("Bình chọn thí sinh yêu thích nhất hàng tuần",
                                subtitle="Hãy bình chọn cho thí sinh bạn yêu thích nhất hàng tuần bạn nhé!",
                                image_url="https://img.saostar.vn/2017/03/28/1168861/thefaceonline-concept-milor-hoangku.jpg",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Bình chọn", "binh_chon"),
                                    Template.ButtonPostBack(
                                        "Thể lệ bình chọn", "the_le_binh_chon")
                                ]),
        Template.GenericElement("Video Full - The Face Vietnam 2017",
                                subtitle="Xem lại bản đầy đủ các tập đã được phát sóng trên Youtube, Live Streaming.",
                                image_url="https://i.ytimg.com/vi/i9nFRcKPA4I/maxresdefault.jpg",
                                buttons=[
                                    Template.ButtonWeb(
                                        "Xem trên Youtube", "https://www.youtube.com/playlist?list=PLEhBV4sOYnBmMRpojxlAB4pcOA9V18B8J")
                                ]),
        Template.GenericElement("About us",
                                subtitle="Theo dõi The Face Vietnam 2017 thông qua các kênh truyền thông",
                                image_url="http://static.vietnammoi.vn/stores/news_dataimages/duynt/042017/17/16/1002_the-face-vietnam.jpg",
                                buttons=[
                                    Template.ButtonWeb(
                                        "Youtube", "https://www.youtube.com/channel/UCF5RuEuoGrqGtscvLGLOMew/featured"),
                                    Template.ButtonWeb(
                                        "Instagram", "https://www.instagram.com/thefacevietnam_official/"),
                                    Template.ButtonWeb(
                                        "Facebook", "https://www.facebook.com/TheFaceVietNamOfficial/")

                                ])
    ]
    page.send(sender_id, Template.Generic(elements))
