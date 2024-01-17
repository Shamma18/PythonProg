# f=open('abc.txt','a')
# content='\nWelcome to tcl hjkhk djhk '
# f.write(content)
# print('saved')
# f.close()



f = open("abc.txt",'r')   
print(f.read())

# get the current file position
print(f.tell())
# Set the current file position
print(f.seek(130))
print(f.read())

f.close()