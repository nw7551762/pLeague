from flask import Flask, Response, render_template, jsonify, make_response, render_template_string, request
import requests
import json
import crawl
import pyodbc
import configparser


app = Flask(__name__)
app.static_folder = 'static'  # 设置静态文件目录为static

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


@app.route('/')
def index():
    return render_template('threePoint.html')


@app.route('/get-player-stats')
def get_player_stats():
    # 将字典转换为json字符串，并且编码格式设为'utf-8'
    players_json = json.dumps(crawl.get_player_stats(),
                              ensure_ascii=False).encode('utf-8')
    # 使用make_response()方法生成Response对象
    response = make_response(players_json)
    # 设置响应头的Content-Type字段为application/json
    response.headers['Content-Type'] = 'application/json'
    return response


###################

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

@app.route('/player-image/<player_name>')
def player_image(player_name):
    image_data = get_image_by_name(player_name)
    if image_data:
        return Response(image_data, content_type='image/png')
    else:
        return "找不到該球員的圖片。", 404

#<img src="/player-image/{player_name}" alt="球員照片">

############

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
