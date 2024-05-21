from flask import Flask, request, jsonify
from flask_cors import CORS
from read_data.read_data import get_count_keyword, get_count_data, get_skill

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():

    return 'hello'


@app.route('/getkey', methods=['POST'])
def get_key():
    global json_data
    data = request.get_json()
    keyword = data.get('keyword')
    if keyword == 'all':
        json_data = get_count_keyword()
    else:
        json_data = jsonify({'code':0, 'status':400})

    return json_data


@app.route('/getdata', methods=['POST'])
def get_data():
    global json_data
    data = request.get_json()
    keyword = data.get('keyword')
    data_type = data.get('type')
    if data_type == 'technique':
        json_data = get_skill(keyword)
    else:
        json_data = get_count_data(keyword,data_type)

    return json_data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)