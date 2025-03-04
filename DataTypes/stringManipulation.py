s1 = 'code with me'
print(s1[0]) # 0th index value from s1 String
print(s1[1]) # 1st index value from s1 String....

print("Length of s1 is:", len(s1)) #12

print(s1[-1]) # e
print(s1[-2]) # m

# String Slicing: Creating sub Strin from main string
sub_str = s1[0 : 3] # str[start index : end index - 1]
print(sub_str) # cod

print(s1[3 : 6]) # e w

print(s1.upper()) # CODE WITH ME

# Strings are immutable
s1.upper()
print(s1) # code with me

s2 = s1.upper() # Reference variable needed to print
print(s2) # CODE WITH ME
print(s2.lower())