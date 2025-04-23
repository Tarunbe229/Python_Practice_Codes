s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6}
new_set = s1.symmetric_difference(s2)
print(new_set) # {1, 2, 6}

s2 = {1, 2, 3, 4, 5}
s4 = {1, 2, 3, 4, 5, 6}
print(s2.issubset(s4)) # True