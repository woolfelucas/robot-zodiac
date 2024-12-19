from classify import classify
import numpy

numpy.set_printoptions(suppress = True)

import pandas

# actual code starts here

output_file_path = "./output.txt"
data_file_path = "./data.csv"

output_file = open(output_file_path, "w")

datafile = pandas.read_csv(data_file_path)
arrays = pandas.DataFrame.to_numpy(datafile)

amp_max = max(filter(lambda x: not numpy.isnan(x), arrays[:, 1]))
amp_misses_max = max(filter(lambda x: not numpy.isnan(x), arrays[:, 2]))
speaker_max = max(filter(lambda x: not numpy.isnan(x), arrays[:, 3]))
speaker_misses_max = max(filter(lambda x: not numpy.isnan(x), arrays[:, 4]))
shuttle_max = max(filter(lambda x: not numpy.isnan(x), arrays[:, 5]))

amp = arrays[:, 1]/amp_max
amp_misses = arrays[:, 2]/amp_misses_max
speaker = arrays[:, 3]/speaker_max
speaker_misses = arrays[:, 4]/speaker_misses_max
shuttle = arrays[:, 5]/shuttle_max

print(amp, "\n", amp_misses, "\n", speaker, "\n", speaker_misses, "\n", shuttle)


def classify_individual():
    '''
    with open(data_file_path, newline='') as csvfile:
        dataCSV = csv.reader(csvfile)
        for lines in dataCSV:
            if lines[0].find("#") == -1:
                int_lines = [int(entry) for entry in lines]
                output_file.write(str(classify(int_lines))+"\n")
    print("classify_individual() complete, log:" + output_file_path)
    '''

    for i in arrays.shape[1]:



def get_team_list():
    with open(data_file_path, newline='') as csvfile:
        dataCSV = csv.reader(csvfile)
        teams = []
        for lines in dataCSV:
            if teams.count(lines[0]) == 0 and lines[0].find("#") == -1:
                teams.append(lines[0])
        print(teams)

def classify_average():
    with open(data_file_path, newline='') as csvfile:
        dataCSV = csv.reader(csvfile)
        for lines in dataCSV:
            if lines[0].find("#") == -1:
                break # FIX LATER AAAAUGH


#get_team_list()
classify_individual()

'''
def sort_output():
    with open("./output.txt")

'''