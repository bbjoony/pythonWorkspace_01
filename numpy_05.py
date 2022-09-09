import numpy as np

d = np.array([[1,2,3,4,5,],[2,4,5,6,7,],[5,7,8,9,10]]) #이건 배열
d_list = [[1,2,3,4,5], [2,4,5,6,7,], [5,7,8,9,10]] #이건 list

print(type(d))
print(type(d_list))

#d_list[:2] = 0
d[:2, :2] = 0

#print(d_list)
print(d)