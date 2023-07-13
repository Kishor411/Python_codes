#/usr/bin/python3
class student:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    
    def talk(self):
        print("Hello I am ", self.name)
        print("My Age is ", self.age)
        print("My City is ", self.city)
s1=student("Kishor",29,"Pune")
s1.talk()
