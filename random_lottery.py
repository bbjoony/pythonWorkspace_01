from random import random
import pandas as pd
import random

my_list = []
maxvalue = 0
maxelement = 0

for i in range(100):
    my_list.append(random.randrange(0,46))

for i in set(my_list):
    if my_list.count(i) > maxvalue:
        maxelement, maxvalue = i, my_list.count(i)
        
print('제일 많이 나온 숫자는 %d, 등장 횟수는 %d 입니다.' % (maxelement, maxvalue))