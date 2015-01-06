# Exercise 42: Is-A, Has-A, Objects, and Classes

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Animal has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        ## We are calling constructor of the class which we are extending (Person with a name)
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salomon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a Cat called satan
mary.pet = satan

## frank is an Employee whos salary is 120000
frank = Employee("Frank", 120000)

## frank has-a pet called rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salomon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
