from flask import Flask, redirect, request, url_for, render_template
from todo_app.data import session_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index_get():
    items = session_items.get_items()
    return render_template('index.html', items=items)

@app.route('/new')
def new_post():
    title = request.values.get("title", "")
    session_items.add_item(title)
    return redirect(url_for("index_get"))
    