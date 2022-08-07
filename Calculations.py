'''
HELLO WORLD
Calculations
Computers absolutely excel at performing calculations. The “compute” in their name comes from their historical association with providing 
answers to mathematical questions. Python performs addition, subtraction, multiplication, and division with +, -, *, and /.
'''
# Prints "500"
print(573 - 74 + 1)
 
# Prints "50"
print(25 * 2)
 
# Prints "2.0"
print(10 / 5)
'''
Notice that when we perform division, the result has a decimal place. This is because Python converts all ints to floats before performing division. 
In older versions of Python (2.7 and earlier) this conversion did not happen, and integer division would always round down to the nearest integer.

Division can throw its own special error: ZeroDivisionError. Python will raise this error when attempting to divide by 0.

Mathematical operations in Python follow the standard mathematical order of operations.
'''

print(2 / 0)
'''
console
Traceback (most recent call last):
  File "script.py", line 1, in <module>
    print(2 / 0)
ZeroDivisionError: division by zero
'''

#source: codecademy
