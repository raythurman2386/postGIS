import os
from dotenv import load_dotenv

import psycopg2
from sqlalchemy import create_engine, text
import pandas as pd

load_dotenv()
host = os.getenv("SQL_HOST")
database = os.getenv("SQL_DATABASE")
user = os.getenv("SQL_USER")
password = os.getenv("SQL_PASSWORD")

connection_string = f"postgresql://{user}:{password}@{host}/{database}"

# Test connection using psycopg2
try:
    connection = psycopg2.connect(
        dbname=database, user=user, password=password, host=host
    )
    print("Connection to PostgreSQL database successful!")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM cities LIMIT 5;")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()

except Exception as e:
    print(f"Error: {e}")

# Test connection using SQLAlchemy
try:
    engine = create_engine(connection_string)
    with engine.connect() as conn:
        query = text("SELECT * FROM cities LIMIT 5;")
        result = conn.execute(query)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        print("\nData retrieved using SQLAlchemy:")
        print(df)

except Exception as e:
    print(f"SQLAlchemy Error: {e}")
