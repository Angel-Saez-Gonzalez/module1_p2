text= input("input a text: ")

import json
import requests

url = "https://api.meaningcloud.com/sentiment-2.1"

payload={
    'key': 'a9830bf837591626a247cad2e2bf8f1a',
    'txt': text,
    'lang': 'en',  # 2-letter code, like en es fr ...
}

response = requests.post(url, data=payload)

print('Status code:', response.status_code)
data = dict(json.loads(response.text))


print(data["score_tag"])