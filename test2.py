import requests
import json

# The URL of your StripeIntentView endpoint
url = "http://127.0.0.1:8000/core/shop/stripe_payment_intent/2/product/"

# The user's email and the ID of the product they want to purchase
data = {
    "email": "valdgenyuk29@gmail.com",
    'id': 1
}

headers = {
    'Content-Type': 'application/json'
}

# Send the POST request
response = requests.post(url, data=json.dumps(data), headers=headers)

# If the request was successful, the response will contain the client secret
if response.status_code == 200:
    print("Client Secret: ", response.content)
else:
    print("Error: ", response.content)
