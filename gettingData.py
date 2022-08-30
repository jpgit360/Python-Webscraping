import csv

Name = input("Please provide name: ")

with open('posted stats/BlueJays 23,08,2022 12,18,21.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    #ask user for macroscopic search
    for index, row in enumerate(reader):
        if Name.lower() in row['Name'].lower():
            print("Here are the names: ",row['Name'])
            print("\nindex: ", index)
        else:
            print("No")
    #ask user for specific search
    numPlayer = input("Provide index: ")


