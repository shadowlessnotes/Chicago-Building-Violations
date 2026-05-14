# Chicago Building Violations API

## Setup and Installation


1. **Clone the repository**
```bash
git clone https://github.com/yourusername/chicago_building_violations.git
cd chicago_building_violations
```
2. **create your virtual environment**
```
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies that are required for this app to run**
```Bash
pip install -r requirements.txt
```

4. **Create .env file in the project root with PostgreSQL database credentials:**

Create a .env file in the root folder with your database credentials
```python
DB_HOST='hostname'
DB_PORT='5432'
DB_USER='user'
DB_PASSWORD='password'
DB_NAME='database'
```
5. **Run create_tables.py** to create the 3 tables required for this api
- violations
- scofflaw
- comments
```python
python create_tables.py
```
The appropriate indexes will also be created with this script.

6. **Run ingest_csv.py** to ingest initial data from csv to the data tables. CSVs are included. The files should be in the project root folder.

```
Building_Code_Scofflaw_List_20250807.csv
Building_Violations_20250815.csv
```
**Run ingest_csv.py**
```python
python ingest_csv.py
```

You will be asked for the csvs for the **violations** table and the **scofflaw** table.
If files are in the project root, you may use the relateive file path. Otherwise, use the full file path.

ingest_csv.py should return 'Data Ingested OK' for each dataset.
Otherwise, make sure the csv data and filepaths are correct.
If done, the initial setup is complete.

7. **Start api server.**

```python
python manage.py runserver
```
Check that server is running without any errors.

## API Documentation

Refer to api documentation file api_doc.md for the api endpoint documentation.

## License

This project is open-source.

## Author

Jun Yu Tan