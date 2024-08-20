from flask import Flask,render_template_string,jsonify, request

app = Flask(__name__)

html_template = '<h1> Hello World </h1>'

# In-Memory Storage for the key-value pairs
store = {}

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/store/<key>', methods=['GET'])
def get_value(key):
    value = store.get(key)
    if value is None:
        return jsonify("No Key Value Store found"), 404
    return jsonify({key: value})

@app.route('/store/<key>', methods=['PUT'])
def set_value(key):
    value = request.json.get('value')
    if value is None:
        return jsonify({"Error: No value provided"}), 400
    store[key] = value
    return jsonify({key:value}), 201

    
@app.route('/store/<key>', methods=['DELETE'])
def delete_value(key):
    if key in store:
        del store[key]
        return jsonify({"Key has been deleted"}),200
    return jsonify({"Key not found"})

if __name__ == '__main__':
    app.run(port=8000)