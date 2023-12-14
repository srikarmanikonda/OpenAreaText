import sqlite3
from enums import DATABASE_NAME


def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS area_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            state TEXT NOT NULL,
            area_code INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()


def insert_area_code(csv_file_path):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            state = row['state']
            area_code = row['area_code']
            cursor.execute('''
                INSERT INTO area_codes (state, area_code)
                VALUES (?, ?)
            ''', (state, area_code))

    conn.commit()
    conn.close()



def get_all_area_codes_from_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM area_codes')
    area_codes = cursor.fetchall()

    conn.close()
    return area_codes

def get_area_codes_by_state_from_db(state):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM area_codes WHERE state = ?', (state,))
    area_codes = cursor.fetchall()

    conn.close()

    return area_codes

def get_states():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT DISTINCT state FROM area_codes')
    area_codes = cursor.fetchall()

    conn.close()
    return area_codes
