from pymongo import Connection

connection = Connection()
db = connection['comfortly']

def save(collection, data):
    col = db[collection]
    col.insert(data)