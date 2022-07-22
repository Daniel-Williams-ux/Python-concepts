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


#We can customize it
try:
    num=int(input('Enter a number: '))
    print("30 divided by",num, "is: ", 30/num)
except ValueError:
    print("Bad value!")
print("**Thank you for playing!**")

#More
try:
    num=int(input('Enter a number: '))
    print("30 divided by",num, "is: ", 30/num)
except ZeroDivisionError:
    print("You can't divide by Zero!!!")
print("**Thank you for playing!**")


#you can be more specific
try:
    num=int(input('Enter a number: '))
    print("30 divided by",num, "is: ", 30/num)
except ZeroDivisionError as err:
    print(err, "You can't divide by Zero!!!")
print("**Thank you for playing!**")


#more
try:
    num=int(input('Enter a number: '))
    print("30 divided by",num, "is: ", 30/num)
except ZeroDivisionError as err:
    print(err, "You can't divide by Zero!!!")
except ValueError as err:
    print(err, "Bad Value!")
except:
    print("Invalid Input!")
print("**Thank you for playing!**")


#if everything goes smoothly without the error, we add our 'else' and 'finally' statement.
try:
    num=int(input('Enter a number: '))
   num1 = 30/num
except ZeroDivisionError as err:
    print(err, "You can't divide by Zero!!!")
except ValueError as err:
    print(err, "Bad Value!")
except:
    print("Invalid Input!")
else:
    print("30 divided by",num, "is: ", 30/num)
finally:
    print("**Thank you for playing!**")
