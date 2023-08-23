import psycopg2

def create_connection():
    try:
        connection = psycopg2.connect(
            user="mahesa",
            password="123",
            host="localhost",
            port="5432",
            database="kampus"
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

def close_connection(connection):
    if connection:
        connection.close()
