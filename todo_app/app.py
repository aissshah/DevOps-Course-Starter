from flask import Flask, render_template, request, redirect

from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, add_item, changeList_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)

@app.route('/create-item', methods=['POST'])
def create_item():
    todo = request.form.get('todo')
    add_item(todo)
    return redirect('/')

@app.route('/change-item-list/<list>/<itemID>', methods=['GET', 'PUT'])
def change_item_list(list, itemID):
    changeList_item(list, itemID)
    return redirect('/')