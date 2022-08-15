from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
import pandas as pd

url = "https://www.baseball-reference.com/teams/TOR/2022-batting.shtml"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")

batting_table = soup.find('div', id="all_team_batting").table

rows = batting_table.find('tbody').find_all('tr', attrs = {'class' : None} )#extracts active players and omits non-qualifiers

for player in rows:
    p =player.find('td', {'data-stat':"player"}).text
    print(p)
