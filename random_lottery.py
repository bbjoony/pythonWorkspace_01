import random

my_list = []

for i in range(6):
    a = random.randint(1,46)
    while a in my_list:
        a = random.randint(1, 46)
    my_list.append(a)
       
print(my_list)