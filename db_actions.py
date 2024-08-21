import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import insert
import sqlalchemy as sa

def connect_to_db(user,password,data_for_db):
    db = create_engine(f"postgresql+psycopg2://{user}:{password}@localhost:5432/surf_db", echo = True)
    metadata = sa.MetaData()
    table=sa.Table('example_table', metadata)

    #,autoload=True, autoload_with=db
    
    with db.connect() as conn:
        for item in data_for_db:
            timestamp = item['timestamp']
            print(timestamp)

            conn.execute(insert(table),{"timestamp": timestamp,"Min": item["surf"]["min"],
                                         "Max": item["surf"]["max"],"Plus": item["surf"]["plus"],
                                         "HumanRelation": item["surf"]["humanRelation"],
                                         "Raw": item["surf"]["raw"],
                                         "OptimalScore": item["surf"]["optimalScore"]})
                
#(timestamp, Min, Max, Plus, HumanRelation, Raw, OptimalScore) VALUES (%s, %s, %s, %s, %s, %s, %s)",
#                         (timestamp, item["surf"]["min"], item["surf"]["max"], item["surf"]["plus"], item["surf"]["humanRelation"], item["surf"]["raw"], item["surf"]["optimalScore"]))

        conn.commit()
        conn.close()