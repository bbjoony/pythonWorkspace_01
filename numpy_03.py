import numpy as np

a = ([1,2,3,4,5], [2,3,4,5,6])
len_a = len(a)
# type_a = a.type()

print(a)
print(len_a)
print(type(a))

b = np.zeros((2,10))
c = np.ones((2,10))
d = np.arange(2,10)
e = np.transpose(a)

print(d)
print(e)