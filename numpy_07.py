import numpy as np
import pandas as pd 
import os, re

#os.chdir(r '../Users/devsiters/Documents/GitHub/pythonWorkspace_01')
#quest = np.array(usecsv.switch(usecsv.opencsv('quest.csv')))

# with open("quest.csv") as file_name:
#     array = np.loadtxt(file_name, delimiter=",")

csv_test = pd.read_csv('quest.csv')
print(csv_test)

csv_test_01 = csv_test > 5
type_d = type(csv_test_01)
print(csv_test_01)
print(type_d)