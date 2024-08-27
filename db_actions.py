import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import insert
from sqlalchemy import Table, Column, Integer, String, Boolean, MetaData
import sqlalchemy as sa

def connect_to_db(user,password,db_name,db_host,db_port,data_for_db,table_name):
    """
    connects to a db with the username, password, db name, table name, port and host.

    Parameters
    ----------
    user : string
    password : string
    db_name : string
    db_host : string
    db_port : string
    data_for_db: list[string]
    table_name: string

    Returns
    -------
    void 
    
    """

    db = create_engine(f"postgresql+psycopg2://{user}:{password}@{db_host}:{db_port}/{db_name}", echo = True)
    conn = db.connect()

    if not sa.inspect(db).has_table(table_name):
        new_table = create_surf_table(table_name)
        new_table.create(db)
    
    metadata = sa.MetaData()
    table=sa.Table('Wave', metadata, autoload_with = db)

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

def create_surf_table(table_name_for_helper):
    metadata_var = MetaData()

    test_table = Table(
        table_name_for_helper,
        metadata_var,
        Column("id", Integer,primary_key=True),
        Column("timestamp", Integer),
        Column("min", Integer),
        Column("max", Integer),
        Column("plus", Boolean),
        Column("humanRelation", String(255)),
        Column("raw", String(255)),
        Column("optimalScore", Integer),
        Column("accurateRating", Boolean),
        Column("realMin", Integer),
        Column("realMax", Integer),
        Column("comments", String)
        
    )
    return test_table