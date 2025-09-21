from sqlalchemy import create_engine, text
from db import engine

# SQL statement to create 'messages' and 'statuses' tables if they do not exist
create_tables_sql = """
CREATE TABLE IF NOT EXISTS messages (
    id BIGINT,
    content TEXT,
    message_type TEXT,
    masked_addressee TEXT,
    masked_from_addr TEXT,
    direction TEXT,
    external_id TEXT,
    external_timestamp TIMESTAMP,
    is_deleted BOOLEAN,
    last_status TEXT,
    last_status_timestamp TIMESTAMP,
    rendered_content TEXT,
    uuid UUID PRIMARY KEY,
    inserted_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS statuses (
    id BIGINT,
    status TEXT,
    timestamp TIMESTAMP,
    uuid UUID,
    message_uuid UUID,
    number_id TEXT,
    inserted_at TIMESTAMP,
    updated_at TIMESTAMP
);
"""
# Try to execute the SQL to create tables.
try:
    with engine.begin() as conn:
        conn.execute(text(create_tables_sql))
        print("Tables created successfully")
    # Print any error that occurs during table creation
except Exception as e:
    print("Error:", e)