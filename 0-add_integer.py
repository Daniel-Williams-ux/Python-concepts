#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""

def addInt(a, b):
  if type(a) is not int and type(a) is not float:
    raise TypeError ("a must be an integer")
  if type(b) is not int and type(b) is not float:
    raise TypeError ("b must be an integer")
  if type(a) is float:
    a = int(a)
  if type(a) is float:
    b = int(b)
  return a + b
print(addInt(2, 3))

!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""

def addInt(a, b):
  if type(a) != int and type(a) != float:
    raise TypeError ("a must be an integer")
  if type(b) != int and type(b) != float:
    raise TypeError ("b must be an integer")
  if type(a) == float:
    a = int(a)
  if type(b) == float:
    b = int(b)
  return a + b
print(addInt(2, 3))