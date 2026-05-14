import psycopg
from psycopg import sql, OperationalError
import pandas as pd
from pandas.errors import EmptyDataError, ParserError
from postgres_connection import create_connection, table_columns
import numpy as np

violations_columns = table_columns('violations', 'public')
violations_placeholders = ','.join(['%s'] * len(violations_columns))
print(violations_placeholders)

scofflaw_columns = table_columns('scofflaw', 'public')
scofflaw_placeholders = ','.join(['%s'] * len(scofflaw_columns))

insert_query_violations = """
        INSERT INTO violations (id, violation_date, violation_code, violation_status, violation_description, violation_inspector_comments, address)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
    """

insert_query_scofflaw = """
        INSERT INTO scofflaw (record_id, defendant_owner, address, secondary_address, tertiary_address)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (record_id) DO NOTHING;
    """

#import csv files
def ingest_csv(table_name = "violations", query = "", columns = []):
    filepath = input(f"Enter the filepath for the {table_name} table: ").strip()
    print(filepath)
    try:
        df = pd.read_csv(filepath)
        df.columns = (df.columns
        .str.strip()  # Remove leading/trailing spaces
        .str.lower()  # Convert to lowercase
        .str.replace(' ', '_')  # Replace spaces with underscores
        )
        print("CSV loaded")
        print(df.columns)

    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return
    except EmptyDataError:
        print(f"Error: The file {filepath} is empty")
        return
    
    #trim and UPPERCASE address for joining
    df['address'] = df['address'].apply(lambda x: x.strip().upper() if isinstance(x, str) else x)

    #filter the columns
    try:
        df_filtered = df[columns]
    except pd.errors as e:
        print('Data Error: ', e)
        return
    print(df_filtered.columns)
    if df_filtered.shape[1] == 0:
        print("Wrong csv, there are no matching columns")
        return
    
    data_to_insert = [tuple(row) for row in df_filtered.itertuples(index=False, name=None)]
    #print(data_to_insert)
    #Upload csv file to table
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.executemany(query, data_to_insert)
        conn.commit()
        print(f"{len(data_to_insert)} rows inserted successfully.")
    except psycopg.Error as e:
        print('Database Error: ', e)
    except Exception as e:
        print('Unexpected Error: ', e)

#Import Violations Table
ingest_csv("violations", insert_query_violations, violations_columns)
ingest_csv("scofflaw", insert_query_scofflaw, scofflaw_columns)
