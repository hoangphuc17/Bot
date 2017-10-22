# -*- coding: utf-8 -*-
import os
import sys
import threading
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page
import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page
from CoreChatbot.TheVoiceKid.database import *


import datetime
import time
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
url = "http://210.211.109.211/weqbfyretnccbsaf/"


def broadcast_message(sender_id, text):
    buttons = [
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))


def broadcast_message_link_button(sender_id, text, link):
    buttons = [
        Template.ButtonWeb('👉 Click để xem', link),
        Template.ButtonPostBack("Home", "home")
    ]
    page.send(sender_id, Template.Buttons(text, buttons))


def broadcast_image(sender_id, image_name):
    page.send(sender_id, Attachment.Image(url + image_name))


def broadcast_video(sender_id, video_name):
    page.send(sender_id, Attachment.Video(url + video_name))


def broadcast(list_user_broadcast):
    for id_user in list_user_broadcast:
        broadcast_message_link_button(id_user, "Giọng Hát Việt Nhí tập 10 với rất nhiều tiết mục vô cùng hấp dẫn hiện đang được livestream trên fanpage của Saostar.vn. Cùng đón xem và ủng hộ cho giọng ca mà mình yêu thích",
                                      "https://www.facebook.com/gionghatvietnhi/videos/1587288074703919/?notif_id=1508596247236181&notif_t=live_video_explicit&ref=notif")
        print('Co ', len(list_user_broadcast), ' user')
        print('Da gui broadcast cho user thu:',
              list_user_broadcast.index(id_user))


# get user from database USER
list_user = []
for user in USER.find():
    list_user.append(user['id_user'])


# chia user thanh n groups
def partition(lst, n):
    division = len(lst) / n
    return [lst[round(division * i):round(division * (i + 1))]
            for i in range(n)]


list_thread = []
list_group_user = partition(list_user, 100)

for group in list_group_user:
    thread = threading.Thread(target=broadcast, args=(group,))
    list_thread.append(thread)

second = time.time()

for t in list_thread:
    t.start()

for t in list_thread:
    t.join()

print('done in: ', time.time() - second)


# t = time.time()

# t1 = threading.Thread(target=broadcast, args=(list_group_user[0],))
# t2 = threading.Thread(target=broadcast, args=(list_group_user[1],))
# t3 = threading.Thread(target=broadcast, args=(list_group_user[2],))
# t4 = threading.Thread(target=broadcast, args=(list_group_user[3],))
# t5 = threading.Thread(target=broadcast, args=(list_group_user[4],))
# t6 = threading.Thread(target=broadcast, args=(list_group_user[5],))
# t7 = threading.Thread(target=broadcast, args=(list_group_user[6],))
# t8 = threading.Thread(target=broadcast, args=(list_group_user[7],))
# t9 = threading.Thread(target=broadcast, args=(list_group_user[8],))
# t10 = threading.Thread(target=broadcast, args=(list_group_user[9],))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()
# t9.start()
# t10.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
# t7.join()
# t8.join()
# t9.join()
# t10.join()

# print('doin in: ', time.time() - t)
