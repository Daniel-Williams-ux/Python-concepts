#Concatenation
#The + operator doesn’t just add two numbers, it can also “add” two strings! The process of combining two strings is called string concatenation. 
#Performing string concatenation creates a brand new string comprised of the first string’s contents followed by the second string’s contents 
#(without any added space in-between).

greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text
 
# Prints "Hey there!How are you doing?"
print(full_text)
#In this sample of code, we create two variables that hold strings and then concatenate them. But we notice that the result was missing a space between 
#the two, let’s add the space in-between using the same concatenation operator!

full_text = greeting_text + " " + question_text
 
# Prints "Hey there! How are you doing?"
print(full_text)
#Now the code prints the message we expected.

#If you want to concatenate a string with a number you will need to make the number a string first, using the str() function. If you’re trying to print() 
#a numeric variable you can use commas to pass it as a different argument rather than converting it to a string.

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
 
# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2
 
# Prints "I am 10 years old today!"
print(full_birthday_string)
 
# If we just want to print an integer 
# we can pass a variable as an argument to 
# print() regardless of whether 
# it is a string.
 
# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)
#Using str() we can convert variables that are not strings to strings and then concatenate them. But we don’t need to convert a number to a string for 
#it to be an argument to a print statement.

"""
Instructions
1.
Concatenate the strings and save the message they form in the variable message.

Now uncomment the print statement and run your code to see the result in the terminal!
"""
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

message = string1 + string2 + string3 + string4 + string5 + string6
print(message)
