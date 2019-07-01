import json
import requests

import sys, pygame





url = "https://api.weather.gov/points/38.6303,-90.2003"

payload = "{\r\n    \"text\": \"Test failed, pay attention\"\r\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "41ffc261-d159-4e83-a8a5-d5219851aec2,19af9a1e-610f-4cec-9b9e-76993738b717",
    'Host': "api.weather.gov",
    'accept-encoding': "gzip, deflate",
    'content-length': "46",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }




url = "https://api.weather.gov/gridpoints/LSX/94,74/forecast/hourly"

headers = {
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "d13aef25-7e82-43ae-a397-06f455fa47a8,556523b6-c384-4746-929f-8e8dc867671e",
    'Host': "api.weather.gov",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)

temps = []
times = []

for item in data["properties"]["periods"]:
     temps.append(item["temperature"])
     loc = item["startTime"].find("T")
     to_add = item["startTime"][:loc+3] 
     times.append(to_add)

