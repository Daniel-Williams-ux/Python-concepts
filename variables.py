failed_subjects="2"
name='John'
print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
print(name + '  will need to redo ' + failed_subjects + '  courses.')
print(name + '  is doing well in geography.')

#console
>Dear Mrs Badger
›Your son John is failing 2 subjects.
›John will need to redo 2 courses.
›John is doing well in geography.

#variables can be assigned
failed_subjects="2"
name='John'
print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
print(name + '  will need to redo ' + failed_subjects + '  courses.')
name="Eric"
print(name + '  is doing well in geography.')

#console
›Dear Mrs Badger
›Your son John is failing 2 subjects.
›John will need to redo 2 courses.
›Eric is doing well in geography.

#Escaping string literals
#use double quotes
a="it's"
#or
b='it\'s'


#note here no 2.56 is not a string
failed_subjects=2.56
name='John'
print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' + str(failed_subjects) + ' subjects.')
print(name + '  will need to redo ' + str(failed_subjects) + '  courses.')
name="Eric"
print(name + '  is doing well in geography.')
print(type('hello'))
print(type(1))
print(type(1.64))
print(type(True))

#console
›Dear Mrs Badger
›Your son John is failing 2.56 subjects.
›John will need to redo 2.56 courses.
›Eric is doing well in geography.
›<class 'str'>
›<class 'int'>
›<class 'float'>
›<class 'bool'>

#Typcasting
a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'

print([a,b,c,d,e,f,g,h,i,j])

#console
›[1, 2, 3, 1.0, 2.5, 3.0, 4.23, '80s', '22', '3.01']

#note
c1 = int("3.4")   # c1 will be...  ›Traceback (most recent call last): ValueError: invalid literal for int() with base 10: '3.4'
                                    >!Error: Unknown error
#except this
c1 = int(float("3.4")) 
#console
>3


print('Variables & Datatypes - Exercise')
#Create appropriate Variables for Item name, the price 
#and how many you have in stock

item_name = 'widget'
price = 23.5
inventory = 100
print(item_name, price, inventory)
