# stationary_store.py

from bottle import route, post, run, template, redirect, request
import database

# Initialize the database
database.initialize_database()

@route("/")
def get_index():
    redirect("/items")

@route("/items")
def get_items():
    items = database.get_all_items()
    return template("items.tpl", items=items)

@route("/items/add")
def get_add_item():
    return template("add_item.tpl")

@post("/items/add")
def post_add_item():
    title = request.forms.get("title")
    author = request.forms.get("author")
    genre = request.forms.get("genre")
    database.add_item(title, author, genre)
    redirect("/items")

@route("/items/<item_id>")
def get_item_details(item_id):
    item = database.get_item_details(item_id)
    return template("item_details.tpl", item=item)

@route("/items/<item_id>/update")
def get_update_item(item_id):
    item = database.get_item_details(item_id)
    return template("update_item.tpl", item=item)

@post("/items/<item_id>/update")
def post_update_item(item_id):
    title = request.forms.get("title")
    author = request.forms.get("author")
    genre = request.forms.get("genre")
    database.update_item(item_id, title, author, genre)
    redirect("/items")

@route("/items/<item_id>/delete")
def get_delete_item(item_id):
    database.delete_item(item_id)
    redirect("/items")

run(host='localhost', port=8080)
