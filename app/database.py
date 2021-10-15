from sqlalchemy import create_engine

import os


db_username = os.getenv('DB_USERNAME', 'postgres')
db_password = os.getenv('DB_PASSWORD', '1234abcd')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '5432')
db_name = os.getenv('DB_NAME', 'wheretogo')

db_url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(db_username, db_password, db_host, db_port, db_name)

engine = create_engine(db_url)


# def TestConnection():
#     try:
#         conn = engine.connect()
#         conn.close()
#         print("Connection worked.")
#     except Exception as error:
#         print("Connection failed.")
#         print("ERROR:", error)