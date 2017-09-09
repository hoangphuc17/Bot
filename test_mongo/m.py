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

import datetime
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.Phuc

USER = db.USER
FAQ = db.FAQ
NEWS = db.NEWS
a = db.a


def insert_news(title, subtitle, image_url, item_url):
    new_news = {
        'title': title,
        'subtitle': subtitle,
        'image_url': image_url,
        'item_url': item_url
    }
    a.insert_one(new_news)


def get_news_elements():
    print 'day la ham get_news_elements'


insert_news("a", "a", "a", "a")
