import pymongo  # importing Python MongoDB driver
from pymongo.errors import ConnectionFailure
from post import Post

try:
    client = pymongo.MongoClient('localhost', 27017)
    print('Connected')
except ConnectionFailure as e:
    print('Error', e)

db = client.website  # accessing the website database
#  you can also use the dictionary-style access:
# db = client['website']

post = Post(
    title='Sample Post',
    content='Some engaging content',
    author='Scott Smith'
)

post.save()
