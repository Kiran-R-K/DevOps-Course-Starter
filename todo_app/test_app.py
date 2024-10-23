import os
import pytest
import mongomock
import pymongo

from dotenv import load_dotenv, find_dotenv
from todo_app import app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def test_index_page(client):
  mongo_client = pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_STRING"))
  
  db = mongo_client[os.getenv("MONGODB_DATABASE_NAME")]
  
  collection = db[os.getenv("MONGODB_COLLECTION_NAME")]

  item = {
     "title": "an item",
     "status": "To do"
  }

  collection.insert_one(item)

  response = client.get('/')
  
  assert response.status_code == 200
  assert "an item" in response.data.decode()
