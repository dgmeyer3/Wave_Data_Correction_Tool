import requests as rq 
import json
from datetime import datetime

type1 = "wave"
params = "spotId=5842041f4e65fad6a77089e8&days=1&intervalHours=12"
url = f"https://services.surfline.com/kbyg/spots/forecasts/{type1}?{params}"

response = rq.get(url)
surfline_data = response.content
surfline_data = json.loads(surfline_data.decode())

wave_dict = surfline_data.get("data")
swell_data = wave_dict.get("wave")
#swell_data_print = json.dumps(wave_dict.get("wave"),indent=2)

#print(swell_data[0])


#looks for timestamps and updates to datetime (string format)
#there may be multiple occurences of the key 'timestamp' in a dict, and the loop may be overwriting them?

for dicts in swell_data:
    for key,items in dicts.items():
        if key == "timestamp":
            dt = datetime.fromtimestamp(items)
            formatted_time = dt.strftime('%m/%d/%Y:%I:%M:%s')
            dicts[key] = formatted_time
            
print(json.dumps(swell_data,indent=2))
