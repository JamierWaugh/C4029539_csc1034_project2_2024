import csv #Requires csv reading import
from pathlib import Path #Imports relative path module
from booking import Booking

path = Path(__file__).parent / "../data/sample_data.csv" #Generates relative path
hashmap = {}
with path.open(mode="r") as f: #opens file as f using relative path
    csvF = csv.reader(f) #reads file using csv module
    i = 0
    for line in csvF: #iterates through every line
        hash[i] = Booking(line[0],str(line[1]) + str(line[2]),line[3],line[4],line[5])
        i += 1
print(hashmap[1].room) #Example output of hashmap / table

