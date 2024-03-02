"""
Define 3 methods in this class:
__init__()
nutrition()
fruit_shape()

Print anything you like in these methods.
"""

"""
Create one more class(Any fruit name)

This should inherit from the fruit class created above, 
this will become the child class and "Fruit" will be referred as parent class
 to this class
 
__init__()
nutrition()
color()

Print anything you like in these methods.
"""

"""
Create instances of these classes and call methods from them
call methods from the base class also using the instance of the child class
"""

class Fruit(object):


    def __init__(self):
        print("I am a fruit")

    def nutrition(self):
        print("I am full of vitamins")

    def fruit_shape(self):
        print("Every fruit can have different shape")

class Apple(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("I am an Apple")

    def nutrition(self):
        print("I am full of vitamin A")

    def color(self):
        print("I am red in color")


f = Fruit()
f.nutrition()
f.fruit_shape()

#here inheriting the property from parent class
a = Apple()
a.nutrition()
a.fruit_shape()
a.color()

