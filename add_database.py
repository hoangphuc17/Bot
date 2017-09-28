# -*- coding: utf-8 -*-
import os
import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
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


# def insert_question(metadata, question, answer, rank):
#     check_question = FAQ.find_one({'question': question})
#     if bool(check_question):
#         pass
#     else:
#         new_question = {
#             "metadata": metadata,
#             "question": question,
#             "answer": answer,
#             "rank": rank
#         }
#         FAQ.insert_one(new_question)


def insert_new_questions():
    # insert_question(["ai", "vũ cát tường"],
    #                 "ai là Vũ Cát Tường?", "VCT là ...", "")
    # insert_question(["ai", "soobin"], "ai là Soobin?", "Sb là ...", "")
    # insert_question(["ai", "hương tràm"], "ai là Hương Tràm?", "HT là ...", "")
    # insert_question(["đăng ký", "tham dự"], "để đăng ký tham gia Giọng Hát Việt Nhí ?",
    #                 "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn/ và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")
    # insert_question(["vòng giấu mặt", "tập"], "Vòng giấu mặt có bao nhiêu tập?",
    #                 "Bạn thân mến! Vòng giấu mặt Giọng Hát Việt Nhí có tất cả 5 tập. Xem lại chương trình đã phát sóng trên Youtube: http://youtube.com/btcgionghatvietnhi/", "")
    # insert_question(["hlv"], "HLV Giọng Hát Việt Nhí 2017 là ai?",
    #                 "HLV Giọng Hát Việt Nhí 2017 bao gồm ghế đôi ca sĩ Hương Tràm & nhạc sĩ Tiên Cookie, ghế đơn ca sĩ Soobin Hoàng Sơn và sự trở lại của HLV Giọng Hát Việt Nhí 2016 Vũ Cát Tường. Theo dõi chương trình và ủng hộ các đội mà bạn yêu thích nhé! ❤", "")
    # insert_question(["tuyển"], "đăng ký tham gia Giọng Hát Việt Nhí ?",
    #                 "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn/ và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")

    insert_question(["đăng ký", "tuyển sinh"], "Mình muốn tham gia Giọng Hát Việt Nhí năm sau thì đăng ký ở đâu ạ?",
                    "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")
    insert_question(["đăng ký", "tham gia"], "Mình muốn tham gia Giọng Hát Việt Nhí năm sau thì đăng ký ở đâu ạ?",
                    "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")
    insert_question(["đăng ký", "thi"], "Mình muốn tham gia Giọng Hát Việt Nhí năm sau thì đăng ký ở đâu ạ?",
                    "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")

    insert_question(["phát sóng", "tuần này"], "Tuần này có phát sóng Giọng Hát Việt Nhí 2017 không Ad?",
                    "Bạn thân yêu ơi Giọng Hát Việt Nhí 2017 sẽ được phát sóng vào 21h thứ bảy trên kênh VTV3. Bạn nhớ đón xem nha!", "")
    insert_question(["quán quân"], "Quán quân năm nay là ai vậy ạ?",
                    "Tham gia dự đoán quán quân Giọng Hát Việt Nhí tại Chatbot bạn nhé!", "")
    insert_question(["hlv", "giọng hát việt nhí"], "HLV Giọng Hát Việt Nhí 2017 là ai?",
                    "HLV Giọng Hát Việt Nhí 2017 bao gồm ghế đôi ca sĩ Hương Tràm & nhạc sĩ Tiên Cookie, ghế đơn ca sĩ Soobin Hoàng Sơn và sự trở lại của HLV Giọng Hát Việt Nhí 2016 Vũ Cát Tường. Theo dõi chương trình và ủng hộ các đội mà bạn yêu thích nhé! ❤", "")
    insert_question(["lịch phát sóng"], "Em muốn hỏi lịch phát sóng Giọng Hát Việt nhí",
                    "Giọng Hát Việt Nhí 2017 được phát sóng vào lúc 21 giờ thứ Bảy hàng tuần trên kênh VTV3 bạn nhé! ❤", "")
    insert_question(["bình chọn"], "Làm sao để bình chọn cho thí sinh",
                    "Hệ thống bình chọn chỉ hoạt động để bình chọn chiếc vé may mắn cho thí sinh quay trở lại đêm chung kết và bình chọn cho quán quân chương trình Giọng Hát Việt Nhí 2017 trong đêm chung kết được mở từ ngày 19/11 - 25/11/2017", "")
    insert_question(["hậu trường"], "Admin có quay cảnh hậu trường không? ",
                    "Để xem lại những khoảnh khắc hậu trường vui nhộn bạn nhớ subcribe kênh VIVA Shows: http://bit.ly/vivashows nhé!", "")
    insert_question(["full"], "Tại sao the voice kids không có bản full trên youtube",
                    "Vì lý do bản quyền The Voice Kids không cho phép công bố bản Full trên Youtube nên chúng tôi rất tiếc vì sự bất tiện này. Tuy nhiên, khán giả có thể dễ dàng theo dõi từ thí sính mà mình yêu thích một cách dễ dàng mà không tốn quá nhiều thời gian.", "")
    insert_question(["tuyển"], "Bây giờ còn đăng ký được nữa không?",
                    "Tuyển sinh Giọng Hát Việt Nhí 2018 sẽ được mở ngay sau khi Chung Kết Giọng Hát Việt Nhí 2017 kết thúc. Các bạn theo dõi Fanpage để cập nhật thông tin sớm nhất nhé!", "")
    insert_question(["trực tiếp"], "Năm nay các vòng Liveshow có phát trực tiếp không?",
                    "Liveshow chung kết Giọng Hát Việt Nhí sẽ được phát sóng trực tiếp trên kênh VTV3 vào ngày 25/11/2017 các bạn nhé!", "")
    insert_question(["bao nhiêu", "tập", "thí sinh"], "Một tập gồm mấy thí sinh vậy Ad?",
                    "Bạn ơi bạn à! Bạn muốn hỏi tập mấy nà? Ahihi Mình đùa đấy!! Tùy theo mỗi tập sẽ có số lượng thí sinh khác nhau. Bạn nhớ xem chương trình vào 21h tối Thứ Bảy Hàng tuần trên VTV3 để nắm thông tin nhé!", "")
    insert_question(["phát lại"], "GHVN có phát sóng lại không Ad?",
                    "Giọng Hát Việt Nhí 2017 sẽ được phát sóng vào lúc 21h thứ bảy hàng tuần trên VTV3 và được phát lại vào lúc 14h30 thứ hai tuần tiếp theo cũng trên kênh VTV3 nhé bạn dấu yêu.", "")
    insert_question(["web"], "Website Giọng Hát Việt Nhí là gì vậy?",
                    "Webssite chính thức của chương trình Giọng Hát Việt Nhí/The Voice Kids Việt Nam truy cập vào link: http://gionghatvietnhi.com.vn", "")
    insert_question(["hlv", "năm sau"], "Vũ Cát Tường/Soobin Hoàng Sơn/Hương Tràm/Tiên Cookie có làm HLV năm sau nữa không?",
                    "Cám ơn @user đã quan tâm và theo dõi chương trình. Thông tin về 'ghế nóng' năm sau vẫn là một 'ẩn số'. Theo dõi Fanpage để cập nhật tin tức mới nhất 'nóng hổi nhất' bạn nhé! ;)", "")
    insert_question(["tập mới"], "Cho mình xin link tập @mới nha",
                    "Bạn thân mến! Để xem lại tập vừa phát sóng hãy trở lại phím 'Home' và nhấp vào 'Xem lại tập phát sóng' trên kênh Youtube chính thức của chương trình bạn nhé!", "")
    insert_question(["tuổi", "đăng ký"], "Bao nhiêu tuổi thì được tham gia chương trình vậy ạ?",
                    "Độ tuổi đăng ký tham gia chương trình Giọng Hát Việt Nhí là từ 5 tuổi - 15 tuổi bạn nhé!", "")
    insert_question(["tuổi", "tham gia"], "Bao nhiêu tuổi thì được tham gia chương trình vậy ạ?",
                    "Độ tuổi đăng ký tham gia chương trình Giọng Hát Việt Nhí là từ 5 tuổi - 15 tuổi bạn nhé!", "")
    insert_question(["đăng ký", "thử giọng"], "Tham gia thử giọng ở đâu vậy ad?",
                    "Theo dõi Fanpage để cập nhật thông tin đăng  ký và địa điểm ghi hình sớm nhất bạn nhé!", "")
    insert_question(["năm sau", "tổ chức"], "Năm sau còn tổ chức nữa không ạ?",
                    "Bạn 'đáng yêu' ơi! Giọng Hát Việt Nhí đã trải qua 5 mùa và sẽ tiếp tục đồng hành cùng khán giả yêu mến chương trình vào những năm tiếp theo bạn nhé!", "")
    insert_question(["tsổ chức", "ở đâu"], "Giọng Hát Việt Nhí tổ chức ở đâu vậy ạ?",
                    "Giọng Hát Việt Nhí được tổ chức ghi hình tại TP. HCM bạn nhé! Để biết thêm thông tin địa điểm ghi hình chương trình bạn vui lòng theo dõi Fanpage thường xuyên nhé!", "")
    insert_question(["giấu mặt"], "Vòng giấu mặt có bao nhiêu tập?",
                    "Vòng giấu mặt thường có 4-5 tập bạn nhé!", "")
    insert_question(["xem lại"], "Làm sao xem lại GHVN được ạ?",
                    "Bạn có thể xem phát sóng lại Giọng Hát Việt Nhí vào lúc 14h30 thứ 2 tuần tiếp theo trên VTV3 hoặc vào Youtube chính thức của chương trình để xem lại những tiết mục yêu thích bạn nhé!", "")

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
    first_level("1", ["tổ chức", "diễn ra"])
    final_level("2", "1", ["ở đâu"], "38 Nguyễn Du")
    final_level("3", "1", ["ai"], "Cat Tien Sa")


# insert_node()

insert_new_questions()
