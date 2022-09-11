import pandas as pd
import os, re

df = pd.read_csv('apt.csv', encoding = 'cp949')
print(len(df))

df.head()