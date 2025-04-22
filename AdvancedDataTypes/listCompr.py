# todo sqaure of a given list
li = [1, 2, 3, 4]
ref = [i ** 2 for i in li] # list Comprhension
print(ref) # [1, 4, 9, 16]

# todo print list of even no.
print([i for i in li if i % 2 == 0]) # [2, 4]

# todo add 5 to each element of li
print([i + 5 for i in li]) # [6, 7, 8, 9]