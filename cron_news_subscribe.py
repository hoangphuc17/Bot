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


# 1. kiem tra co subscribe ko?
# 2. neu co thi gui tin tuc

def send_news(sender_id):
    element = Template.GenericElement(
        title="Sau Thụy Bình, Vũ Cát Tường lại chiêu mộ thành công ‘hoàng tử dân ca’ Tâm Hào",
        subtitle="Dự thi với ca khúc mang âm hưởng dân ca vô cùng mộc mạc nhưng cậu bé Nguyễn Tâm Hào vẫn khiến cả trường quay dậy sóng bởi tiếng hò reo, cổ vũ.",
        image_url="https://img.saostar.vn/265x149/2017/08/19/1500005/8.jpg",
        buttons=[
            Template.ButtonWeb(
                'Đọc tin', "https://saostar.vn/tv-show/sau-thuy-binh-vu-cat-tuong-lai-chieu-mo-thanh-cong-hoang-tu-dan-ca-tam-hao-1500005.html"),
            Template.ButtonPostBack('Về Home', 'home')
        ])
    page.send(sender_id, Template.Generic(element))


def news_for_subscribe():
    for user in USER.find({'subscribe_news': 'yes'}):
        send_news(user['id_user'])


news_for_subscribe()


@app.route('/', methods=['POST'])
def webhook():
    payload = request.get_data(as_text=True)
    page.handle_webhook(payload, message=message_handler,
                        postback=postback_handler)
    return "ok", 200


if __name__ == '__main__':
    app.run(host='210.211.109.211', port=5000, debug=True, threaded=True)
