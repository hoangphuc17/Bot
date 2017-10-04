# -*- coding: utf-8 -*-
import os
import sys

from ApiMessenger import Attachment, Template
from ApiMessenger.payload import QuickReply
from ApiMessenger.fbmq import Page

import CoreChatbot.Preparation.messenger
from CoreChatbot.Preparation.config import CONFIG
from CoreChatbot.Preparation.fbpage import page
# from CoreChatbot.TheVoiceKid.database import *

from flask import Flask, render_template, url_for, request, session, redirect, jsonify, flash
from flask_pymongo import PyMongo, ObjectId
import bcrypt
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'Phuc'
app.config['MONGO_URI'] = 'mongodb://cb.saostar.vn:27017/Phuc'
mongo = PyMongo(app)

UPLOAD_FOLDER = '/home/hoangphuc/Bot_Pictures'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# USER_CMS authentication


@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    else:
        return 'You are not logged.'


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.USER_CMS
    login_user = users.find_one({'username': request.form['username']})
    if login_user:
        if login_user['password'] == request.form['password']:
            user_activation_key = bcrypt.hashpw(login_user['username'].encode(
                'utf-8'), bcrypt.gensalt()).decode('utf-8')
            users.update_one(
                {'username': login_user['username']},
                {'$set': {'user_activation_key': user_activation_key}}
            )
            return user_activation_key
        else:
            return 'False'
    else:
        return 'False'


@app.route('/logout/<string:username>', methods=['POST'])
def logout(username):
    # xoa user_activation_key
    logged_out = ''
    users = mongo.db.USER_CMS
    login_user = users.find_one({'username': username})
    if login_user:
        users.update_one(
            {'username': login_user['username']},
            {'$set': {'user_activation_key': ''}}
        )
        logged_out = 'True'
    else:
        logged_out = "False"
    # return 'Removed user_activation_key'
    return logged_out


@app.route('/register/<string:username>', methods=['POST', 'GET'])
def register(username):
    if username == 'admin':
        register = 'False'
        if request.method == 'POST':
            users = mongo.db.USER_CMS
            group = mongo.db.GROUP_USER_CMS
            existing_user = users.find_one(
                {'username': request.form['username']})
            if existing_user is None:
                users.insert({
                    'username': request.form['username'],
                    'password': request.form['password'],
                    'user_activation_key': '',
                    'group': request.form['group']
                })
                register = 'True'
                group.insert({
                    'username': request.form['username'],
                    'group': request.form['group']
                })
            else:
                return 'That username already exists!'
        return register
    else:
        return 'Admin moi duoc dang ky user'

# USER


@app.route('/user/get', methods=['GET'])
def get_all_user():
    user = mongo.db.USER
    output = []
    for user in user.find():
        output.append({
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'id_user': user['id_user'],
            'HLV_da_binh_chon': user['HLV_da_binh_chon'],
            'subscribe_news': user['subscribe_news'],
            'message': user['message']
        })
    return jsonify({'result': output})


# NEWS
@app.route('/news/get', methods=['GET'])
def get_all_news():
    news = mongo.db.NEWS
    output = []
    for news in news.find():
        output.append({
            'id_news': str(news['_id']),
            'title': news['title'],
            'subtitle': news['subtitle'],
            'image_url': news['image_url'],
            'item_url': news['item_url']
        })
    return jsonify({'result': output})


@app.route('/news/insert', methods=['POST'])
def add_news():
    news = mongo.db.NEWS
    title = request.json['title']
    subtitle = request.json['subtitle']
    image_url = request.json['image_url']
    item_url = request.json['item_url']

    check_news = news.find_one({'item_url': item_url})
    if bool(check_news):
        return "This news already exists in database!"
    else:
        insert_news = news.insert({
            'title': title,
            'subtitle': subtitle,
            'image_url': image_url,
            'item_url': item_url
        })
        new_news = news.find_one({'_id': insert_news})
        output = {
            'id_news': str(new_news['_id']),
            'title': new_news['title'],
            'subtitle': new_news['subtitle'],
            'image_url': new_news['image_url'],
            'item_url': new_news['item_url']
        }
        return jsonify({'result': output})


@app.route('/news/update', methods=['PUT'])
def update_news():
    news = mongo.db.NEWS

    title = request.json['title']
    subtitle = request.json['subtitle']
    image_url = request.json['image_url']
    item_url = request.json['item_url']

    updated_news = news.update_one(
        {news['item_url']: item_url},
        {'$set': {
            news['title']: title,
            news['subtitle']: subtitle,
            news['image_url']: image_url,
            news['item_url']: item_url
        }}
    )

    new_news = news.find_one({'_id': updated_news})

    output = {
        'id_news': str(new_news['_id']),
        'title': new_news['title'],
        'subtitle': new_news['subtitle'],
        'image_url': new_news['image_url'],
        'item_url': new_news['item_url']
    }

    return jsonify({'result': output})


@app.route('/news/update', methods=['DELETE'])
def delete_news():
    news = mongo.db.NEWS
    title = request.json['title']
    subtitle = request.json['subtitle']
    image_url = request.json['image_url']
    item_url = request.json['item_url']
    news.delete_one({'item_url': item_url})
    return 'Deleted news'


# BROADCAST API: message, image, video
@app.route('/broadcast/message', methods=['POST'])
def broadcast_message():
    for user in USER.find():
        message = request.json['message']
        buttons = [
            Template.ButtonPostBack("Home", "home")
        ]
        page.send(user['id_user'], Template.Buttons(message, buttons))
        return 'Sent a broadcast message'


@app.route('/broadcast/image', methods=['POST'])
def broadcast_image():
    for user in USER.find():
        image_url = "http://210.211.109.211/weqbfyretnccbsaf/" + \
            request.json['image']
        page.send(user['id_user'], Attachment.Image(image_url))
        return 'Sent a broadcast image'


@app.route('/broadcast/video', methods=['POST'])
def broadcast_video():
    for user in USER.find():
        video_url = "http://210.211.109.211/weqbfyretnccbsaf/" + \
            request.json['video']
        page.send(user['id_user'], Attachment.Video(video_url))
        return 'Sent a broadcast video'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/broadcast/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             # return redirect(request.url)
#             return 'file not in format'
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             # return redirect(request.url)
#             return 'No selected file'
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             # return redirect(url_for('uploaded_file', filename=filename))
#             return ('http://210.211.109.211/weqbfyretnccbsaf/' + filename)
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


# @app.route('/broadcast/upload', methods=['GET', 'POST'])
# def broadcast_upload():
#     if request.method == 'POST':
#         file = request.files['file']
#         extension = os.path.splitext(file.filename)[1]
#         f_name = str(uuid.uuid4()) + extension
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
#         return json.dumps({'filename': f_name})


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='210.211.109.211', port=3000, debug=True, threaded=True)


# tieng anh tieng viet thong nhat
# json or form
# check user_activation_key trong broadcast
