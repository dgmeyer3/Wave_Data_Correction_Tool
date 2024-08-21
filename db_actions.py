import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import insert
import sqlalchemy as sa

def connect_to_db(user,password,data_for_db):
    
    db = create_engine(f"postgresql+psycopg2://{user}:{password}@localhost:5432/surf_db", echo = True)
    
    conn = db.connect()
    metadata = sa.MetaData()
    table=sa.Table('example_table', metadata, autoload_with = db)

    for item in data_for_db:
        timestamp = item["timestamp"]

        data_list = {"timestamp": timestamp,"Min": item["surf"]["min"],
                                        "Max": item["surf"]["max"],"Plus": item["surf"]["plus"],
                                        "HumanRelation": item["surf"]["humanRelation"],
                                        "Raw": item["surf"]["raw"],
                                        "OptimalScore": item["surf"]["optimalScore"]}
        
        stmt = insert(table).values(data_list)
        conn.execute(stmt)
                    
    conn.commit()
    conn.close()