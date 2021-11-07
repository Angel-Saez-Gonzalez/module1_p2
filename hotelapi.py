import requests

url = "https://hotels4.p.rapidapi.com/locations/search"

querystring = {"query":"Vincci Palace","locale":"en_US"}

headers = {
    'x-rapidapi-host': "hotels4.p.rapidapi.com",
    'x-rapidapi-key': "b4283fc980msh169a29513a1b3f4p1e133ajsn101454fa67ac"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = dict(json.loads(response.text))



{3 items
"result":"ERROR"
"error_message":"ShoppingApp failed the following input checks: Destination with id [229448] not found in geo service."
"error_keys":[1 item
0:"VALIDATION_ERROR"
]
}