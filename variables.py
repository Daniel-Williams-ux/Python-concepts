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
