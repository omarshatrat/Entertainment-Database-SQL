import sqlite3
import pandas as pd
from sqlalchemy import create_engine

csv_file = pd.read_csv('hw5_original.csv')
db_file = 'hw5.db'


conn = sqlite3.connect(db_file)

engine = create_engine('sqlite:///hw5_python.db')
csv_file.to_sql('hw5_python', con = engine, if_exists = 'replace', index = False)


conn.close()