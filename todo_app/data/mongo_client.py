from flask import session
from todo_app.data.models import Item, List
from bson.objectid import ObjectId
import pymongo
import os

stored_collection = None
def get_collection():
  global stored_collection
  if stored_collection is not None:
    return stored_collection
  client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"))
  db = client[os.getenv("MONGODB_DATABASE_NAME")]
  collection = db[os.getenv("MONGODB_COLLECTION_NAME")]
  stored_collection = collection
  return collection



def get_items():

  collection = get_collection()

  lists = [List("To do"), List("Doing"), List("Done")]

  db_items = collection.find()

  for item in db_items:        
    newItem = Item(str(item["_id"]), item["title"], item["status"])
    for list in lists:
      if newItem.list == list.name:
        list.items.append(newItem)

  return lists


def get_item(id):
  collection = get_collection()

  item = collection.find_one({'_id': ObjectId(id)})

  return item

def add_item(title):

  collection = get_collection()

  newItem = {
     "title": title,
     "status": "To do"
  }

  collection.insert_one(newItem)

  return
  

def save_item(item_id, list_name):

  collection = get_collection()

  collection.find_one_and_update({'_id': ObjectId(item_id)}, {'$set': {'status': list_name }})

  return
