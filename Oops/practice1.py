class Employee:
    company_name = "KodNest" # class variable
    
    def work(self):
        print(self.name, "is studying") # self holds the address of curent object
    def play(self):
        print(self.name, "is playing")

e1 = Employee()
e1.name = "Tarun" # Instance variables
e1.id = 100
e1.work()

e2 = Employee()
e2.name = "Bhooth"
e2.id = 101
e2.work()
e2.play()