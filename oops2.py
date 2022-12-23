class person:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def printout(self):
        print("My name is :",self.name,"and rollno is:", self.rollno)
        
person1=person("vidhi sanodiya","54")
person2=person("akriti sharma","04")

print(id(person1))
print(id(person2))

person1.printout()
person2.printout()



