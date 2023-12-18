import sqlite3
import csv
from enums import DATABASE_NAME


def create_database():
    
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS area_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            state TEXT NOT NULL,
            area_code INTEGER NOT NULL,
            UNIQUE(state, area_code)
        )
    ''')
    conn.commit()
    conn.close()



def insert_area_code(csv_file_path):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            state = row['state']
            area_code = row['area_code']
            try:
                cursor.execute('''
                    INSERT INTO area_codes (state, area_code)
                    VALUES (?, ?)
                ''', (state, area_code))
            except sqlite3.IntegrityError:
                print(f"Duplicate entry for state: {state}, area_code: {area_code} not added.")
                continue

    conn.commit()
    conn.close()



def get_all_area_codes_from_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT state, area_code FROM area_codes ORDER BY state')
    area_codes = cursor.fetchall()

    conn.close()
    area_codes_dict = {}
    for state, area_code in area_codes:
        if state in area_codes_dict:
            area_codes_dict[state].append(area_code)
        else:
            area_codes_dict[state] = [area_code]

    return area_codes_dict

def get_area_codes_by_state_from_db(state):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM area_codes WHERE LOWER(state) = ?', (state,))
    area_codes = cursor.fetchall()

    conn.close()

    return [area_code[0] for area_code in area_codes]



def get_states():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT DISTINCT state FROM area_codes')
    area_codes = cursor.fetchall()

    conn.close()
    return area_codes
def get_state_by_area_code_from_db(area_code):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT state FROM area_codes WHERE area_code = ?', (area_code,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    else:
        return None