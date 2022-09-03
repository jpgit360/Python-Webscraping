import csv
import os
from unicodedata import name
import pandas as pd
from unittest import result
import matplotlib.pyplot as plt

statDict = {    
    1 : 'Avg',
    2 : 'Hits',
    3 : 'HR',
    4 : 'RBI',
    5 : 'Walks',
    6 : 'OPS',
}

directory = 'posted stats'
numPlayer = -1
nameNotFound = True
df = pd.DataFrame()

#get specific name of player from newest file
latestFile = os.listdir(directory)[-1]

#note: SEVERAL with open() STATEMENTS WERE USED AS THEY CAN EACH ONLY HANDLE ONE LOOP

#ask user for macroscopic search and displays players that resemble input
while nameNotFound:
    nameCount = 0
    Name = input("Please provide name: ")
    with open(f"posted stats/{latestFile}") as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader):
            if Name.lower() in row['Name'].lower():
                nameCount += 1
                print(index, ": ",row['Name'])
        if nameCount != 0:
            nameNotFound = False

#ask user for specific index search
with open(f"posted stats/{latestFile}") as csvfile:
    reader = csv.DictReader(csvfile)
    rowCount = sum(1 for row in csvfile) - 2
    while numPlayer < 0 or numPlayer > rowCount:
        numPlayer = int(input("Provide index: "))

#finds player
with open(f"posted stats/{latestFile}") as csvfile:
    reader = csv.DictReader(csvfile)
    for index, row in enumerate(reader):
        if index == numPlayer:
            playerName = row['Name']
    
#get user input for which stat
userStat = int(input("Choose which stat:\n1. Avg\n2. Hits\n3. HR\n4. RBI\n5. Walks\n6. OPS\n>> "))

#get results
for file in os.listdir(directory): #loop through all files (oldest to newest)
    f = open(f"posted stats/{file}", "r")
    reader = csv.DictReader(f)
    for index, row in enumerate(reader): #loop through rows within file
        if playerName in row['Name']: #find instance of selected player
            resultDate = row['Date']
            resultStat = float(row[statDict[userStat]])
            sers = pd.Series(
                    [resultDate, resultStat],
                    index = ['Date', statDict[userStat]]
                )
            df = pd.concat([df, sers.to_frame().T], ignore_index=True)

#print plot
df.plot.line(
    x = 'Date',
    y = statDict[userStat],
    title = f"{playerName}'s {statDict[userStat]}"
)
plt.show()