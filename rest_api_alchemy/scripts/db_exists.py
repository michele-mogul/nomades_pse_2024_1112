import pymysql


def ensure_database_exists():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="root", port=3307)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS questdb")
    except pymysql.MySQLError as e:
        print(f"Error while creating database: {e}")
        raise e
    finally:
        if 'connection' in locals() and connection:
            connection.close()


if __name__ == "__main__":
    ensure_database_exists()
