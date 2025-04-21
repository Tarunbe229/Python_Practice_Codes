t1 = (10, 20, True, 'Code')
print(t1, type(t1))

print(t1[0]) # 10
print(t1[3]) # True

# t1[0] = 300 // not allowed(can't modify)
print(t1)

t2 = (10, 20, 30, 40, 50)
e1, e2, e3, e4, e5 = t2
print(f"e1: {e1}, e2: {e2}, e3: {e3}, e4: {e4}, e5: {e5},")

tup1 = (10, 20)
tup2 = (30, 40)
newtup = tup1 + tup2
print(newtup) # (10, 20, 30, 40)
print(len(newtup)) #4

"""
1.In Tuple we can store Homogeneous(Data with similar Data Type) as well as 
Heterogeneous (Data with different Data Type) Type of Data.

2.Tuple is an Ordered Collection of Data. Tuple Maintains order of insertion in the output
as it is thats why we call it as ordered collection of Data.

3.In Tuple we can Store duplicate values.

4. Tuples are Immutable, means once we declare the list we cannot modify it.
"""