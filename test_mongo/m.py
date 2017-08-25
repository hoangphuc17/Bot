from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.pymongo_test

# # define a document
#
#
# class Post(Document):
#     title = StringField(required=True, max_length=200)
#     content = StringField(required=True)
#     author = StringField(required=True, max_length=50)
#     published = DateTimeField(default=datetime.datetime.now)
#
#
# # save Document
# post_1 = Post(
#     title='Sample Post',
#     content='Some engaging content',
#     author='Scott'
# )
# post_1.save()       # This will perform an insert
# print(post_1.title)
# post_1.title = 'A Better Post Title'
# post_1.save()       # This will perform an atomic edit on "title"
# print(post_1.title)


# insert documents
posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Jack',
    'published': datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))

# find one (retrieve data)
bills_post = posts.find_one({'author': 'Jack'})
print(bills_post)

print 'now: ', datetime.datetime.now()
