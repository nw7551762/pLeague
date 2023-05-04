import os
import pyodbc
import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def get_image_by_name(player_name):
    config = load_config()
    server = config.get('MSSQL', 'server')
    database = config.get('MSSQL', 'database')
    username = config.get('MSSQL', 'username')
    password = config.get('MSSQL', 'password')
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    select_query = "SELECT photo FROM players WHERE name = ?"
    cursor.execute(select_query, player_name)

    image_data = None
    row = cursor.fetchone()
    if row:
        image_data = row[0]

    cursor.close()
    connection.close()
    return image_data

def save_image_to_file(image_data, file_path):
    with open(file_path, 'wb') as file:
        file.write(image_data)

# 使用範例
player_name = "高國豪"
image_data = get_image_by_name(player_name)

if image_data:
    file_path = f'{player_name}.png'
    save_image_to_file(image_data, file_path)
    print(f'圖片已儲存為: {file_path}')
else:
    print('找不到該球員的圖片。')
