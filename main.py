from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import pandas as pd

url = "https://www.baseball-reference.com/teams/TOR/2022-batting.shtml"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")

batting_table = soup.find('div', id="all_team_batting").table

rows = batting_table.find('tbody').find_all('tr')#extracts active players and omits non-qualifiers
#attrs = {'class' : None}

for player in rows:
    validRow = player.find('th', {'data-stat': "ranker"}).text
    
    if validRow != 'Rk': #omits invalid rows (rows without player stats)
        validPos = player.find('td', {'data-stat': "pos"}).text
        if validPos != 'P': #omits invalid batters (namely pitchers)
            player_name =player.find('td', {'data-stat':"player"}).text.replace("*","")
            player_batt_avg = player.find('td', {'data-stat':"batting_avg"}).text
            player_hits = player.find('td', {'data-stat':"H"}).text
            player_homers = player.find('td', {'data-stat':"HR"}).text
            player_rbis = player.find('td', {'data-stat':"RBI"}).text
            player_walks = player.find('td', {'data-stat':"BB"}).text
            player_ops =player.find('td', {'data-stat':"onbase_plus_slugging"}).text

            print(f"Player Name: {player_name}")
            print(f"Batting Avg: {player_batt_avg}")
            print(f"player_hits: {player_hits}")
            print(f"player_homers: {player_homers}")
            print(f"player_rbis: {player_rbis}")
            print(f"player_walks: {player_walks}")
            print(f"player_ops: {player_ops}\n")
    
