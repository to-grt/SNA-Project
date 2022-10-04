import os
from unittest import skip
import pandas as pd

directory = '.'

for filename in os.listdir(directory):
    if filename[-4:] != "json":
        continue
    print("filename= ", filename)
    file_pd = pd.read_json(filename)
    name = filename.split('.')[0]
    file_pd.to_csv (r"C:\Users\tgueu\Desktop\csv_files\\" + name + ".csv", index = False, header=True)