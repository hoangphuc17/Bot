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

from CoreChatbot.TheVoiceKid.answer import *


add_question(["ai", "vũ cát tường"], "ai là Vũ Cát Tường?", "VCT là ...", "")
add_question(["ai", "soobin"], "ai là Soobin?", "Sb là ...", "")
add_question(["ai", "hương tràm"], "ai là Hương Tràm?", "HT là ...", "")
