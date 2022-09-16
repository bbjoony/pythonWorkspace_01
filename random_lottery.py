import random

my_list = [] 

for i in range(6):
    a = random.randint(1,46) #실제 배열 안에 기록될 랜덤한 숫자 'a'
    
    while a in my_list: 
        a = random.randint(1, 46)
    my_list.append(a)
       
print(my_list)