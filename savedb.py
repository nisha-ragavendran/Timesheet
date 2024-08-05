import requests
import json

def insert_row(Create_row):
    url = "https://eu-central-1.aws.data.mongodb-api.com/app/data-qjiey/endpoint/data/v1/action/insertOne"

    payload = json.dumps({
    "collection": "Timesheet",
    "database": "Timesheet_1",
    "dataSource": "Cluster0",
    "document":Create_row
    
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'zDjXFEulJXCLlFXnVkVctDZ4h7c6XKzcnpXwS5TBP6r0k14xYe35aXHMf1j5JSVa',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

def find_data(User_name,Date):
    url = "https://eu-central-1.aws.data.mongodb-api.com/app/data-qjiey/endpoint/data/v1/action/findOne"

    payload = json.dumps({
    "collection": "Timesheet",
    "database": "Timesheet_1",
    "dataSource": "Cluster0",
    "filter":{"User":User_name,
              "Date":Date}
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'zDjXFEulJXCLlFXnVkVctDZ4h7c6XKzcnpXwS5TBP6r0k14xYe35aXHMf1j5JSVa',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return json.loads(response.text)

def delete_data(User_name,Date):
    url = "https://eu-central-1.aws.data.mongodb-api.com/app/data-qjiey/endpoint/data/v1/action/deleteOne"

    payload = json.dumps({
    "collection": "Timesheet",
    "database": "Timesheet_1",
    "dataSource": "Cluster0",
    "filter":{"User":User_name,
              "Date":Date}
    
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'zDjXFEulJXCLlFXnVkVctDZ4h7c6XKzcnpXwS5TBP6r0k14xYe35aXHMf1j5JSVa',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    