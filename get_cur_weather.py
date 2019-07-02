import json
import requests





url = "https://api.weather.gov/points/38.6303,-90.2003"
url = "https://api.weather.gov/gridpoints/LSX/94,74/forecast"

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

response = requests.get( url)
data = json.loads(response.text)

temps = []
times = []

for item in data["properties"]["periods"]:
     temps.append(item["temperature"])
     loc = item["startTime"].find("T")
     to_add = item["name"]+": "
     times.append(to_add)
     print('{:-<25}'.format(item['name'])+ str(item["temperature"]))

