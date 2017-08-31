# -*- coding: utf-8 -*-

from pymongo import MongoClient
import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
            "metadata": metadata,
            "question": question,
            "answer": answer,
            "rank": rank
        }
        FAQ.insert_one(new_question)


def insert_new_questions():
    insert_question(["ai", "vũ cát tường"], "ai là Vũ Cát Tường?", "VCT là ...", "")
    insert_question(["ai", "soobin"], "ai là Soobin?", "Sb là ...", "")
    insert_question(["ai", "hương tràm"], "ai là Hương Tràm?", "HT là ...", "")
    insert_question(["đăng ký", "nhí"], "Làm sao để đăng ký tham gia Giọng Hát Việt Nhí ?",
                    "Để đăng ký tham gia chương trình bạn vui lòng truy cập vào website chính thức Giọng Hát Việt Nhí / The Voice Kids Viet Nam: http://gionghatvietnhi.com.vn/ và theo dõi Fanpage chính thức Giọng Hát Việt Nhí để cập nhật thông tin mới nhất bạn nhé!", "")


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


sender_id = 123
message = [
    "ai là Vũ Cát Tường ?",
    "làm sao đăng ký GHV nhí"
]

insert_new_questions()
answer(message[1], sender_id)
