li = [1, 4, 2, 10, 9]
li.sort()
print(li) # [1, 2, 4, 9, 10]

li1 = [10, 40, 2, 10, 90]
sorted(li1) # creates another object so need referece
print(li1) # [10, 40, 2, 10, 90]
"""so we have to use ref var"""
print(sorted(li1)) # [2, 10, 10, 40, 90]
sortedli = sorted(li1) # [2, 10, 10, 40, 90]