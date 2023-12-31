import sqlite3
import pandas as pd
from sqlalchemy import create_engine

csv_file = pd.read_csv('entertainment_original.csv')
db_file = 'entertainment.db'


conn = sqlite3.connect(db_file)

engine = create_engine('sqlite:///entertainment_python.db')
csv_file.to_sql('entertainment_python', con = engine, if_exists = 'replace', index = False)


conn.close()
