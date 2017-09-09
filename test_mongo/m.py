# -*- coding: utf-8 -*-
import os
import sys
# sys.path.insert(0, '/Users/mac/Desktop/Bot/ApiMessenger')
# # from ApiMessenger import Attachment, Template
# from ApiMessenger.attachment import *
# from ApiMessenger.template import *
# from ApiMessenger.payload import QuickReply
# from ApiMessenger.fbmq import Page
#
# import CoreChatbot.Preparation.messenger
# from CoreChatbot.Preparation.config import CONFIG
# from CoreChatbot.Preparation.fbpage import page


from pymongo import MongoClient
client = MongoClient('cb.saostar.vn', 27017)
db = client.Phuc
a = db.a


def insert_news(title, subtitle, image_url, item_url):
    new_news = {
        'title': title,
        'subtitle': subtitle,
        'image_url': image_url,
        'item_url': item_url
    }
    a.insert_one(new_news)


insert_news("a", "a", "a", "a")
