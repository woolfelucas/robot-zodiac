import numpy as np
import pandas as pd

np.set_printoptions(suppress=True)

output_file_path = "./output.txt"
data_file_path = "./data.csv"

output_file = open(output_file_path, "w")

datafile = pd.read_csv(data_file_path)
arr = pd.DataFrame.to_numpy(datafile)

col_maxima = np.append([1],np.nanmax(arr[:,1:len(arr[0])], axis=0))

arr_norm = arr/col_maxima

def find_team_avgs(team_number, arr):
    arr_team = arr[arr[:,0]==team_number]
    return np.nanmean(arr_team, axis=0)

print(find_team_avgs(4039, arr_norm))