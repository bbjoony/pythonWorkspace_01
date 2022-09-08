import numpy as np

a = ([1,2,3,4,5], [2,3,4,5,6])
len_a = len(a)
# type_a = a.type()

print(a)
print(len_a)
print(type(a))

b = np.zeros((2,10))
c = np.ones((1,10))
d = np.arange(2,10)
e = np.transpose(a)

len_c = len(c) #열값만 출력함(몇 개의 열이 있는지로 length를 측정)
len_e = len(e)

print("b=", b)
print("c=", c, len_c)
print("d=", d)
print("e=", e, len_e)