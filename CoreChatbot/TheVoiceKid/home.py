# -*- coding: utf-8 -*-


def home(sender_id):
    page.send(sender_id, "ham home")
    elements = [
        Template.GenericElement("Fansign",
                                subtitle="Cùng đón nhận những lời chúc từ các thí sinh của The Face Việt Nam 2017 nào!",
                                image_url="https://img.saostar.vn/w600/2017/05/20/1288771/ava-top9.png",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Lấy Fansign", "fansign")
                                ]),
        Template.GenericElement("Tin tức mới nhất từ The Face 2017",
                                subtitle="Nơi cập nhật các tin tức mới nhất từ The Face 2017.",
                                image_url="http://2sao.vietnamnetjsc.vn/images/2017/06/14/08/58/the-face-2017.png",
                                buttons=[
                                    Template.ButtonPostBack(
                                        "Xem tin tức", "xem_tin_tuc"),
                                    Template.ButtonPostBack(
                                        "Theo dõi tin tức", "theo_doi_tin_tuc")
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
