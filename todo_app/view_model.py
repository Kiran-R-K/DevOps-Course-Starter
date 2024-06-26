class ViewModel:
  def __init__(self, lists):
    self._lists = lists

  @property
  def lists(self):
    return self._lists
  
  @property
  def done_items_list(self):
    return [x for x in self._lists if x.name == 'Done']

  @property
  def doing_items_list(self):
    return [x for x in self._lists if x.name == 'Doing']
  
  @property
  def to_do_items_list(self):
    return [x for x in self._lists if x.name == 'To do']