import csv
from tinydb import TinyDB, Query

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
def insert_into_db(data, db_path):
    # Insert data into TinyDB
    pass

def query_db(db_path, query_field, query_value):
    # Query the database
    pass

if __name__ == "__main__":
    # Main execution logic
    pass
read_csv('user_data.csv')