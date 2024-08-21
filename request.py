import requests as rq 
import json
from datetime import datetime
import db_actions

#db: testdatabase
#change intervalhours to an appropriate number of my choosing
#count number of items in list
#create column in db for each list item
#load list to db 

def main():

    type1 = "wave"
    cupsogue_params = "spotId=5842041f4e65fad6a77089e8&days=1&intervalHours=6"
    base_url = f"https://services.surfline.com/kbyg/spots/forecasts/"
    pg_username = "surf_admin"
    pg_password = ""
    
    #{type1}?{cupsogue_params}

    cupsogue_data_dict = request(base_url, type1, cupsogue_params)
    

    #display(cupsogue_data_dict)

    #print(type(cupsogue_data_dict[0]["timestamp"]))
    #print(cupsogue_data_dict[0]["surf"])
    #for key, value in cupsogue_data_dict[0]['surf'].items():
    #    print(f"{key}:{type(value)}")
   
    db_actions.connect_to_db(pg_username,pg_password,cupsogue_data_dict) 

def request(url,type_data,params):

    updated_url = f"{url}{type_data}?{params}"

    response = rq.get(updated_url)
    surfline_data = response.content
    surfline_data = json.loads(surfline_data.decode())

    wave_dict = surfline_data.get("data")
    swell_data = wave_dict.get("wave")

    return swell_data

    #there may be multiple occurences of the key 'timestamp' in a dict, and the loop may be overwriting them?
'''
    for dicts in swell_data:
        for key,items in dicts.items():
            if key == "timestamp":
                dt = datetime.fromtimestamp(items)
                formatted_time = dt.strftime('%m/%d/%Y:%I:%M')
                dicts[key] = formatted_time
'''
     
def display(info_to_display):

    dataType = type(info_to_display)
    print(str(dataType))
    
    if str(dataType) == "<class 'list'>":
        print(json.dumps(info_to_display,indent=2))
        print(len(info_to_display))
        #print(swell_data[0])

    else:
        print("the requested data was not a list, and"
               "could not be displayed with this function.")
        
if __name__ == "__main__":
    main()
