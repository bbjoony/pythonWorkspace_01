import numpy as np

discount = .05
cashflow = 100

def presentvalue(n):
    return(cashflow / ((1 + discount) ** n)) #n년이 지난 다음의 자산 가치

# print(presentvalue(1))
# print(presentvalue(2))

for i in range(20): #20년이 지나는 동안의 자산 가치를 출력함
    print(presentvalue(i))
    