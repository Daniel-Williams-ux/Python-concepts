#positions of string
msg='Welcome to Python 101: Strings'
print(msg.find('Python'))
#CONSOLE
›11


#Replace
msg='Welcome to Python 101: Strings'
print(msg.replace('Python','Java')) #two parameters: the one we want to repace and the the one replacing it
#CONSOLE
›Welcome to Java 101: Strings
 

#Strings are immutable. to change string you need to create a new one
msg='Welcome to Python 101: Strings'
print(msg.replace('Python','C'))
msg1=msg.replace('Python','C'))
print(msg1)
#CONSOLE
›Welcome to C 101: Strings

 
#Membership
msg='Welcome to Python 101: Strings'
print('Python' in msg)
#CONSOLE
›True

msg='Welcome to Python 101: Strings'
print('Python' not in msg)
#CONSOLE
›False


#string formating
name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color.lower() + '!'
#better written 
msg1 = f'[{name}] loves the color {color.lower()}!'
print(msg)
print(msg1)
#CONSOLE
›[TERRY] loves the color red!
›[TERRY] loves the color red!
