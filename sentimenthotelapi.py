import requests, json
import sentimentmeaningcloudapi as sentiment
#import matplotlib.pyplot as plt

url = "https://hotels4.p.rapidapi.com/reviews/list"

querystring = {"id":"436371","page":"1","loc":"en_US"}

headers = {
    'x-rapidapi-host': "hotels4.p.rapidapi.com",
    'x-rapidapi-key': "b4283fc980msh169a29513a1b3f4p1e133ajsn101454fa67ac"
    }

response = requests.request("GET", url, headers=headers, params=querystring)



data = dict(json.loads(response.text))

print("Total reviews:",data["reviewData"]["guestReviewGroups"]["guestReviewOverview"]["totalCount"])
print("Medium score:",data["reviewData"]["guestReviewGroups"]["guestReviewOverview"]["overall"])

for elem in data["reviewData"]["guestReviewGroups"]["guestReviews"][0]["reviews"]:
    elem
    print(sentiment.getSemtiment(elem))



