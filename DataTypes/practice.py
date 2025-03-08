s1 = "Code"
s2 = "World"
s3 = "Hello" 

print(s1, id(s1)) # Code 2372263783104
print(s2, id(s2)) # World 2372263782960

print("Address of C in s1:", id(s1[0])) # Address of C in s1: 140722510035520
print("Address of l in s2:", id(s2[3])) # Address of l in s2: 140722510037488

'''
Here the address of both l is same(i.e, the l object is pointed by same address)
even the object that is present in different strings -> Memory utilization is efficient
'''

print("Address of l in s3:", id(s3[2])) # Address of l in s3: 140722510037488
print("Address of l in s3:", id(s3[3])) # Address of l in s3: 140722510037488
print("Address of l in s2:", id(s2[3])) # Address of l in s3: 140722510037488

print("Address of o in s1:", id(s1[1])) # Address of l in s3: 140722510037632
print("Address of o in s2:", id(s2[1])) # Address of l in s3: 140722510037632
print("Address of o in s3:", id(s3[4])) # Address of l in s3: 140722510037632