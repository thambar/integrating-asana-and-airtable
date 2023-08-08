import requests
from airtable import Airtable

# Asana API endpoint and headers
ASANA_ENDPOINT = "https://app.asana.com/api/1.0/events"
ASANA_HEADERS = {
    "Authorization": "Bearer YOUR_ASANA_TOKEN",
}

# Airtable API access
AIRTABLE_API_KEY = 'patUPFsGHavAEzQmE'
AIRTABLE_BASE_ID = 'appSsd4IywdfO0E7Z'
AIRTABLE_TABLE_NAME = "Asana Tasks"

# Create an Airtable client
airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, api_key=AIRTABLE_API_KEY)

def fetch_asana_tasks():
    # Fetch new tasks or events from Asana using webhooks
    # Extract relevant information and return a list of task data
    # Example: Fetch using requests library and parse JSON response
    response = requests.get(ASANA_ENDPOINT, headers=ASANA_HEADERS)
    tasks_data = response.json().get("data", [])
    return tasks_data

def copy_to_airtable(task_data):
    # Copy task data to Airtable
    airtable.insert(task_data)

def main():
    # Fetch tasks from Asana
    asana_tasks = fetch_asana_tasks()

    for task in asana_tasks:
        # Extract relevant task data
        task_data = {
            "Task ID": task.get("id"),
            "Name": task.get("name"),
            "Assignee": task.get("assignee"),
            "Due Date": task.get("due_date"),
            "Description": task.get("description"),
        }

        # Copy task data to Airtable
        copy_to_airtable(task_data)

if __name__ == "__main__":
    main()
