from wsgiref.util import request_uri
from flask import Flask, request, jsonify

app = Flask(__name__)
    
AIRTABLE_API_KEY = 'your_airtable_api_key'
AIRTABLE_BASE_ID = 'your_airtable_base_id'

@app.route('/webhook', methods=['POST'])
def asana_webhook():
    data = request.json
    # Process the received data (extract relevant information)
    task_data = extract_task_data(data)

    if task_data:
        # Copy the task to Airtable using the data received
        copy_task_to_airtable(task_data)
        return jsonify({'message': 'Task copied to Airtable successfully'}), 200
    else:
        return jsonify({'message': 'Invalid data received'}), 400

def extract_task_data(data):
    # Extract relevant information from the received data
    task_id = data.get('id')
    name = data.get('name')
    assignee = data.get('assignee', {}).get('name', '') if data.get('assignee') else ''
    due_date = data.get('due_on', '')
    description = data.get('notes', '')

    return {
        'Task ID': task_id,
        'Name': name,
        'Assignee': assignee,
        'Due Date': due_date,
        'Description': description
    }

def copy_task_to_airtable(task_data):
    url = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/Asana%20Tasks'
    headers = {
        'Authorization': f'Bearer {AIRTABLE_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'fields': task_data
    }

    response = request_uri.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print('Task copied to Airtable successfully!')
    else:
        print('Failed to copy task to Airtable.')



    return jsonify({'message': 'Webhook received successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
