import csv
import os

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
            print("Here are the names: ",row['Name'])
            print("\nindex: ", index)
        else:
            print("No")

#ask user for specific search  
with open(f"posted stats/{latestFile}") as csvfile:
    numPlayer = int(input("Provide index: "))
    reader = csv.DictReader(csvfile)
    for index, row in enumerate(reader):
        if index == numPlayer:
            playerName = row['Name']


for filename in os.listdir(directory):
    f = open(f"posted stats/{filename}", "r")
    reader = csv.DictReader(f)
    for index, row in enumerate(reader):
        if playerName in row['Name']:
            print(row['Name'], "and", row['Avg'])


