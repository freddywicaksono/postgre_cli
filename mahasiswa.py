from db import *

def create_record(connection, nim, nama, jk, prodi):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO mahasiswa (nim, nama, jk, prodi) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (nim, nama, jk, prodi))
        connection.commit()
        print("Record created successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error creating record:", error)

def read_records(connection):
    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM mahasiswa"
        cursor.execute(select_query)
        records = cursor.fetchall()
        for record in records:
            print(record)
    except (Exception, psycopg2.Error) as error:
        print("Error reading records:", error)

def get_record(connection,kode):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM mahasiswa WHERE nim = %s"
        values = (kode,)
        cursor.execute(query, values)
        result = cursor.fetchone()  # Use fetchone() as you are fetching a single row
        if result:
            id, nim, nama, jk, prodi = result
            return id, nim, nama, jk, prodi
        else:
            return None
    except (Exception, psycopg2.Error) as error:
        print("Error reading records:", error)

def update_record(connection, nim, new_nama, new_jk, new_prodi):
    try:
        cursor = connection.cursor()
        update_query = "UPDATE mahasiswa SET nama = %s, jk = %s, prodi = %s WHERE nim = %s"
        cursor.execute(update_query, (new_nama, new_jk, new_prodi, nim))
        connection.commit()
        print("Record updated successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error updating record:", error)

def delete_record(connection, id):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM mahasiswa WHERE id = %s"
        cursor.execute(delete_query, (id,))
        connection.commit()
        print("Record deleted successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error deleting record:", error)
