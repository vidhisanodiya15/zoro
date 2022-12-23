#class person:
  #  def __init__(self):
    #    self.name= "shubham"
    #    self.age= 18

   # def updateName(self):
    #    self.name="vidhi"

   # def compareAge(self,other):
   #     if self.age == other.age:
     #       return True
     #   else: 
     #       return False

#person1=person()
#person2=person()

#person2.name="atul"
#person1.updatename("ABC")

#person1.age = 22

#if person1.compareAge(person2):
  #  print("They are of same age")
#else: 
  #  print("They are of different age")

#print(person1.name,person1.age)
#print(person2.name,person2.age)

#type of name that chnge with object is known as instance

class car:
    wheels=4
    def __init__(self,brand,mil):
     self.brand=brand
     self.mil=mil
car1=car("BMW",10)
car2=car("TESLA",8)

car.wheels=3

print(car1.brand)
print(car2.brand)

print(car1.brand,car1.mil,car1.wheels)
print(car2.brand,car2.mil,car2.wheels)