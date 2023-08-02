import json
import requests
import os

API_URL = os.environ['API_URL']
API_TOKEN = os.environ['API_TOKEN']

headers = {"Authorization": f"Bearer {API_TOKEN}"}

table = {
    "Restaurant name": ["The Ji Spot", "Mr Due Stinky Tofu", "A Normal Beef Noodle Place", "A Spicy Beef Noodle Place"],
    "features": ["takeout only, american, chicken biscuit, fast, high quality", "taiwanese, seating, good for families, cheap", "beef noodle soup, fast, high quality, seating", "spicy, beef noodle soup, seating, clean, expensive"],

}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()



def lambda_handler(event,contex):
    operation = event['operation'];

    if operation == 'query':
        output = query({
            "inputs": {
                "query": event["payload"]["query"],
                "table": table,
            }
        })

        return {
            "statusCode": 200,
            'headers': {'Content-Type': 'application/json'},
            "body": json.dumps(output)
        }
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "The query was malformed."
            })
        }
