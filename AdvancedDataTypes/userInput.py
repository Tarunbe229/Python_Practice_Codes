userData = input('Enter elements seperated by space: ') # "1 1 2 3 4"
strList = userData.split() # ['1', '1', '2', '3', '4']
intList = []
for i in strList:
    intList.append(int(i))
print(intList)

# todo avg of list
print(sum(intList) / len(intList))

