d = {
    "name" : "Tarun",
    "age" : 22,
    1 : "Java",
    "bool" : True,
    "name" : "Tarun B E"
}
print(d, type(d))

print(d['name']) # Tarun B E
print(d["age"]) # 22
print()

for i in d:
    print(i) # Tarun B E 22 name age 1 bool (random keys and values)
print()

for i in d.keys():
    print(i, end = "-") # name-age-1-bool- (for keys)
print()

for i in d.values():
    print(i, end = "-") # Tarun B E-22-Java-True- (for values)
print()

for i in d.items():
    print(i) 
'''('name', 'Tarun B E')
('age', 22)
(1, 'Java')
('bool', True)''' # (we get tuples here)

'''
1.In Dictionary we can store Homogeneous(Data with similar Data Type) as well as 
Heterogeneous (Data with different Data Type) Type of Data.

2.Dictionary is an Ordered Collection of Data. Dictionary Maintains order of insertion in the output
as it is thats why we call it as ordered collection of Data.(before 3.8 Dictionary was an unordered collection of data)

3.In Dictionary we can Store duplicate values but keys don't. If we use to duplicate key then previous
keyed value will be re-write to as new value that comes from duplicate key.

4. Dictionary are Mutable, means once we declare the list we can modify it.
'''