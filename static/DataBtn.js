const stat_items = ['number', 'team', 'games_played', 'time_played', 'two_points_made', 'two_points_attempted', 'two_points_percentage', 'three_points_made', 'three_points_attempted', 'three_points_percentage', 'free_throws_made', 'free_throws_attempted', 'free_throws_percentage', 'points', 'offensive_rebounds', 'defensive_rebounds', 'rebounds', 'assists', 'steals', 'blocks', 'turnovers', 'fouls'];

function createButton(stat_items, is_x_axis) {
    const button = document.createElement('button');
    button.innerText = getChineseName(stat_items);
    const item = stat_items;
    button.id = item;

    button.onclick = function () {
        let item = this.id;
        //點擊的是x軸按鈕, 改變x軸item
        if (is_x_axis) {
            x_item = item;
        } else {
            y_item = item;
        }
        //重新設定數據config
        let { team_cfgs, bounds } = data_to_cfg(playerStats, x_item, y_item);
        //重畫chart
        plotChart(team_cfgs, bounds);
    };
    //將按鈕加到html x軸或y軸 div內
    if (is_x_axis) {
        document.querySelector('.btn-group.x-axis').appendChild(button);
    } else {
        document.querySelector('.btn-group.y-axis').appendChild(button);
    }
}

function getChineseName(stat_items) {
    const names = {
        'number': '球員號碼',
        'team': '球隊名稱',
        'games_played': '出賽場次',
        'time_played': '出賽時間',
        'two_points_made': '兩分球進球數',
        'two_points_attempted': '兩分球出手次數',
        'two_points_percentage': '兩分球命中率',
        'three_points_made': '三分球進球數',
        'three_points_attempted': '三分球出手次數',
        'three_points_percentage': '三分球命中率',
        'free_throws_made': '罰球進球數',
        'free_throws_attempted': '罰球出手次數',
        'free_throws_percentage': '罰球命中率',
        'points': '得分',
        'offensive_rebounds': '進攻籃板',
        'defensive_rebounds': '防守籃板',
        'rebounds': '籃板',
        'assists': '助攻',
        'steals': '抄截',
        'blocks': '阻攻',
        'turnovers': '失誤',
        'fouls': '犯規'
    };
    return names[stat_items];
}



