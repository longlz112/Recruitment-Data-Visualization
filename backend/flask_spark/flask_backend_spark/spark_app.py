from flask import Flask, request, jsonify
from flask_cors import CORS
import sys

sys.path.append("..")
from count_keyword import get_count_keyword
from count_experience import get_count_exp
from count_degree import get_count_degree
from count_job_area import get_count_area
from count_salary import get_count_salary
from technique_process import count_by_keyword

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
    if data_type == 'exp':
        json_data = get_count_exp(keyword)
    elif data_type == 'area':
        json_data = get_count_area(keyword)
    elif data_type == 'degree':
        json_data = get_count_degree(keyword)
    elif data_type == 'salary':
        json_data = get_count_salary(keyword)
    elif data_type == 'technique':
        json_data = count_by_keyword(keyword)

    return json_data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
