import requests

API_URL = "http://localhost:3000/api/v1/prediction/0268f686-0e79-4989-a8d0-bd55021ba1d3"
headers = {"Authorization": "Bearer wMixFfbwJX3G9eIKTAPEiMboFAfLGMJjqPLuww0cgXk"}


def generate_article(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# import requests

# API_URL = "http://localhost:3000/api/v1/prediction/0268f686-0e79-4989-a8d0-bd55021ba1d3"
# headers = {"Authorization": "Bearer wMixFfbwJX3G9eIKTAPEiMboFAfLGMJjqPLuww0cgXk"}

# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()
    
# output = query({
#     "question": "Hey, how are you?",
# })