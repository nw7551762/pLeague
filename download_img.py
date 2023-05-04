import os
import pyodbc

def save_image_to_database(image_path, player_name):
    with open(image_path, 'rb') as file:
        image_data = file.read()

    server = 'localhost'
    database = 'pleague'
    username = 'sa'
    password = 'sa123456'
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    insert_query = "INSERT INTO players (name, photo) VALUES (?, ?)"
    cursor.execute(insert_query, player_name, image_data)

    connection.commit()
    cursor.close()
    connection.close()

def save_all_images_in_folder(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith('.png'):
            # image_path = os.path.join(folder_path, file)
            player_name = os.path.splitext(file)[0]
            print( player_name )
            # save_image_to_database(image_path, player_name)

# 使用範例
folder_path = 'static/img/player'
save_all_images_in_folder(folder_path)
