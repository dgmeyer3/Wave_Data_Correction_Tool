import requests as rq 
import json
from sqlalchemy import create_engine
from sqlalchemy import text
from datetime import datetime

def main():

    type1 = "wave"
    cupsogue_params = "spotId=5842041f4e65fad6a77089e8&days=1&intervalHours=12"
    base_url = f"https://services.surfline.com/kbyg/spots/forecasts/"
    
    #{type1}?{cupsogue_params}

    #cupsogue_data_dict = request(base_url, type1, cupsogue_params)
    #display(cupsogue_data_dict)
    connect_to_db()

def request(url,type_data,params):

    updated_url = f"{url}{type_data}?{params}"

    response = rq.get(updated_url)
    surfline_data = response.content
    surfline_data = json.loads(surfline_data.decode())

    wave_dict = surfline_data.get("data")
    swell_data = wave_dict.get("wave")

    #looks for timestamps and updates to datetime (string format)
    #there may be multiple occurences of the key 'timestamp' in a dict, and the loop may be overwriting them?

    for dicts in swell_data:
        for key,items in dicts.items():
            if key == "timestamp":
                dt = datetime.fromtimestamp(items)
                formatted_time = dt.strftime('%m/%d/%Y:%I:%M:%s')
                dicts[key] = formatted_time
    
    return swell_data
    
def display(info_to_display):

    dataType = type(info_to_display)
    print(str(dataType))
    
    if str(dataType) == "<class 'list'>":
        print(json.dumps(info_to_display,indent=2))
        #print(swell_data[0])
    else:
        print("the requested data was not a list, and"
               "could not be displayed with this function.")
        
def connect_to_db():
    db = create_engine("sqlite+pysqlite:///:memory:", echo = True)
    with db.connect() as conn:
        result = conn.execute(text("select 'test'"))
        
if __name__ == "__main__":
    main()
