# indexing

# str="My Name is Python"
# print(str[0])
# print(str[-1])
# print(str[1])

# Slicing
# str="MyNameispython"
# print(str[1:])      #1 to Last
# print(str[0::2])
# print(str[::-1])   #Reverse
# print(str[0:4])     #0-3
# print(str[:3])      #0-2
# print(str[::-1])    #Reverse
# print(str[-5:-1])   
# print(len(str))
# print(str.lower())
# str1=str.lower()
# print(str1)

# print(str)

# print(str.upper())
# print(str.replace('Na', 'XYZ'))  #Temp Change Not Permanent
# print(str)
# print(str.count('a'))           
# print(str.find("Name"))         #
# print(str.find("name"))         #Gives 

# str[0]="m"
# print(str)            #immutable #str'
# str="my name is Python"
# print(str.title())      
# str="my name is Python"
# print(str.capitalize())


# print(str.index('y'))
# str="My"
# print(str.isalpha())    #True

# str="My "
# print(str.isalpha())    #False

# str="122"
# print(str.isdigit())

# str="s2323"
# print(str.isalnum())


# str="i like apples,mango,banana"
# print(str.split(','))           #['i like apples', ' mango', ' banana']


# str="this is my ipad i like it"
# print(str.split('s'))           #['thi', ' i', ' my ipad i like it']

#sort alphabetically the words 

# my_str = "Jasmine,Mehak,Gurneet,Gurbir,Abhinav"
# words = my_str.split(',')
# print(my_str)
# print(words)
# print(words[2])
# words.sort()
# print("The sorted words are:")
# print(words)
# words.reverse()
# print(words)

# str = "My Name is Python"
# print(str)
# for a in range(len(str)):
#     print(str[a],end='')
# for a in str:
#      print(a) 

# words = str.split(' ')
# print(words)
# for a in range(len(words)):
#     print(words[a] ,end=' ')
# for a in words:
#    print(a,end=' ')

# str="pop"
# s=str[::-1]
# if str==s:
#     print(str)
# else:
#     print('not a palindrome')

# n=101
# count=0
# for a in range(n):
#     x=a**2
#     if x%10 ==1 :
#         count=count+1       
# print(count)

# n=101
# count=0
# count1=0
# for a in range(n):
#     x=a**2
#     if x%10==4 :
#         count=count+1
#     if x%10==9:
#         count1=count1+1
# print('ending with 4 is ',count)
# print('ending with 9 is ',count1)

# str = input('enter the string ')
# print(len(str))
# print(str*10)
# print(str[0])
# print(str[0:4])
# print(str[-4:-1])
# print(str[::-1])
# print(str[8])
# print(str[1:-1])
# print(str.upper())
# print(str.replace('a','e'))


# str = input('enter the string ')
# print(str.count(' ')+1)

# str = input('enter the string ')
# if(('a'in str)or ('e'in str) or('i'in str)or('o'in str)or('u'in str)):
#     print('true')
# else:
#     print('false')

# str = input('enter the string ')
# print(str.replace(str[1],'*'),end='!!!')

# str = input('enter the string ')
# print(str.lower())

# str= str.replace('.',' ')
# str= str.replace(',',' ')
# print(str) 

# str = input('enter the string ')
# for a in str:
#     print(a*2,end=' ')


# num = int(input("Enter a number: "))
# for n in range(1, num + 1):
#     print(" " * (n-1) + str(n))

# str=input('enter the word ')
# x=str.find('a')
# print(str[0:x+1])
# print(str[x+1:])

# str = "ELVIS"
# for i in range(len(str)):
#     print(str[:i+1], end=" ")

# str='hello'
# for n in range(len(str)):
    
#     print(str[n:],str[:n],sep='')
    

# def reset():
#     global x
#     x=0
# def sum():
#     print(x)
# x=100
# sum()
# reset()
# print(x)
    