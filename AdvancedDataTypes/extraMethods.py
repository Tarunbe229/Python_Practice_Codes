# li = "This is a test. This test is simple."
# li = s1.replace(".", " ")
# print(s1.count(' is '))

"""or using dictionary"""
li = "This is a test. This test is simple.".replace(".", "").split()
di = {}
for i in li:
    if i in di:
        di[i] = di[i] + 1
    else:
        di[i] = 1
print(di)
'''or'''
for key in di:
    print(f"{key}: {di[key]}")

