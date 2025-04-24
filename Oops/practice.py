class Students:
    name = "Tarun"
    age = 22

    def study(self):
        print("tarun is studying")

s1 = Students()
s2 = Students()
print(s1.name)
print(s2.name)
s1.study()
s2.study()

'''
1. The methods which are present inside the class are caled as Instance(object) methods.
2. For instance methods, self parameter is must.
'''