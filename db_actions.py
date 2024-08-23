import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import insert
import sqlalchemy as sa

def connect_to_db(user,password,data_for_db):
    
    db = create_engine(f"postgresql+psycopg2://{user}:{password}@localhost:5432/surf_db", echo = True)
    
    conn = db.connect()
    metadata = sa.MetaData()
    table=sa.Table('wave', metadata, autoload_with = db)

    for item in data_for_db:
        timestamp = item["timestamp"]

        data_list = {"timestamp": timestamp,"min": item["surf"]["min"],
                                        "max": item["surf"]["max"],"plus": item["surf"]["plus"],
                                        "humanRelation": item["surf"]["humanRelation"],
                                        "raw": str(item["surf"]["raw"]),
                                        "optimalScore": item["surf"]["optimalScore"]}
        
        stmt = insert(table).values(data_list)
        conn.execute(stmt)
                    
    conn.commit()
    conn.close()