import os
from flask import Flask, request, jsonify
from tcms_api import TCMS

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Replace with your Kiwi TCMS API token and URL
api_token = os.getenv("API_TOKEN")
tcms_url = os.getenv("TCMS_URL")
username = os.getenv("USERNAME")
# tcms_url = 'http://localhost:8080'  # Or your Kiwi TCMS instance URL

# Create a connection to the Kiwi TCMS API
client = TCMS(username=username, api_key=api_token, uri=f'{tcms_url}/xml-rpc/')


@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    name = data.get('name')
    description = data.get('description', '')
    
    # Add product to Kiwi TCMS
    try:
        product = client.Product.create({'name': name, 'description': description})
        return jsonify({'message': 'Product created', 'product': product}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/add_test_plan', methods=['POST'])
def add_test_plan():
    data = request.json
    name = data.get('name')
    product_id = data.get('product_id')
    author_id = data.get('author_id')
    text = data.get('text', '')

    # Add test plan to Kiwi TCMS
    try:
        test_plan_data = {
            'name': name,
            'product': product_id,
            'author_id': author_id,
            'text': text
        }
        test_plan = client.TestPlan.create(test_plan_data)
        return jsonify({'message': 'Test Plan created', 'test_plan': test_plan}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/add_test_case', methods=['POST'])
def add_test_case():
    data = request.json
    summary = data.get('summary')
    product_id = data.get('product_id')
    case_text = data.get('text', '')
    test_plan_id = data.get('test_plan_id')

    # Add test case to Kiwi TCMS
    try:
        test_case_data = {
            'summary': summary,
            'product': product_id,
            'text': case_text,
            'plan': test_plan_id
        }
        test_case = client.TestCase.create(test_case_data)
        return jsonify({'message': 'Test Case created', 'test_case': test_case}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
