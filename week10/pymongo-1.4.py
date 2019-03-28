import pymongo  # importing Python MongoDB driver
from pymongo.errors import ConnectionFailure

try:
    client = pymongo.MongoClient('localhost', 27017)
    print('Connected')
except ConnectionFailure as e:
    print('Error', e)

db = client.website  # accessing the website database
#  you can also use the dictionary-style access:
# db = client['website']

posts_collection = db.posts

scotts_posts = posts_collection.find({'author': 'Steve Harley'})

# print(scotts_posts)
for post in scotts_posts:
    print(post['title'])