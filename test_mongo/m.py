from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.pymongo_test

# insert documents
posts = db.posts
post_data = {
    'id': 1,
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Jame',
    'published': datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
}
# print('One post: {0}'.format(result.inserted_id))

# find one (retrieve data)
# bills_post = posts.find_one({'author': 'Jack'})
# print(bills_post)

posts.insert_one(post_data)

posts.update_one(
    {'id': 1},
    {'$set': {'author': 'King'}
     }
)

# posts.delete_many({'author': 'Jame'})
# result = posts.insert_one(post_data)
