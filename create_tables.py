import psycopg
from psycopg import sql, OperationalError
from postgres_connection import create_connection

#Create Table SQL Queries
CREATE_VIOLATIONS_TABLE = """
CREATE TABLE IF NOT EXISTS violations (
    id TEXT PRIMARY KEY,
    violation_date DATE NOT NULL,
    violation_code VARCHAR(50) NOT NULL,
    violation_status VARCHAR(50) NOT NULL,
    violation_description TEXT,
    violation_inspector_comments TEXT,
    address VARCHAR(255) NOT NULL
);
"""

CREATE_SCOFFLAW_TABLE = """
CREATE TABLE IF NOT EXISTS scofflaw (
    record_id TEXT PRIMARY KEY,
    defendant_owner VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    secondary_address VARCHAR(255),
    tertiary_address VARCHAR(255)
);
"""

CREATE_COMMENTS_TABLE = """
CREATE TABLE IF NOT EXISTS comments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    author VARCHAR(255) NOT NULL,
    datetime TIMESTAMP DEFAULT NOW(),
    address VARCHAR(255) NOT NULL,
    comment TEXT NOT NULL
);
"""

#function to create table
def create_table(table_query = ""):
    try:
        conn = create_connection()
        with conn.cursor() as cur:
            cur.execute(table_query)
            conn.commit()
            print(f"Table {table_query} created sucessfully (if not exists)")
            cur.close()
            conn.close()
    except psycopg.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Exception error: {e}")

create_table(CREATE_VIOLATIONS_TABLE)
create_table(CREATE_SCOFFLAW_TABLE)
create_table(CREATE_COMMENTS_TABLE)

#CREATE INDEXES
VIOLATIONS_INDEX = """
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_violations_address ON violations (address);
"""
SCOFFLAW_INDEX = """
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_scofflaw_address ON scofflaw (address);
"""
COMMENTS_INDEX = """
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_comments_address ON comments (address);
"""

def create_index(query = ""):
    try:
        conn = create_connection()
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query)
        print(f"Index {query} created successfully")
        cursor.close()
        conn.close()
    except OperationalError as e:
        print(f"Database connection error: {e}")
    except Exception as e:
        print(f"Error creating index: {e}")

create_index(VIOLATIONS_INDEX)
create_index(SCOFFLAW_INDEX)
create_index(COMMENTS_INDEX)