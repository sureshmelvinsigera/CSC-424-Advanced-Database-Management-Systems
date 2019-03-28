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

post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott Smith'
}
post_2 = {
    'title': 'Anaconda Virtual Environments',
    'content': 'Use virtual environments',
    'author': 'Scott Smith'
}
post_3 = {
    'title': 'Learning Python and Amazon EC2',
    'content': 'Learn Python, it is easy',
    'author': 'Bill Smith'
}

# insert many
result = posts_collection.insert_many([post_1, post_2, post_3])

print('Multiple posts: {0}'.format(result.inserted_ids))
