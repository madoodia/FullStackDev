# --------------------- #
# (C) 2021 madoodia.com #
# --------------------- #

import requests
import json

response = requests.get(
    "https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow"
)

for question in response.json()["items"]:
    print(question["title"])
