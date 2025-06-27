from flask import Flask,render_template,request,jsonify

app = Flask (__name__)


items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route("/")
def home():
  return "Welcome to the todo app"

#get : retrieve all the data

@app.route('/items',methods=['GET'] )
def get_items():
  return jsonify(items)

#get : Retrieve a specific item by id 

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
  item = next((item for item in items if item['id']==item_id  ),None)
  if item is None:
    return jsonify({"error":"item not found"})
  return jsonify(item)
  
## Post :create a new task- API
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name":request.json['name'],
        "description":request.json["description"]


    }
    items.append(new_item)
    return jsonify(new_item)



if __name__ == "__main__":
  app.run(debug=True)