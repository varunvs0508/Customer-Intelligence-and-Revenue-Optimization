from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def load_to_db(df):
    connection = os.getenv("DB_CONNECTION")

    if not connection:
        print("No DB connection found. Skipping DB step.")
        return

    engine = create_engine(connection)

    df.to_sql(
        name="transactions",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data uploaded to database.")