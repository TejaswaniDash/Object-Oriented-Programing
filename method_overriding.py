"""
let's imagine the scenario that my car BMW, which inherits from the Car class,
it drives, but it has some more features,
that needs to be implemented when the engine starts,
maybe auto start or like self start, or maybe lots of different things,
it might have a different engine or like V6 or V8 or different,
different kinds of things.

# for that reason, we can try my own drive() method,
"""

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
 # we are just calling the init method of the car class to resolve the warning
        print("You just created the BMW instance")

    def drive(self):
         print("You driving BMW, Enjoy....")

    def headup_display(self):
        print("This is a unique feature")

    def music_setup(self):
        print("Setup your settings to autoplay")



c = Car()
c.drive()
c.stop()

#here inheriting the property from parent class
b = BMW()
b.drive()
b.stop()
b.headup_display()
b.music_setup()

#we can use methods define in any base class, in any child class
#in parent class we can only call methods that are defined inside it.
#it is not allowed to call any method/attribute from child class

print('*'*20)
"""
Let's use some functionality from the base class, and overridden it. 
let's say my drive() thing,there are some basic functionalities in the drive() method. 
which happens in my drive() method of BMW class as well, 
let's say we want to add more functionality. 
Which means we don't want to completely override it, 
We still want to use whatever is there in the base class 
And then on top of it, we want to add more functionality. 
So how do we achieve that thing?
"""
class Car(object):


    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started.....")

    def stop(self):
        print("Car stopped")

class BMW(Car):
    def __init__(self):

        Car.__init__(self)
        print("You just created the BMW instance")

    def drive(self):

        #super().drive()
#this syntax is not just specific to this, what we can do is,
#in order to be more specific, what we can do is we can pass the name of the car class here, BMW, and then self, this is a more, it's just a better syntax for better practice.

        super(BMW, self).drive()
        print("You driving BMW, Enjoy....")
#not just for overriding/functionality
#it will call the method from base class and run whatever there in child class


    def headup_display(self):
        print("This is a unique feature")

    def music_setup(self):
        print("Setup your settings to autoplay")

#c = Car()
#c.drive()
#c.stop()

#here inheriting the property from parent class
b = BMW()
b.drive()
b.stop()
b.headup_display()
b.music_setup()
