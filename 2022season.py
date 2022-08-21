from bs4 import BeautifulSoup
import requests  
import pandas as pd
from datetime import datetime
import time

def findBattingStats():
    url = "https://www.baseball-reference.com/teams/TOR/2022-batting.shtml"
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")

    batting_table = soup.find('div', id="all_team_batting").table

    rows = batting_table.find('tbody').find_all('tr')
    #attrs = {'class' : None}

    #loops through player data
    for player in rows:
        rowFilled = True
        invalidRow = player.find('th', {'data-stat': "ranker"}).text
        for element in player: #loops thorugh row to ensure row is filled with data
            if element.text == '':
                rowFilled = False
        if invalidRow != 'Rk' and rowFilled: #omits invalid rows (rows without player data)
            validPos = player.find('td', {'data-stat': "pos"}).text
            if validPos != 'P': #omits invalid batters (namely pitchers)
                player_name = player.find('td', {'data-stat':"player"}).text.replace("*","")
                player_batt_avg = float(player.find('td', {'data-stat':"batting_avg"}).text.replace(".", ""))
                player_hits = int(player.find('td', {'data-stat':"H"}).text)
                player_homers = int(player.find('td', {'data-stat':"HR"}).text)
                player_rbis = int(player.find('td', {'data-stat':"RBI"}).text)
                player_walks = int(player.find('td', {'data-stat':"BB"}).text)
                player_ops = float(player.find('td', {'data-stat':"onbase_plus_slugging"}).text.replace(".", ""))

                player_batt_avg /= 1000
                player_ops /= 1000
                currentTime = datetime.now().strftime("%d,%m,%Y %H,%M,%S")
                with open(f'posted stats/{player_name} {currentTime}.txt', 'w') as f:

                    f.write(f"Player Name: {player_name}\n")
                    f.write(f"Batting Avg: {player_batt_avg}\n")
                    f.write(f"player_hits: {player_hits}\n")
                    f.write(f"player_homers: {player_homers}\n")
                    f.write(f"player_rbis: {player_rbis}\n")
                    f.write(f"player_walks: {player_walks}\n")
                    f.write(f"player_ops: {player_ops}\n")
                print(f'File Saved as: BlueJays', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    print("Time Updated:",datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


if __name__ == '__main__':
    while True:
        findBattingStats()
        time.sleep(60)