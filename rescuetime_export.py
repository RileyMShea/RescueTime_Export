"""
RescueTime appears to offer no built in way to export data from the site without premium membership
This script provides a way to export the data to csv/html/json for non-premium users
"""

#!/usr/bin/python3
import pandas as pd
from pprint import pprint
import requests
import json
import os

api_url = "https://www.rescuetime.com/anapi/data"  # base analytic api
# *******************************************
# Enter your api key inside the quotes
api_key = ""
# example:
# api_key = "B63_NTh2nNtFewTH5vi2WA6TgoCSmjMqzksIL1N6"
# *******************************************
if not api_key:
    print("Enter full api key key available at https://www.rescuetime.com/anapi/manage")
    print("Ex: B63_NTh2nNtFewTH5vi2WA6TgoCSmjMqzksIL1N6")
    while len(api_key) >= 5:
        api_key = input('Full Key: ')
        if len(api_key) >= 5:
            print("Key too short(Did you use a Key Code by mistake?")

api_key.strip()
format = "json"

payload = {'key': api_key,
           'format': format}

with requests.session() as s:
    r = s.get(url=api_url, json=payload)
    assert r.status_code != 400, "Error connecting to api server, please check settings"
    json_query_return = json.loads(r.text)
    pprint(json_query_return)
    df = pd.DataFrame(data=json_query_return['rows'], columns=json_query_return['row_headers'])
    df.to_json("rescue_time_data.json")
    df.to_html("rescue_time_data.html")
    df.to_csv("rescue_time_data.csv")
