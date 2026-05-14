import os
from dotenv import load_dotenv
import psycopg
from psycopg import sql, OperationalError

#load environment files
load_dotenv();

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

#connect to postgresql database
def create_connection(db_name = db_name, db_user = db_user, db_password = db_password, db_host = db_host, db_port = db_port):
    """
    Create a connection to the PostgreSQL database.
    """
    try:
        conn = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print("✅ Connection to PostgreSQL successful")
        return conn
    except OperationalError as e:
        print(f"❌ Error: Could not connect to PostgreSQL\n{e}")
        return None

#automate get table columns
def table_columns(table_name = "violations", schema_name="public"):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        # Use parameterized query to avoid SQL injection
        query = sql.SQL("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = %s
                AND table_name   = %s
                ORDER BY ordinal_position;
            """)
        cursor.execute(query, (schema_name, table_name))
        columns = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        print(columns)
        return columns
    except OperationalError as e:
        print(f"Database connection failed: {e}")
        return []
    except Exception as e:
        print(f"Error retrieving columns: {e}")
        return []
