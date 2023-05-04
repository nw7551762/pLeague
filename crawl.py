from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup


def get_player_stats():
    url_plg = 'https://pleagueofficial.com/stat-player'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    # 向plg api 發出請求, 獲得html源代碼
    response_plg = requests.get(url_plg, headers=headers)
    # 用utf-8解碼
    content = response_plg.content.decode('utf-8')

    # 将 HTML 文档载入 Beautiful Soup
    soup = BeautifulSoup(content, 'html.parser')

    # 找到表格
    table = soup.find('table', {'id': 'main-table'})

    # 找到所有行
    rows = table.find_all('tr')[1:]

    # 生成所有球員字典
    # players = {}
    # 生成球隊dict
    teams = {
        "臺北富邦勇士": {},
        "桃園璞園領航猿": {},
        "新北國王": {},
        "福爾摩沙台新夢想家": {},
        "新竹街口攻城獅": {},
        "高雄17直播鋼鐵人": {}
    }


    # 迭代每一行，生成一个字典并返回
    for row in rows:
        # 生成單一球員字典
        stats = {}
        player_name = row.find('a').text

        # 找到球員所有數據
        cells = row.find_all('td')

        # 依序寫入球員字典內
        player_stats = {
            'number': cells[0].text.strip(),
            'team': cells[1].text.strip(),
            'games_played': cells[2].text.strip(),
            'time_played': cells[3].text.strip(),
            'two_points_made': cells[4].text.strip(),
            'two_points_attempted': cells[5].text.strip(),
            'two_points_percentage': cells[6].text.strip(),
            'three_points_made': cells[7].text.strip(),
            'three_points_attempted': cells[8].text.strip(),
            'three_points_percentage': cells[9].text.strip(),
            'free_throws_made': cells[10].text.strip(),
            'free_throws_attempted': cells[11].text.strip(),
            'free_throws_percentage': cells[12].text.strip(),
            'points': cells[13].text.strip(),
            'offensive_rebounds': cells[14].text.strip(),
            'defensive_rebounds': cells[15].text.strip(),
            'rebounds': cells[16].text.strip(),
            'assists': cells[17].text.strip(),
            'steals': cells[18].text.strip(),
            'blocks': cells[19].text.strip(),
            'turnovers': cells[20].text.strip(),
            'fouls': cells[21].text.strip()
        }

        # 數據寫入所有球員字典內
        teams[player_stats['team']][player_name] = player_stats

        
      
        
        

    return teams
