# for n in range(11):
#     print('1',end='')
#     for i in range(n):
#         print('0',end='')
        

str='equation'
print(str)

l=[]
for n in range(len(str)):
    l.append(str[n])
print(l)
l.sort()
print(l)
print(''.join(l))


