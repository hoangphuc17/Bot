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


def insert_new_questions():
    # insert_question(["ai", "vũ cát tường"],
    #                 "ai là Vũ Cát Tường?", "VCT là ...", "")
    # insert_question(["ai", "soobin"], "ai là Soobin?", "Sb là ...", "")
    # insert_question(["ai", "hương tràm"], "ai là Hương Tràm?", "HT là ...", "")
    insert_question(["đăng ký", "tham dự"], "để đăng ký tham gia Giọng Hát Việt Nhí ?",
                    "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn/ và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")
    insert_question(["vòng giấu mặt", "tập"], "Vòng giấu mặt có bao nhiêu tập?",
                    "Bạn thân mến! Vòng giấu mặt Giọng Hát Việt Nhí có tất cả 5 tập. Xem lại chương trình đã phát sóng trên Youtube: http://youtube.com/btcgionghatvietnhi/", "")
    insert_question(["hlv"], "HLV Giọng Hát Việt Nhí 2017 là ai?",
                    "HLV Giọng Hát Việt Nhí 2017 bao gồm ghế đôi ca sĩ Hương Tràm & nhạc sĩ Tiên Cookie, ghế đơn ca sĩ Soobin Hoàng Sơn và sự trở lại của HLV Giọng Hát Việt Nhí 2016 Vũ Cát Tường. Theo dõi chương trình và ủng hộ các đội mà bạn yêu thích nhé! ❤", "")
    insert_question(["tuyển"], "đăng ký tham gia Giọng Hát Việt Nhí ?",
                    "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn/ và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")
    print('da them new question')


def insert_new_news():
    insert_news("Sau Thụy Bình, Vũ Cát Tường lại chiêu mộ thành công ‘hoàng tử dân ca’ Tâm Hào", "Dự thi với ca khúc mang âm hưởng dân ca vô cùng mộc mạc nhưng cậu bé Nguyễn Tâm Hào vẫn khiến cả trường quay dậy sóng bởi tiếng hò reo, cổ vũ.",
                "https://img.saostar.vn/265x149/2017/08/19/1500005/8.jpg", "https://saostar.vn/tv-show/sau-thuy-binh-vu-cat-tuong-lai-chieu-mo-thanh-cong-hoang-tu-dan-ca-tam-hao-1500005.html")
    insert_news("Thể hiện hit của diva Hà Trần, ‘thiên thần nhí’ khiến Soobin, Vũ Cát Tường phải tung ‘chiêu’ hết mình chinh phục", "Lần đầu tiên ở mùa giải năm nay, Giọng hát Việt nhí 2017 đã có một thí sinh khiến các HLV phải tung hết tất cả các chiêu trò để chiêu dụ về đội của mình. ",
                "https://img.saostar.vn/265x149/2017/08/19/1500621/mg_8085.jpg", "https://saostar.vn/tv-show/hien-hit-cua-diva-ha-tran-thien-nhi-khien-soobin-vu-cat-tuong-phai-tung-chieu-het-minh-chinh-phuc-1500621.html")
    print('da them new news')


# insert_new_news()
# insert_new_questions()

def insert_node():
    first_level("1", ["2", "3"], ["tổ chức"])
    final_level("2", "1", ["ở đâu"], "38 Nguyễn Du")
    final_level("3", "1", ["ai"], "Cat Tien Sa")


insert_node()
