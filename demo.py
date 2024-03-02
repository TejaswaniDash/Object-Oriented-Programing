"""
Object Oriented Programming

in py everything is an object, python manipulate everyting as object
object in term of programming is data structure

#Here, we will see how do we create classes,
what are the attributes and the member variables,
and what are the methods inside classes, h
ow inheritance works in Python, and all those sort of things.
"""

#define a string

s = "this is a string"
s.upper()   #control click it to see buit-in
s.lower()
#these are the methods , stay in string class

print(type('s'))  #s here is the instance of that class or object string
print(type('a'))
#when we create our own objects or our own classes and we create instances of
#those things then we get the type that going to refer to our ownclass and object
#we use class keyword to do that

"""
CREATE YOUR OWN OBJECT

Class - Blueprint / template that defines the object
"""

class Car(object):

    #def __init__(self):  #this required in class
        #used to initialise attribute in an object
    #__init__ is one of the method
    # let's add model as an instance to the attribute
    # let's add a default model= 550i
    def __init__(self, make, model= '550i'):
        self.make_car = make
        self.model_car = model
#here the car class is inheriting the object class
#now we are creating instance of the class
c1 = Car("bmw") #outside
print(c1.make_car)
print(c1.model_car)

c2 = Car("benz") #outside
print(c2.make_car)
print(c2.model_car)

#'c1' and 'c2' is not the instance,
# it's the reference variable that accesses the instance in the memory
#creating two different instances, passing two different values for self. make attribute.
#And how does it know that when I use 'c1',
# it should print "bmw", and when I use 'c2' it should print "benz",
# because when we created the reference variable,
# we passed on this "bmw" to this class, and it assigned self .make as "bmw",
# so self is referring to that instance

"""
CREATE YOUR OWN METHOD

"""

print('*'*20)

class Car(object):
    def __init__(self, make, model):
        self.make = make
        self.model = model

#init is a buit-in method
#here we are creating our own method for car class that will give information about car class

    def info(self):
        print("Make of the car:" + self.make)
        print("Model of the car:" + self.model)
        #create an utility method

c1 = Car("bmw" , "550i")
c1.info()

c2 = Car("benz" , "E350")
c2.info()

print('*'*20)

#till now we were goint through the attributes of the property of class

#MEMBER VARIABLES

#print(c1.make) & print(c2.make) will give different value
#not provide all the information but only about the make of the class car
#let's see a common thing that is available to all the class- MEMBER VARIABLE
#what if we want same value for every instance


class Car(object):

    wheels = 4 #global value

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car:" + self.make)
        print("Model of the car:" + self.model)

print(Car.wheels)

c1 = Car("bmw" , "550i")
print(c1.make)
#c1.info()
print(c1.wheels)

c2 = Car("benz" , "E350")
print(c2.make)
#c2.info()
print(c2.wheels)

print('*'*20)

#let's see what will happen if we change the value of wheel in c1 instance

class Car(object):

    wheels = 4 #global value

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car:" + self.make)
        print("Model of the car:" + self.model)



c1 = Car("bmw" , "550i")
print(c1.make)
c1.wheels = 3
#c1.info()
print(c1.wheels)

c2 = Car("benz" , "E350")
print(c2.make)
#c2.info()
print(c2.wheels)

#let's see does the c1 change value affects the assigned global value
print(Car.wheels)



