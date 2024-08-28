from datetime import datetime
import json
import requests as rq 
import sys
import db_actions
import config_read

#change intervalhours to an appropriate number of my choosing
#count number of items in list
#create column in db for each list item
#load list to db 

def main():

    """
    ARGS
    ----
    argv[0] : filename
    argv[1] : spot_id_params
    argv[2] : db_table_name

    """

    type1 = "wave"

    # params: [spotID, db_table_name]
    cupsogue_params = ["spotId=5842041f4e65fad6a77089e8&days=1&intervalHours=6", "Wave"]
    dune_rd_west_params = ["spotId=584204214e65fad6a7709d07&days=1&intervalHours=6","Westhampton_Dunes"]
    road_k_params = ["spotId=5842041f4e65fad6a77089f7&days=1&intervalHours=6","RoadK"]

    base_url = f"https://services.surfline.com/kbyg/spots/forecasts/"
    
    config_data = config_read.read_config()

    pg_username = config_data['db_username']
    pg_password = config_data['db_password']
    pg_db = config_data['db_name']
    pg_host = config_data['db_host']
    pg_port = config_data['db_port']

    #print(pg_db + ' ' +pg_username + ' ' + pg_password + ' ' + pg_host + ' ' + pg_db + ' ' + pg_port)
    print(sys.argv[1])
    cupsogue_data_dict = request(base_url, type1, sys.argv[1])
    db_actions.connect_to_db(pg_username,pg_password,pg_db,pg_host,pg_port,cupsogue_data_dict,sys.argv[2]) 

def request(url,type_data,params):

    updated_url = f"{url}{type_data}?{params}"

    response = rq.get(updated_url)
    surfline_data = response.content
    surfline_data = json.loads(surfline_data.decode())

    wave_dict = surfline_data.get("data")
    swell_data = wave_dict.get("wave")

    return swell_data

    #there may be multiple occurences of the key 'timestamp' in a dict, and the loop may be overwriting them?
     
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
        
def convertTimestamp(swell_data):
    for dicts in swell_data:
        for key,items in dicts.items():
            if key == "timestamp":
                dt = datetime.fromtimestamp(items)
                formatted_time = dt.strftime('%m/%d/%Y:%I:%M')
                dicts[key] = formatted_time
    
    return swell_data
        
if __name__ == "__main__":
    main()
