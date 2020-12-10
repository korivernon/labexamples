class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


class Student(Person):
    def __init__(self, fname, lname, height=0):
        Person.__init__(self, fname, lname)
        self.height = height

    def printEverything(self):
        print(self.firstname, self.lastname, self.height)

x = Student("Mike", "Olsen")
x.printname()
x.printEverything()
y = Student("Kori", "Vernon", 70)
