friends = ['John','Michael','Terry','Eric','Graham']

print(friends[1],friends[4])
print(friends[:4])
print(friends[:])
print(len(friends))
print(friends.index('Eric')) #position of Eric
print(friends.count('Eric'))

#CONSOLE
›Michael Graham
›['Terry', 'Eric']
>['John', 'Michael', 'Terry', 'Eric', 'Graham']
>5
>3
>1


friends = ['John','Michael','Terry','Eric','Graham']
print(friends)
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)

#CONSOLE
›['John', 'Michael', 'Terry', 'Eric', 'Graham']
›['Eric', 'Graham', 'John', 'Michael', 'Terry']
›['Terry', 'Michael', 'John', 'Graham', 'Eric']
›['Eric', 'Graham', 'John', 'Michael', 'Terry']



friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
print(max(cars))
print(min(cars))
print(sumcars))
print(min(friends))
print(max(friends))

#console
›911
›2952
>130
›Eric
›Terry
