import numpy as np
import pandas as pd
from io import StringIO
# my_lst1=[1,2,3,4,5]
# # arr=np.array(my_lst1)
# # print(type(arr))
# # print(arr.shape)
# my_lst2=[2,3,4,5,6]
# my_lst3=[9,7,6,8,9]
# arr2=np.array([my_lst1,my_lst2,my_lst3])
# # print(arr2)
# # print(arr2.shape )
# # print(arr2.reshape(5,3))

# arr3=np.array([1,2,3,4,5,6,7,8,9])
# print(arr3[3])
# print(arr2[:,: ])
# print(arr2[0:2,0:2])
# print(np.arange(0,10,step=2))
# print(np.linspace(1,10,50))
# arr3[3:]=100 #copy function
# print(arr3)
# arr4=arr3
# arr4[3:]=500
# print(arr4)
# print(arr3 )
# val=2
# print(arr3<val)
# print(np.ones(4))
# print(np.ones((2,5),dtype=int))
# print(np.random.rand(3,3))
# print(np.random.randn(3,3))

df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=["column1","column2","column3","column4"])
print(df.head())
df.to_csv('test1.csv')
# accesing the elements has 2 ways
# 1. .loc   2. .iloc
print(df.loc['Row1'])
print(type(df.loc['Row1']))
print(df.iloc [0:3,0:2]) 
print(type(df.iloc [0:3,0:2]))
# to convert into an array
print(df.iloc[:,1:].values)
print(df.isnull().sum())
print(df['column1'].value_counts())
print(df['column1'].unique())

data=('a,b,c\n'
      '4,apple,bat\n'
      '8,orange,cow')
print(pd.read_csv(StringIO(data),index_col=False))
print(pd.read_csv(StringIO(data),usecols=['b','c'],index_col=False))
# df1=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)
# print(df1.head())
# df_excel=pd.read_exel('excel.xlsx')
# df_excel.to_pickle('df_excel')
# df.head()
# dfs=pd.read_html(url,match="mobile",header=0)