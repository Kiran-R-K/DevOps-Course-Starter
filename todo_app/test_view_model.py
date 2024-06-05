from todo_app.view_model import ViewModel
from todo_app.data.trello_items import Item, List

def get_test_items(list_name):
  items = [
    Item(1, "item", list_name),
    Item(2, "an item", list_name),
    Item(3, "another item", list_name),
  ]
  return items

def get_test_lists(list_name):
  lists = [
    List(1, list_name, get_test_items(list_name)),
    List(2, "other list", Item(4, "other item", "other list"))
  ]
  return lists

def test_view_model_done_items():
  list_name = "Done"
  test_lists = get_test_lists(list_name)
  view_model = ViewModel(test_lists)
  done_items = view_model.done_items

  assert len(done_items) == 1
  assert done_items[0].name == list_name
  assert len(done_items[0].items)

def test_view_model_doing_items():
  list_name = "Doing"
  test_lists = get_test_lists(list_name)
  view_model = ViewModel(test_lists)
  doing_items = view_model.doing_items

  assert len(doing_items) == 1
  assert doing_items[0].name == list_name
  assert len(doing_items[0].items)

def test_view_model_to_do_items():
  list_name = "To do"
  test_lists = get_test_lists(list_name)
  view_model = ViewModel(test_lists)
  to_do_items = view_model.to_do_items

  assert len(to_do_items) == 1
  assert to_do_items[0].name == list_name
  assert len(to_do_items[0].items)