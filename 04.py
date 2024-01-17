#List It is an ordered collection of elements enclosed in []
#It is mutable- so we can modify it

# l=[1,'Hello',3.14,True,[12,23,66]]
# print(l)
# l[0]=12     #Mutable
# print(l)
# print(type(l))
# print(l[1])

#indexing
# print(l[4])         #[12, 23, 66]
# print(l[4][1])      #23



#Slicing
# l=[1,'Hello',3.14,True,[12,23,66]]
# print(l[:3])
# print(l[::-1])      #[[12, 23, 66], True, 3.14, 'Hello', 1]
# print(l[0],l[3])
# print(l[:])         # elements beginning to end


# l=[11,21,31] 
# n=[3,4] 
# del l[1]    #[11, 31]
# del l[0:2]    #[31]
# del l
# print(l)

#Append

# l=[1,2,3]
# n=[3,4]
# l.append(n)
# print(l)
# l.append(5)
# l.append(6)
# l.append(8)
# print(l)
# l.append([6,9,10])
# m=['x','y','z']
# l.append(m)
# print(l)

#Extend

# l=[1,2,3]
# n=[3,4]

# l.extend(n)
# print(l)


#Insert

# l=[11,9]
# l.insert(1,200)
# print(l)


#Clear

# l=[1,9]
# l.clear()
# print(l)
# del l
# print(l)

#Remove

# l=[1,200,3]
# l.remove(200)
# print(l)


#Pop

# l=[1,200,3]
# l.pop()
# print(l)


#Count

# l=[1,200,3,200,1]
# print(l.count(200))


#Max

# l=[1,200,3]
# m=max(l)
# print(m)


#Min

# l=[1,200,3]
# m=min(l)
# print(m)


#Sort

# l=[1,200,3]
# l.sort()
# print(l)


#Reverse

# l=[1,200,3]
# l.reverse()
# print(l)


#Reverse sort

# l=[1,200,3]
# l.sort()
# l.reverse()
# print(l)
# l.sort(reverse=True)
# print(l)



# Repetition		
# print(l*2)

#Concatenation
# l=[11,21,31] 
# n=[3,4]
# print(l+n)

#Membership	
# l=[2,11,21,31] 	
# print(12 in l) 		

# Iteration
# l=[11,21,31]
# print(l) 
# for i in l:
#     print(i,end=' ')
    
#Comprehensive list
# l=[]
# for a in range(1,5):
#     x=eval(input('enter Value :'))
#     l.append(x)
# print(l)


#Zip function 
# l = [1, 2, 3, 4,6]
# l1 = [11, 12, 13, 14]
# for a, b in zip(l, l1):
# 	print(a,b,a+b)


#choice(L) 		picks a random item from L 
# from random import *
# l = [1, 2, 3, 4]
# print(choice(l))


# sample(L,n) 		picks a group of n random items from L 
# from random import *
# l = [1, 2, 3, 4,5,6,7,8,9]
# print(sample(l,3))


# shuffle 		Shuffles the items of L
# from random import *
# l = [1, 2, 3, 4]
# shuffle(l)
# print(l)


# Random Number
# from random import * 	
# x = randint(1,10) 		#Integer Random No
# print(x)
# x = uniform(1.0, 10.5)	 #Float Random Number
# print(x)

# from math import *		
# print(abs(-4.3)); 
# print(round(3.346,0)) 
# print(round(3.346, 1)) 	
# print(round(3.346, 2)) 
# print(round(3.946, 0)) 	
# print(round(345.2, -1)) 
# print(round(99.2, -1))
# print(round(365.2, -2))

# Join
# L = ['A', 'B', 'C']
# print(L)
# print(' ' . join(L) )
# print('' . join(L) )
# print(',' . join(L) )
# print('***' . join(L))

# m=[]
# l=[20,540,590,0]
# for a in l:
#     m.append(str(a))
# print(l)
# print(m)
# a=(" ".join(m))
# print(a)

#Print 2nd Position Digit Two Times
# l=['823','234','345','466','5755','6966']
# for a in l:
#     print(a[1]*2,end='')
# q1
# l=[23,234,345,6,5755,6966]
# count=0
# for a in l:
#     if a>50:
#         count=count+1
# print(count)

# q2
# l=[23,234,345,6,5755,6966]
# m=max(l)
# l.remove(max(l))
# n=max(l)
# print(m)
# print(n)
# l.append(m)
# x=min(l)
# l.remove(min(l))
# y=min(l)
# print(x)
# print(y)
# l.append(x)

# q3
# l=[]
# for a in range(1,5):
#     x=eval(input('enter Value :'))
#     l.append(x)
# print(l)
# count=0
# for a in l:
#     count=count+1
# print(count)
# print(l[-1])
# print(l[::-1])
# if 5 in l:
#     print('yes')
# else:
#     print('no')
# print(l.count(5))
# del l[0]
# del l[-1]
# print(l.sort())
# coun=0
# for a in l:
#     if a<5:
#         coun=coun+1
# print(coun)

# q4
# from random import * 
# avg=0
# l=[]	
# for a in range(1,21):
#     x = randint(1,100) 
#     l.append(x)
#     avg=avg+x
# avg=avg/20
# print(l)
# print(avg)
# l.sort()
# print(l[0])
# print(l[-1])
# print(l[1])
# print(l[-2])


# q5
# l=[8,9,10]
# l.insert(1,17)
# l.extend([4,5,6])

# del l[0]
# print(l)
# l.sort()
# m =l*2
# m.insert(3,25)
# print(m)

# q6
# l=[]
# for n in range(6):
    #  x=eval(input('enter number'))
#     if x>10:
#         x=10
#     l.append(x)
    
# print(l)

# q7
# l = []
# for a in range(50):
#     l.append(a)

# print(l)

# l = []
# for a in range(1,51):
#     l.append(a**2)

# print(l)

# l = []
# alpha = 'abcdefghijklmnopqrstuvwxyz'

# for i in range(1, len(alpha) + 1):
#     l.append(alpha[i - 1] * i)

# print(l)

# q8
# l = [3,1,4]
# l1 = [1,5,9]
# for a, b in zip(l, l1):
# 	print(a,b,a+b)

# q13
# word= input('enter a word')
# w=''.join(sorted(word))
# print(w)

# q9
# for i in range(11): 
#     print(1, end='')
#     for n in range(i):
#         print(0, end='')

# q11
# l=[]
# for n in range(6):
     
#      l.append(input('enter number'))
# print('+'.join(l))

# q10
# x = input('Enter some text: ')
# a = 0
# b = 0
# c = 0

# words = x.split()

# for word in words:
#     if word == 'a':
#         a += 1
#     elif word == 'an':
#         b += 1
#     elif word == 'the':
#         c += 1

# print(a + b + c)

# l=[]
# x=0
# while x!=5:
#     x=int(input('enter the choice: 1.push 2.pop 3.peek 4.display 5.exit'))
#     if x==1:
#        l.append(eval(input('enter a number')))
#     elif x==2:
#         if len(l)==0:
#             print('cannot pop')
#         else:
            
#             l.pop()
#     elif x==3:   
#         if len(l)==0:
#            print('cannot peek')
#         else:
#            print(l[-1])
#     elif x==4:
        
#        if len(l)==0:
#            print('cannot display')
#        else:
#            for n in range(len(l)):
#                print(l[n])
               
            
    
    

    

     
        
    


    
