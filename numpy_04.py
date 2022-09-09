import numpy as np

arr1 = np.array([[2,3,4], [6,7,8]])
arr2 = np.array([[12,23,14], [46,13,11]])
arr3 = np.array([100,200,300]) #It has a different size with upper arraies 
arr4 = np.array([1,2,3,4,5,6,7,8,9,10])
arr5 = np.array([[9], [3]])

shape_a = arr1.shape
shape_c = arr3.shape
shape_d = arr4.shape

# print(arr1)
# print(arr2)
# print(arr1/arr2)
# print(shape_a)
# print(shape_c)
# print(shape_d)

# print(arr1 + arr3) #arr3의 값이 arr1[0]과 arr1[1] 모두에 더해짐
print(arr1 + arr5) #행과 열의 크기가 모두 다르면 브로드캐스팅을 할 수 없음 -> 오류 발생 