from flask import Flask,send_from_directory,jsonify, request
# importing lock function to handle multiple clients at once
from threading import Lock

app = Flask(__name__)

html_template = '<h1> Hello World </h1>'

# In-Memory Storage for the key-value pairs
store = {}
lock = Lock()

# Default landing page
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Get method for key value pairs
@app.route('/store/<key>', methods=['GET'])
def get_value(key):
        value = store.get(key)
        if value is None:
            return jsonify("No Key Value found"), 404
        return jsonify({key: value})

# Set method for key value pair
@app.route('/store/<key>', methods=['PUT'])
def set_value(key):
        value = request.json.get('value') #used insead of request.json['value'], handles errors better
        if value is None:
         return jsonify({"Error: No value provided"}), 400
        with lock:
            # If time allows it add better more efficient way of doing this
            if value in store.values():
              return jsonify({"Error: Duplicate value found"}), 409
            store[key] = value
        return jsonify({key:value}), 201

# De;ete method for key value pairs    
@app.route('/store/<key>', methods=['DELETE'])
def delete_value(key):
    with lock:
        if key in store:
         del store[key]
         return jsonify({"Key has been deleted"}),200
    return jsonify({"Key not found"}), 404

if __name__ == '__main__':
    app.run(port=8000)