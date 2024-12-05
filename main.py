import json
import csv
from classify import classify

# general-types.json is unused for now because bugs
general_type_json = {
    "generalist-true":{
        "amp-min":0.25,
        "amp-max":0.40,
        "speaker-min":0.25,
        "speaker-max":0.4,
        "shuttle-min":0.25,
        "shuttle-max":0.4
    },
    "generalist-attacker":{
        "amp-min":0.35,
        "amp-max":0.65,
        "speaker-min":0.35,
        "speaker-max":0.65,
    },

    "amplifier":{
        "amp-min":0.51
    },

    "shooter":{
        "speaker-min":0.51
    },

    "trucker":{
        "shuttle-min":0.51
    }
}



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


#file = open("general-types.json")

#general_types = json.load(file)

#for i in general_types["generalist-true"]:
#    print(i)

#json.close()

