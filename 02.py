# print('a',end='')
# print('b',end='')
# print('cd'*5,end='')
# print('e',end='')

# print('a',end='')
# print('b',end='')
# print('c'*5,end='')
# print('d'*5,end='')
# print('e',end='')

# for n in range(8,90,3):
#          print(n)

# for n in range(100,1,-2):
#          print(n)

# x=1
# n=eval(input('enter a number  '))
# for a in range (2,n):
#     if n%a==0:
#         x=0
 
    
# if x==1:
#     print('prime')
# else:
#     print('not prime')

# a=0
# b=1
# n= eval(input('enter the number '))
# if n<0:
#     print('incorrect input')
# elif n==1:
#     print(b)
# else:
#     for x in range(1,n):
#         c=a+b
#         a=b
#         b=c
#         print(b)

n= eval(input('enter the number '))
sum=0
temp=n
while temp>0:
    digit =temp%10
    sum=sum+ digit**3
    temp =temp//10
    
if n==sum:
    print(n,'is an armstrong no.')
else:
    print (n,'is not an armstrong no')






