def greeting():
    print("Hello Friend!")
    
greeting()
#CONSOLE
›Hello Friend!


def greeting(name,age):
    print("Hello " + name + ", you are " + age + "!")
    print(f"Hello {name}, you are {age}!")
    
greeting("Brian","32")
#CONSOLE
›Hello Brian, you are 32!
›Hello Brian, you are 32!


#We can set a default age
def greeting(name,age="28"):
    print("Hello " + name + ", you are " + age + "!")
    print(f"Hello {name}, you are {age}!")
    
greeting("Brian","32")
greeting("Judith")
#CONSOLE
›Hello Brian, you are 32!
›Hello Judith, you are 28!


#input value
def greeting(name,age="28"):
    print(f"Hello {name}, you are {age}!")

name = input("Enter your name: ")    
greeting(name,"32")


#using integers not strings
def greeting(name,age=28):
    print("Hello " + name + ", you are " + str(age) + "!")
    print(f"Hello {name}, you are {age}!") #using formatted string is much more easier

name = input("Enter your name: ")    
greeting(name,32)
greeting("Judith")
#CONSOLE
›Hello Peter, you are 32!
›Hello Judith, you are 28!

