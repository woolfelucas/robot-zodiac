import json
import csv
from classify import classify

# actual code starts here

output_file_path = "./output.txt"
data_file_path = "./data.csv"

output_file = open(output_file_path, "w")

def classify_individual():
    with open(data_file_path, newline='') as csvfile:
        dataCSV = csv.reader(csvfile)
        for lines in dataCSV:
            if lines[0].find("#") == -1:
                int_lines = [int(entry) for entry in lines]
                output_file.write(str(classify(int_lines))+"\n")
    print("classify_individual() complete, log:" + output_file_path)

def get_team_list():
    with open(data_file_path, newline='') as csvfile:
        dataCSV = csv.reader(csvfile)
        teams = []
        for lines in dataCSV:
            if teams.count(lines[0]) == 0 and lines[0].find("#") == -1:
                teams.append(lines[0])
        print(teams)

def classify_average():
    with open(data_file_path, newLine='') as csvfile:
        dataCSV = csv.reader(csvfile)
        for lines in dataCSV:
            if lines[0].find("#") == -1:
                break # FIX LATER AAAAUGH

get_team_list()
classify_individual()

'''
def sort_output():
    with open("./output.txt")

'''