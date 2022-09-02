import csv
import os
import pandas as pd
from unittest import result
import matplotlib.pyplot as plt

Name = input("Please provide name: ")
directory = 'posted stats'

#get specific name of player from newest file
latestFile = os.listdir(directory)[-1]
print(latestFile)

#ask user for macroscopic search
with open(f"posted stats/{latestFile}") as csvfile:
    reader = csv.DictReader(csvfile)
    for index, row in enumerate(reader):
        if Name.lower() in row['Name'].lower():
            print(index, ": ",row['Name'])

#ask user for specific search  
with open(f"posted stats/{latestFile}") as csvfile:
    numPlayer = int(input("Provide index: "))
    reader = csv.DictReader(csvfile)
    for index, row in enumerate(reader):
        if index == numPlayer:
            playerName = row['Name']

#get user input for which stat
userStat = int(input("Choose which stat:\n1. Avg\n2. Hits\n3. HR\n4. RBI\n5. Walks\n6. OPS\n>> "))

statDict = { 1 : 'Avg',
                2 : 'Hits',
                3 : 'HR',
                4 : 'RBI',
                5 : 'Walks',
                6 : 'OPS',
}
df = pd.DataFrame()

#get results
for file in os.listdir(directory): #loop through all files (oldest to newest)
    f = open(f"posted stats/{file}", "r")
    reader = csv.DictReader(f)
    for index, row in enumerate(reader): #loop through rows within file
        if playerName in row['Name']: #find instance of selected player
            resultDate = row['Date']
            resultStat = row[statDict[userStat]]
            sers = pd.Series(
                    [resultDate, resultStat],
                    index = ['Date', statDict[userStat]]
                )
            df = pd.concat([df, sers.to_frame().T], ignore_index=True)

print(df)

df.plot(x = 'Date', y = statDict[userStat], kind = 'scatter')
plt.show()

