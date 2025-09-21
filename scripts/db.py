from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()  
# Load environment variables from .env
'''
This file loads database connection parameters from environment variables
and creates a SQLAlchemy engine for connecting to the PostgreSQL database.
Make sure to set the following environment variables in a .env file or your system:
- DB_USER: Database username
- DB_PASS: Database password
- DB_HOST: Database host (e.g., localhost)
- DB_PORT: Database port (e.g., 5432)
- DB_NAME: Database name
'''
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
print(engine)