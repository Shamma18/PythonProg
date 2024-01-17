import numpy as np
my_lst1=[1,2,3,4,5]
# arr=np.array(my_lst1)
# print(type(arr))
# print(arr.shape)
my_lst2=[2,3,4,5,6]
my_lst3=[9,7,6,8,9]
arr2=np.array([my_lst1,my_lst2,my_lst3])
# print(arr2)
# print(arr2.shape )
# print(arr2.reshape(5,3))

arr3=np.array([1,2,3,4,5,6,7,8,9])
print(arr3[3])
print(arr2[:,: ])
print(arr2[0:2,0:2])
print(np.arange(0,10,step=2))
print(np.linspace(1,10,50))
arr3[3:]=100 #copy function
print(arr3)
arr4=arr3
arr4[3:]=500
print(arr4)
print(arr3 )
val=2
print(arr3<val)
print(np.ones(4))
print(np.ones((2,5),dtype=int))
print(np.random.rand(3,3))
print(np.random.randn(3,3))


