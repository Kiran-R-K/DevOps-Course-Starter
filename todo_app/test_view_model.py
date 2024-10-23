from todo_app.view_model import ViewModel
from todo_app.data.models import Item, List


def get_test_lists(list_name):
  
  first_list = List(list_name)
  first_list.items.append(Item(1, "item", list_name))
  first_list.items.append(Item(2, "an item", list_name))
  first_list.items.append(Item(3, "another item", list_name))

  second_list = List("other list")
  second_list.items.append(Item(4, "other item", "other list"))

  lists = [
    first_list, second_list
  ]
  return lists

def test_view_model_done_items():
  list_name = "Done"
  test_lists = get_test_lists(list_name)
  view_model = ViewModel(test_lists)
  done_items_list = view_model.done_items_list

  assert len(done_items_list) == 1
  assert done_items_list[0].name == list_name
  assert len(done_items_list[0].items)

def test_view_model_doing_items():
  list_name = "Doing"
  test_lists = get_test_lists(list_name)
  view_model = ViewModel(test_lists)
  doing_items_list = view_model.doing_items_list

  assert len(doing_items_list) == 1
  assert doing_items_list[0].name == list_name
  assert len(doing_items_list[0].items)

def test_view_model_to_do_items():
  list_name = "To do"
  test_lists = get_test_lists(list_name)
  view_model = ViewModel(test_lists)
  to_do_items_list = view_model.to_do_items_list

  assert len(to_do_items_list) == 1
  assert to_do_items_list[0].name == list_name
  assert len(to_do_items_list[0].items)