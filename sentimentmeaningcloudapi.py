

import json
import requests

def getSemtiment(text):
    url = "https://api.meaningcloud.com/sentiment-2.1"

    payload={
        'key': 'a9830bf837591626a247cad2e2bf8f1a',
        'txt': text,
        'lang': 'en',  # 2-letter code, like en es fr ...
    }

    response = requests.post(url, data=payload)
    data = dict(json.loads(response.text))
    return data["sentence_list"][0]["score_tag"]