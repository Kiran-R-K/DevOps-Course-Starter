class Item:
  def __init__(self, id, title, list):
    self.id = id
    self.title = title
    self.list = list

class List:
  def __init__(self, name):
    self.name = name
    self.items = []    
