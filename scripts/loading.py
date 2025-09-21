import pandas as pd
from db import engine


"""
    Function to load a CSV file into a PostgreSQL table
    Args:
    csv_path (str): Path to the CSV file.
    table_name (str): Name of the target table in the database.
"""
def load_csv_to_postgres(csv_path, table_name):
    try:
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f" Loaded {csv_path} into '{table_name}' table.")
    except Exception as e:
        print(f" Failed to load {csv_path} into '{table_name}': {e}")


# Main execution block
if __name__ == "__main__":
    # Load messages.csv into the 'messages' table
    load_csv_to_postgres("data/messages.csv", "messages")
    # Load statuses.csv into the 'statuses' table
    load_csv_to_postgres("data/statuses.csv", "statuses")
