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
client = MongoClient('localhost', 27017)
db = client.Phuc
users = db.user
FAQ = db.FAQ

danh_sach_hinh_anh_HLV = {
    "Vũ Cát Tường": "hinh5_minigame.jpg",
    "Tiên Cookie và Hương Tràm": "hinh6_minigame.jpg",
    "Soobin": "hinh7_minigame.jpg"
}


def greeting(sender_id):
    # them cau hoi vao data FAQ
    insert_new_questions()

    # get user info
    user_profile = page.get_user_profile(sender_id)  # return dict
    first_name = user_profile["first_name"]
    last_name = user_profile["last_name"]
    id_user = user_profile["id"]

    space = " "
    a = "Chào"
    b = "😍. Cùng mình cập nhật những tin tức “nóng hổi” của chương trình “Giọng Hát Việt Nhí” 2017 tại chatbot này bạn nhé 😉. Ngoài ra, bạn còn có cơ hội tham gia các màn dự đoán “nẩy lửa” và nếu may mắn bạn có thể “rinh” về những phần quà vô cùng hấp dẫn nữa đấy. Giờ thì còn chần chừ gì mà không bắt đầu cuộc “trò chuyện thân mật” này nào !!!\n⏩⏩⏩ Quay về tính năng chính bằng cách ấn phím “Home” hoặc gõ vào chữ “Home” hoặc “Menu” 👇\n⏩⏩⏩ Chương trình “Giọng Hát Việt Nhí” 2017 sẽ được phát sóng vào lúc 21h10 thứ 7 hằng tuần trên kênh VTV3📺"
    a = a.decode('utf-8')
    b = b.decode('utf-8')
    seq = (a, first_name, b)
    text = space.join(seq)
    buttons = [
        Template.ButtonPostBack(
            "Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))

    check_user = users.find_one({'id_user': sender_id})
    if bool(check_user):
        pass
    else:
        new_user = {
            'first_name': first_name,
            'last_name': last_name,
            'id_user': id_user,
            'HLV_da_binh_chon': '',
            'subscribe': 'no'
            # 'tin_tuc_da_doc': {
            #     'title': '',
            #     'subtitle': '',
            #     'item_url': '',
            #     'image_url': ''
            # }
            # 'thoi_gian': datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        }
        users.insert_one(new_user)

    return


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
        text = "Bạn đã đăng ký nhận tin tức mới thành công. \nMỗi khi có bài viết mới về chương trình The Voice Kid 2017, mình sẽ thông báo tới bạn."
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


def revote(sender_id):
    question = "Bạn dự đoán thí sinh thuộc đội của huấn luyện viên nào sẽ xuất sắc giành lấy ngôi vị quán quân của chương trình?"
    quick_replies = [
        QuickReply(title="#teamcôTường", payload="Vũ Cát Tường"),
        QuickReply(title="#teamcôTiênvàcôTràm", payload="Tiên Cookie và Hương Tràm"),
        QuickReply(title="#teamchúSoobin", payload="Soobin")
    ]
    page.send(sender_id,
              question,
              quick_replies=quick_replies,
              metadata="DEVELOPER_DEFINED_METADATA")

    return


def vote_menu(sender_id):
    check_vote = users.find_one({'id_user': sender_id})
    # check_voter = users.find_one({'HLV_da_binh_chon': ''})

    # page.send(sender_id, check_vote["HLV_da_binh_chon"])

    if check_vote["HLV_da_binh_chon"] == "":
        print "user chua binh chon"
        revote(sender_id)

    else:
        # page.send(sender_id, "User da binh chon")
        space = " "
        a = "Bạn đã dự đoán dự đoán thành công đội có thí sinh đạt được vị trí cao nhất của chương trình. Dự đoán của bạn đang dành cho team của"
        a = a.decode('utf-8')
        b = check_vote["HLV_da_binh_chon"]
        seq = (a, b)
        text = space.join(seq)

        buttons = [
            Template.ButtonPostBack("Bình chọn lại", "revote"),
            Template.ButtonPostBack("Home", "home")
        ]

        page.send(sender_id, Template.Buttons(text, buttons))
    return


def vote_handle_quick_reply(sender_id, quick_reply_payload):
    hinh_hlv = "http://210.211.109.211/weqbfyretnccbsaf/" + \
        danh_sach_hinh_anh_HLV[quick_reply_payload.encode('utf-8')]
    page.send(sender_id, Attachment.Image(hinh_hlv))

    space = " "
    a = "Bạn đã dự đoán dự đoán thành công đội có thí sinh đạt được vị trí cao nhất của chương trình. Dự đoán của bạn đang dành cho team của"
    a = a.decode('utf-8')
    seq = (a, quick_reply_payload)
    text = space.join(seq)
    # page.send(sender_id, text)
    buttons = [
        Template.ButtonPostBack("Bình chọn lại", "revote"),
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))

    users.update_one(
        {'id_user': sender_id},
        {'$set': {'HLV_da_binh_chon': quick_reply_payload}}
    )

    return


def vote_rule(sender_id):
    text = "- Mỗi bạn tham gia sẽ có 01 lựa chọn cho việc dự đoán đội huấn luyện viên có thí sinh đạt được giải quán quân 🎊 của chương trình.\n- Nếu bạn thay đổi ý kiến, dự đoán được BTC ghi nhận là dự đoán cuối cùng mà bạn chọn.\n- Nếu dự đoán đúng và may mắn, bạn sẽ nhận được 01 phần quà 🎁 hấp dẫn từ ban tổ chức.\n Hãy tận dụng “giác quan thứ 6” của mình để 'rinh' quà về nhà nào!\n👉👉👉 “Giọng Hát Việt Nhí” 2017 sẽ chính thức được phát sóng vào lúc 21h10 thứ 7 hằng tuần trên kênh VTV3"

    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]

    page.send(sender_id, Template.Buttons(text, buttons))

    return


def timeline(sender_id):
    text = "📣📣📣 Chương trình “Giọng Hát Việt Nhí” 2017 sẽ được phát sóng vào lúc 9h10 tối thứ 7 hằng tuần từ (ngày 12/08/2017) trên kênh VTV3"
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]

    page.send(sender_id, Template.Buttons(text, buttons))


def introduce(sender_id):
    text = "Đến hẹn lại lên, 'Giọng Hát Việt Nhí' đã trở lại và lợi hại hơn bao giờ hết. Với dàn huấn luyện viên là những nghệ sỹ trẻ nổi tiếng tài năng và sở hữu lượng fan hùng hậu nhất nhì làng giải trí Việt. Đó là cặp đôi Hương Tràm –Tiên Cookie, ca sĩ – nhạc sĩ Vũ Cát Tường, ca sĩ Soobin Hoàng Sơn. Họ hứa hẹn sẽ mang đến cho Giọng Hát Việt Nhí mùa 5 nhiều điều thú vị với độ cạnh tranh, “chặt chém” quyết liệt trên ghế nóng.\n📣📣📣 21h10 thứ 7 hằng tuần trên kênh VTV3 - Giọng Hát Việt Nhí 2017 với những bất ngờ đang chờ bạn khám phá!"
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]

    page.send(sender_id, Template.Buttons(text, buttons))
