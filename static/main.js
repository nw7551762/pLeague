let playerStats;
let x_item = 'three_points_made';
let y_item = 'three_points_percentage';


window.onload = function () {
    fetch('/get-player-stats')
        .then(response => response.json())
        .then(data => {
            playerStats = data;
            //拿到照隊伍分類的球員資料
            let { team_cfgs, bounds } = data_to_cfg(data, 'three_points_made', 'three_points_percentage');
            plotChart(team_cfgs, bounds);
        }
        );
    stat_items.forEach(function (item) {
        createButton(item, 1);
        createButton(item, 0);
    });
}


function TeamCfg(team_name, players_cfg, pointRadius, backgroundColor) {
    this.label = team_name;
    this.data = players_cfg;
    this.pointRadius = pointRadius;
    this.backgroundColor = backgroundColor;
}
const backgroundColor = [
    'rgba(101, 67, 33, 1)',
    'rgba(68, 215, 182, 1)',
    'rgba(128, 99, 132, 1)',
    'rgba(246, 128, 38, 1)',
    'rgba(0, 39, 76, 1)',
    'rgba(233, 91, 128, 1)'
]

function PlayerThreePointsCfg(player_name, data_x, data_y) {
    this.label = player_name;
    this.x = data_x;
    this.y = data_y;
}

//傳入數據, x/y軸item
function data_to_cfg(data, axis_x, axis_y) {
    team_cfgs = [];
    let i = 0;
    const players = [];
    // bounds 紀錄 x y軸上下限 
    let bounds = [0, 0, 0, 0]
    for (let team_name in data) {
        let team = data[team_name]
        let players_cfg_arr = []
        // 球隊config物件
        let team_cfg = new TeamCfg(team_name, players_cfg_arr, 10, backgroundColor[i])
        i += 1


        // for team 把球隊裡的數據加入
        for (let player_name in team) {
            let data_x = parseInt(team[player_name][axis_x]);
            let data_y = parseInt(team[player_name][axis_y]);
            // 球員cfg物件
            let player = new PlayerThreePointsCfg(
                player_name,
                data_x,
                data_y
            );
            bounds[0] = Math.max(bounds[0], data_x);
            bounds[1] = Math.max(bounds[1], data_y);
            bounds[2] = Math.min(bounds[2], data_x);
            bounds[3] = Math.min(bounds[3], data_y);

            //加入cfg arr
            players_cfg_arr.push(player);
        }

        //球員數據物件按照隊伍分類放入 teams物件(map)
        team_cfgs.push(team_cfg);
    }

    return { team_cfgs, bounds };
}

// 將 scatterChart 設為全局變量
let scatterChart;
function plotChart(data_cfg, bounds) {
    const ctx = document.getElementById('myChart').getContext('2d');

    if (scatterChart) {
        scatterChart.destroy(); // 銷毀舊的圖表
    }
    scatterChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: data_cfg
        },
        options: {
            scales: {
                x: {
                    type: 'linear',
                    min: bounds[2],
                    max: bounds[0],
                    title: {
                        display: true,
                        text: x_item,
                        font: {
                            size: 20 // 設定x軸標題字體大小
                        }
                    },
                    ticks: {
                        font: {
                            size: 20 // 設定x軸標籤字體大小
                        }
                    }
                },
                y: {
                    type: 'linear',
                    min: bounds[3],
                    max: bounds[1],
                    title: {
                        display: true,
                        text: y_item,
                        font: {
                            size: 20 // 設定x軸標題字體大小
                        }
                    },
                    ticks: {
                        font: {
                            size: 20 // 設定x軸標籤字體大小
                        }
                    }
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            let label = context.raw.label;
                            return label + ': (' + context.raw.x + ', ' + context.raw.y + ')';
                        }
                    }
                },
                legend: {
                    labels: {
                        font: {
                            size: 20 // 設定圖例字體大小
                        }
                    }
                }
            }
        }
    });
}
