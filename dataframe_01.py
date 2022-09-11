import pandas as pd

data = {'name': ['Mark', 'Jane', 'Crhis', 'Ryan'],
        'age' : [33, 32, 45, 13],
        'score' : [91.3, 84.1, 98.1, 98]
        }

df = pd.DataFrame(data)
print(type(df))
print(df)

print(df.sum()) #각 열값을 모두 더함. Text도 하나로 모음. 