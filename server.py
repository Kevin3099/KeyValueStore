from flask import Flask,render_template_string

app = Flask(__name__)

html_template = '>h1> Hello World </h1>'

# In-Memory Storage for the key-value pairs
store = {}

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/store/<key>', methods=['GET'])
def get_value(key):
    return render_template_string(html_template)

@app.route('/store/<key>', methods=['PUT'])
def get_value(key):
    return render_template_string(html_template)

@app.route('/store/<key>', methods=['DELETE'])
def get_value(key):
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(port=8000)