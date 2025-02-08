import csv
from tinydb import TinyDB, Query
import argparse

def read_csv(file_path):
    # Read and parse the CSV file
    data = []
    try:
        file = open(file_path, mode='r', newline='')
        reader = csv.DictReader(file)
        for i in reader:
            data.append(i)
        file.close()
    except FileNotFoundError:
        raise ValueError(f"File {file_path} not found")
    return data
def insert_into_db(data, db_path=None):
    if db_path is None:
        raise ValueError
    if not data:
        raise ValueError
    information=[]
    # Insert data into TinyDB
    db=TinyDB(db_path)
    for i in data:
        information.append(db.insert(i))
    return information

def query_db(db_path, query_field=None, query_value=None):
    # Query the database
    db=TinyDB(db_path)
    if query_db and query_field:
        QueryObekti=Query()
        return db.search(QueryObekti[query_field]==query_value) or []
    return db.all() or []
def main():
    parser = argparse.ArgumentParser(description="CSV to TinyDB converter")
    parser.add_argument("csv_file", help="Path to the CSV file")
    parser.add_argument("--db", default="database.json", help="Path to TinyDB file")

    args = parser.parse_args()
    data = read_csv(args.csv_file)
    insert_into_db(data, args.db)

if __name__ == "__main__":
    # Main execution logic
    pass
read_csv('user_data.csv')