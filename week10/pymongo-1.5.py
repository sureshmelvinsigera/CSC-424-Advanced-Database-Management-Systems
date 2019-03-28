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

posts = posts_collection.find()

query = {"title": "Python and MongoDB"}
update_query = {"$set": {"title": "Python and MongoDB for developers"}}

posts_collection.update_one(query, update_query)

for post in posts:
    print(post['title'])
