# s1 = "    Code   "
# print(s1.strip())

# s2 = "---Code--"
# print(s2.strip("-"))
# print(s2.lstrip("-"))
# print(s2.rstrip("-"))

num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
print(f"Addition of {num1} and {num2} is: {num1 + num2}") # Addition of 57 and 75 is: 5775

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print(f"Addition of {num1} and {num2} is: {num1 + num2}") # Addition of 34 and 34 is: 68

# WAC to accept string value from user and remove its trailing and leaading spaces
s1 = input("Enter string: ").strip()
print(s1)

s2 = "code with KodNest"
print(s2.find("with")) # 5
print(s2.replace("KodNest", "me!")) # code with me!
print(len(s2)) # 17
print(s2[7:9]) # th 7th to (9-1)th index