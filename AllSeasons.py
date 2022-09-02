from bs4 import BeautifulSoup
import requests 
import pandas as pd
from datetime import datetime
import time

urlDict = { '2022' : "https://www.baseball-reference.com/teams/TOR/2022-batting.shtml",
                '2021' : "https://www.baseball-reference.com/teams/TOR/2021-batting.shtml",
                '2020' : "https://www.baseball-reference.com/teams/TOR/2020-batting.shtml",
                '2019' : "https://www.baseball-reference.com/teams/TOR/2019-batting.shtml",
                '2018' : "https://www.baseball-reference.com/teams/TOR/2018-batting.shtml",
                '2017' : "https://www.baseball-reference.com/teams/TOR/2017-batting.shtml",
                '2016' : "https://www.baseball-reference.com/teams/TOR/2016-batting.shtml",
                '2015' : "https://www.baseball-reference.com/teams/TOR/2015-batting.shtml",
                '2014' : "https://www.baseball-reference.com/teams/TOR/2014-batting.shtml",
                '2013' : "https://www.baseball-reference.com/teams/TOR/2013-batting.shtml",
                '2012' : "https://www.baseball-reference.com/teams/TOR/2012-batting.shtml",
                '2011' : "https://www.baseball-reference.com/teams/TOR/2011-batting.shtml",
                '2010' : "https://www.baseball-reference.com/teams/TOR/2010-batting.shtml" }

season = input('Enter the season year: ')

while season not in urlDict:
    season = input('Enter the season year: ')
minBattAvg = float(input('Enter min batting avg (0.xxx): '))

def findBattingStats():
    html_text = requests.get(urlDict[season]).text
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

                if player_batt_avg >= minBattAvg:
                    print(f"Player Name: {player_name}")
                    print(f"Batting Avg: {player_batt_avg}")
                    print(f"player_hits: {player_hits}")
                    print(f"player_homers: {player_homers}")
                    print(f"player_rbis: {player_rbis}")
                    print(f"player_walks: {player_walks}")
                    print(f"player_ops: {player_ops}\n")

    print("Time Updated:",datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


if __name__ == '__main__':
    while True:
        findBattingStats()
        time.sleep(10)