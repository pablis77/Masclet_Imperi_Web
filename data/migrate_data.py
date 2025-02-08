import csv
import sqlite3
from models.data_manager import db, Animal

def migrate_animals_from_csv(file_path, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear tabla Animals
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Animals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        gender TEXT NOT NULL,
        farm TEXT,
        cod TEXT,
        series_number TEXT,
        birth_date DATE,
        status TEXT,
        is_lactating BOOLEAN,
        calving_history TEXT
    )
    ''')

    # Leer archivo CSV y cargar datos
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
            INSERT INTO Animals (name, gender, farm, cod, series_number, birth_date, status, is_lactating, calving_history)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                row['nombre'], row['genero'], row['explotacion'],
                row['COD'], row['n_serie'], row['fecha_nacimiento'],
                row['estado'], row['amamantando'] == 'True', row.get('calving_history', '[]')
            ))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    migrate_animals_from_csv('data/matriz_master.csv', 'masclet_imperi.db')