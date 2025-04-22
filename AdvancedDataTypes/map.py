li = [1, 2, 3, 4]

def square(ele):
    return ele * ele

res = map(square, li) # it excepts map(function, iterable object)

print(res) # getting map object(iterator obj created when you called the map fn above) <map object at 0x00000282CF24AE30>

print(list(res)) # converting to list [1, 4, 9, 16]

# todo convert string list to int list
li1 = ["10", "20", "30", "40"]
print(li1) # ["10", "20", "30", "40"]
newli1 = list(map(int, li1))
print(newli1) # [10, 20, 30, 40]

li2 = [1, 2, 3, 0]
# convert to float 
print(list(map(float, li2))) # [1.0, 2.0, 3.0, 0.0]

# convert to boolean
print(list(map(bool, li2))) # [True, True, True, False]