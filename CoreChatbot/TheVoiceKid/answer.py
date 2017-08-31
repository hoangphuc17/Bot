# -*- coding: utf-8 -*-
import os
import sys
from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page

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

def add(metadata, question, answer, rank):
    check_question = FAQ.find_one({'question': question})
    if bool(check_question):
        pass
    else:
        new_question = {
            "metadata" = metadata,
            "question" = question,
            "answer" = answer,
            "rank" = rank
        }
        FAQ.insert_one(new_question)


def insert_question():
    add(["ai", "vũ cát tường"], "ai là Vũ Cát Tường?", "VCT là ...", "")
    add(["ai", "soobin"], "ai là Soobin?", "Sb là ...", "")
    add(["ai", "hương tràm"], "ai là Hương Tràm?", "HT là ...", "")


def answer(message, sender_id):
    count = 0
    for data in FAQ:
        for word in data['metadata']:
            if word in message:
                count = count + 1
            if count == len(data['metadata']):
                print 'message nam trong data nay', data['metadata']
