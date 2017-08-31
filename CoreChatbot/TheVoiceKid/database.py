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


def insert_question(metadata, question, answer, rank):
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
