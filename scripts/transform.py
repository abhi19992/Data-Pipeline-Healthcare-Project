from sqlalchemy import create_engine, text
import os
from db import engine

'''
This script reads and executes a SQL file to create and populate
the messages_enriched table in your PostgreSQL database.
'''


# ---- Path to the SQL file that joins tables ----
sql_file_path = os.path.join(os.path.dirname(__file__), "../sql/message_enriched.sql")

# Read the SQL file
with open(sql_file_path, "r") as file:
    sql_commands = file.read()
    print(sql_commands)

# Execute SQL commands inside a transaction
with engine.begin() as conn:
    conn.execute(text(sql_commands))
    print(" messages_enriched table created and populated successfully")
