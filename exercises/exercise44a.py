# Exercise 44: Inheritance Versus Composition (Part 1 - Inheritance)

# Implicit Inheritance

class ParentA(object):

    def implicit(self):
        print "PARENT A implicit()"

class ChildA(ParentA):
    pass

dadA = ParentA()
sonA = ChildA()

dadA.implicit()
sonA.implicit()

# Override Explicitly

class ParentB(object):

    def override(self):
        print "PARENT B override()"

class ChildB(ParentB):

    def override(self):
        print "CHILD B override()"

dadB = ParentB()
sonB = ChildB()

dadB.override()
sonB.override()

# Alter before of after

class ParentC(object):

    def altered(self):
        print "PARENT C altered()"

class ChildC(ParentC):

    def altered(self):
        print "CHILD C, BEFORE PARENT C altered()"
        super(ChildC, self).altered()
        print "CHILD C, AFTER PARENT C altered()"

dadC = ParentC()
sonC = ChildC()

dadC.altered()
sonC.altered()

# All three combined

class ParentD(object):

    def override(self):
        print "PARENT D override()"

    def implicit(self):
        print "PARENT D implicit()"

    def altered(self):
        print "PARENT D altered()"

class ChildD(ParentD):

    def override(self):
        print "CHILD D override()"

    def altered(self):
        print "CHILD D, BEFORE PARENT D altered()"
        super(ChildD, self).altered()
        print "CHILD D, AFTER PARENT D altered()"

dadD = ParentD()
sonD = ChildD()

dadD.implicit()
sonD.implicit()

dadD.override()
sonD.override()

dadD.altered()
sonD.altered()
