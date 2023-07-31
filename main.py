import json
import requests
import os

API_URL = os.environ['API_URL']
API_TOKEN = os.environ['API_TOKEN']
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
	"inputs": {
		"query": "What restaurant should I go to if I want spicy noodles?",
		"table": {
			"Restaurant name": ["The Ji Spot", "Mr Due Stinky Tofu", "A Normal Beef Noodle Place", "A Spicy Beef Noodle Place"],
			"features": ["takeout only, american, chicken biscuit, fast, high quality", "taiwanese, seating, good for families, cheap", "beef noodle soup, fast, high quality, seating", "spicy, beef noodle soup, seating, clean, expensive"],
		}
	},
})

print(output)

def main_handler(event, context):
	response = requests.post(API_URL, headers=headers, json=payload)
	return {
        "statusCode": 200,
        "body": response.json()
    }
