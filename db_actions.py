import psycopg2
from sqlalchemy import create_engine

def connect_to_db(user,password,data_for_db):
    db = create_engine(f"postgresql+psycopg2://{user}:{password}@localhost:5432/surf_db", echo = True)
    with db.connect() as conn:
        for item in data_for_db:
            timestamp = item['timestamp']

            conn.execute("INSERT into example_table(timestamp, Min, Max, Plus, HumanRelation, Raw, OptimalScore) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                          (timestamp, item["surf"]["min"], item["surf"]["max"], item["surf"]["plus"], item["surf"]["humanRelation"], item["surf"]["raw"], item["surf"]["optimalScore"]))

        conn.commit()
        conn.close()


