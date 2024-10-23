from flask import Flask, redirect, request, url_for, render_template
from todo_app.data import mongo_client
from todo_app.view_model import ViewModel

from todo_app.flask_config import Config

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config())


  @app.route('/')
  def index_get():
      lists = mongo_client.get_items()
      lists_view_model =  ViewModel(lists)
      return render_template('index.html', view_model=lists_view_model)

  @app.route('/new')
  def new_post():
      title = request.values.get("title", "")
      mongo_client.add_item(title)
      return redirect(url_for("index_get"))

  @app.route('/update')
  def update_item_list():
      item_id = request.values.get("item_id", "")
      list_name = request.values.get("list_name", "")

      mongo_client.save_item(item_id, list_name)
      return redirect(url_for("index_get"))
  
  return app
    