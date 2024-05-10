from flask import session
import requests
import os
import json

class Item:
   def __init__(self, id, title, list):
      self.id = id
      self.title = title
      self.list = list

class List:
   def __init__(self, id, name, items):
      self.id = id
      self.name = name
      self.items = items

def get_items():
  request_url = 'https://api.trello.com/1/boards/{id}/lists?key={key}&token={token}&cards=open&card_fields=id,name'
  response = requests.get(request_url.format(id=os.getenv('TRELLO_BOARD_ID'), key=os.getenv('TRELLO_API_KEY'), token=os.getenv('TRELLO_API_TOKEN')))
  
  json_response = json.loads(response.text)

  lists = []

  for json_list in json_response:
     items = []
     for item in json_list['cards']:
           item = Item(item['id'], item['name'], json_list['id'])
           items.append(item)
     lists.append(List(json_list['id'], json_list['name'], items))
        
  return lists

def get_item(id):
  request_url = 'https://api.trello.com/1/cards/{id}?key={key}&token={token}'
  response = requests.get(request_url.format(id=id, key=os.getenv('TRELLO_API_KEY'), token=os.getenv('TRELLO_API_TOKEN')))
  
  json_response = json.loads(response.text)

  item = Item(json_response['id'], json_response['name'], json_response['idList'])
  
  return item

def add_item(title):
  request_url = 'https://api.trello.com/1/cards?idList={id}&key={key}&token={token}&name={name}'
  requests.post(request_url.format(id=os.getenv('TRELLO_TO_DO_LIST_ID'), key=os.getenv('TRELLO_API_KEY'), token=os.getenv('TRELLO_API_TOKEN'), name=title))
  return

def save_item(item_id, list_id):
    request_url = 'https://api.trello.com/1/cards/{id}?key={key}&token={token}&idList={list_id}'
    requests.put(request_url.format(id = item_id, key=os.getenv('TRELLO_API_KEY'), token=os.getenv('TRELLO_API_TOKEN'), list_id = list_id))
    return
