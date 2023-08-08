import requests

AIRTABLE_API_KEY = 'patUPFsGHavAEzQmE'
AIRTABLE_BASE_ID = 'appSsd4IywdfO0E7Z'

def copy_task_to_airtable(task_data):
    url = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/Asana%20Tasks'
    headers = {
        'Authorization': f'Bearer {AIRTABLE_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'fields': {
            'Task ID': task_data['id'],
            'Name': task_data['name'],
            'Assignee': task_data['assignee']['name'] if task_data.get('assignee') else '',
            'Due Date': task_data['due_on'] if task_data.get('due_on') else '',
            'Description': task_data['notes'] if task_data.get('notes') else ''
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print('Task copied to Airtable successfully!')
    else:
        print('Failed to copy task to Airtable.')

