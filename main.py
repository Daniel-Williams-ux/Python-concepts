name = 'dan'
age = 20
number = [1, 2, 3]
print(name)
print(age)
print(number)
#python doesn't use semi-colon like JS


#DATA TYPES
brand = "devdan"
age = 23
pi = 3.14
numbers = []
isAdult = True
print(type(brand)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(pi)) #<class 'float'>
print(type(numbers)) #<class 'list'>
print(type(isAdult)) #<class 'bool'>


# Comments
# use the pound/hash sign or the quote sign from multi-line comments

# Ask the user to enter name
name = input('What is your name: ' )
print('Hello', name)



# Ask the user to input 2 values and sore them in variables num1 num2
num1, num2 = input('Enter two numbers: ').split()

# Convert the strings into regular number integers
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum
sum = num1 + num2

# Subtract the values entered and store in difference
difference= num1 - num2

# Multiply the values entered and store in product
product = num1 * num2

# Divide the values entered and store in quotient
quotient = num1 / num2

# use modulos on the values to find the remainder
remainder = num1 % num2

# print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
