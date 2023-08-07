# integrating-asana-and-airtable

In this code, we add the extract_task_data function to process the received data and extract relevant information (Task ID, Name, Assignee, Due Date, Description) from the JSON payload received from Asana's webhook. We then pass this processed task_data dictionary to the copy_task_to_airtable function, which will create a new record in the "Asana Tasks" table using the Airtable API.

Please note that you'll need to replace 'your_airtable_api_key' and 'your_airtable_base_id' with your actual Airtable API key and base ID, respectively.

With this code, whenever a new task is created on Asana, Asana will send the task data to the Flask app's /webhook endpoint. The app will process the data, copy it to Airtable, and create a new record in the "Asana Tasks" table. The Flask app will then respond with a success or failure message.

Again, make sure to install the required libraries (flask and requests) using pip install flask requests before running the code.
