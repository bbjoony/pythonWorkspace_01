import numpy as np

loss = [-750, -250]
profit = [100] * 18 #100값이 18개 들어있는 배열

cf = loss + profit
print(cf)
print(len(cf))

cashflow = np.array(cf)
print(cashflow)