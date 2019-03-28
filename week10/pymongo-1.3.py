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

single_post = {
    'title': "Java 101",
    "content": "Welcome to Java programming",
    "author": "Steve Harley"
}

# inserting the single post
result = posts_collection.insert_one(single_post)
