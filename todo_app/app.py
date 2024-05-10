from flask import Flask, redirect, request, url_for, render_template
from todo_app.data import trello_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index_get():
    lists = trello_items.get_items()
    return render_template('index.html', lists=lists)

@app.route('/new')
def new_post():
    title = request.values.get("title", "")
    trello_items.add_item(title)
    return redirect(url_for("index_get"))

@app.route('/update')
def update_item_list():
    item_id = request.values.get("item_id", "")
    list_id = request.values.get("list_id", "")

    trello_items.save_item(item_id, list_id)
    return redirect(url_for("index_get"))
    