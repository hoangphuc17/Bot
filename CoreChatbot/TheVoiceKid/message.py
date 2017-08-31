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


# step 1: insert cau hoi va cau tra loi
# step 2: viet dieu kien trong file app.py
# step 3: viet minigame va hoan thanh cong viec
# step 4: xem lai vu submission cua fb
# step 5: gap thay


def insert_new_questions():
    insert_question(["ai", "vũ cát tường"], "ai là Vũ Cát Tường?", "VCT là ...", "")
    insert_question(["ai", "soobin"], "ai là Soobin?", "Sb là ...", "")
    insert_question(["ai", "hương tràm"], "ai là Hương Tràm?", "HT là ...", "")


def answer(message, sender_id):
    for data in FAQ.find():
        count = 0
        metadata = data['metadata']
        print metadata
        for word in metadata:
            if word in message.lower():
                count = count + 1
            else:
                break
        if count == len(data['metadata']):
            print 'cau tra loi cho cau hoi', data['question'], 'la:'
            print data['answer']
