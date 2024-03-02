class Car(object):


    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started.....")

    def stop(self):
        print("Car stopped")

#create instance of car

c = Car()
c.drive()
c.stop()

print('*'*20)
#let's say we have a different variety of cars
#let's say we have some common functionality or unique functionality to those cars

class Car(object):


    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started.....")

    def stop(self):
        print("Car stopped")

class BMW(Car):

    #here BMW became the child class or derived from parent class "Car"
    def __init__(self):
 #in init there is a warning- "this inspection warns if call to super construction in class is missed
#the base class is super class for the derived class
        Car.__init__(self)
 # we are just calling the init method of the car class
        print("You just created the BMW instance")


c = Car()
c.drive()
c.stop()

#here inheriting the property from parent class
b = BMW()
b.drive()
b.stop()

