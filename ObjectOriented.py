import matplotlib.pyplot as plt
import traceback


#Link to vid: https://www.youtube.com/watch?v=JeznW_7DlB0&list=WL&index=2&ab_channel=TechWithTim

######## Basics
class Person: #Could be parent to student
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __gt__(self, o):
        """Operator overload ">"

        Args:
            o (Person): The other person

        Returns:
            Bool: Is self older than Other
        """
        return self.age > o.age

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def getGrade(self): # Method
        return self.grade

class Course:
    def __init__(self, name, maxStudents):
        self.name = name
        self.maxStudents = maxStudents
        self.students = []
    
    def __add__(self, stud):
        """Operator Overloading "+"

        Args:
            stud (Student): Appending student to the list of students

        Raises:
            OverflowError: When maximum amount of students are attending the course
        """
        if len(self.students) < self.maxStudents:
            self.students.append(stud)
        else:
            raise OverflowError

Logging = []

s1 = Student('Rom', 23, 6)
s2 = Student('Steen', 22, 6)
s3 = Student('Moen', 27, 2)

c1 = Course('AlgDat', 2)
c2 = Course('Linmet', 5)

try:
    c1 + s1
    c1 + s2
    c1 + s3
except Exception:
    Logging.append(traceback.format_exc())


print('Following errors occured:')
for error in Logging:
    print(error)


#### Inheritance and Class attributes
print('\n\nInheritance and Class attributes')
class Animal:
    numOfAnimals = 0 #Static member in c++. Class attributes in Pyth
    def __init__(self, name, age):
        """Abstract Animal

        Args:
            name (String): Name of animal
            age (Int): Age of animal
        """
        self.name = name
        self.age = age
        Animal.numOfAnimals += 1
    
    def speak(self):
        """The sound the animal makes
        """
        print("I'm abstract af...")
    def show(self):
        print(f"My nam iz {self.name}, and I am {self.age} years old.")
        self.speak()

class Dog(Animal):
    def speak(self): #Called method. Overwrites parent class' fnc
        print('bark')

class Cat(Animal):
    def speak(self): #Called method
        print('meow')

c = Cat('Tim', 12)
d = Dog('Leo', 13)

c.show()
d.show()
print(d.numOfAnimals)

##### Static
class math:
    
    @staticmethod #Do sometin' but don't change
    def add5(x):
        return x + 5

print(math.add5(5))