import numpy as np
import pandas as pd 
import os, re

csv_test = pd.read_csv('quest.csv')
df = pd.DataFrame(csv_test)


df = df.replace(6,5)
print(df)

df.to_csv('quest_01.csv')