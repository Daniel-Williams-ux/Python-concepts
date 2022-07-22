print("Errors: Try/Except")

#try:
    #code you want to run
#except:
    #executed if error occurs
#else:
    #executed if no error
#finally:
    #always executed 

    
num=int(input('Enter a number: '))
print("30 divided by",num, "is: ", 30/num)
print("**Thank you for playing!**")

#Handling error message
#for example you enter string in tne input 
try:
    num=int(input('Enter a number: '))
    print("30 divided by",num, "is: ", 30/num)
except:
    print("Invalid Input!")
print("**Thank you for playing!**")
