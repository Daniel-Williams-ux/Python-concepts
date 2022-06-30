msg='welcome to Python 101: Strings'
print(msg+msg)
#console
>welcome to Python 101: Strings
  
#Another way
msg='welcome to Python 101: Strings'
print(msg+msg)
#CONSOLE
›welcome to Python 101: Stringswelcome to Python 101: Strings
    
#Also
msg='welcome to Python 101: Strings'
print(msg*2)
#CONSOLE
›welcome to Python 101: Stringswelcome to Python 101: Strings
    
#Also with a comma(Here it separate the strings
msg='welcome to Python 101: Strings'
print(msg,msg)
#CONSOLE
›welcome to Python 101: Strings welcome to Python 101: Strings
    
#string methods
msg='welcome to Python 101: Strings'
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
#console
›welcome to Python 101: Strings
›WELCOME TO PYTHON 101: STRINGS
›welcome to python 101: strings
›Welcome to python 101: strings
›Welcome To Python 101: Strings
  
#This will fail
msg='welcome to it\'s Python 101: Strings'
print(msg.title())
#console
›Welcome To It'S Python 101: Strings


#Length of string/count letters
msg='welcome to Python 101: Strings'
print(msg)
print(len(msg))
print(msg.count('o'))
#console
›welcome to Python 101: Strings
>3


#Slicing
msg='welcome to Python 101: Strings'
print(msg[0])
print(msg[1])
print(msg[2])
print(msg[-1])
print(msg[-2)
print(msg[2:])
print(msg[2:7]) #slice from index 2 upto 7 not inclusive 
print(msg[:7])
#console
>w
>e
>l
>s
>g
>lcome to Python 101: Strings
›lcome
›welcome
          
          
          
msg='welcome to Python 101: Strings'
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title())
print(msg1[::-1].title()) #reverse the string
#CONSOLE
›1 Welcome Ring To Tyler
›Relyt Ot Gnir Emoclew 1
