# pLeague

安裝步驟
1. 下載或複製此專案到你的本機端。
2. 進入專案資料夾。
3. 建立虛擬環境，使用 virtualenv 或 conda 都可以。
  例如：
    virtualenv venv
    source venv/bin/activate
4. 安裝相依套件，執行以下命令：
  pip install -r requirements.txt
5. 設定環境變數，複製 example.env 到 .env，並根據需要修改其中的設定。
  cp example.env .env
  
使用步驟
1. 啟動 Flask 應用程式，執行以下命令：
  flask run
開啟瀏覽器，在網址列輸入 http://localhost:5000/
現在您可以使用此 Flask 應用程式。
