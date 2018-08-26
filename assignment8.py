#ques 1
import math
class circle:
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return math.pi * (self.radius ** 2)
    def getCircumference(self):
        return 2 * math.pi * self.radius
r = int(input("Enter radius of circle: "))
obj = circle(r)
print("Area of circle:", round(obj.getArea(), 2))
print("circumference of circle:", round(obj.getCircumference(), 2))

#ques 2
import math
class Student:
    def __init__(self,name,roll_number):
       self.name=name
       self.roll_number=roll_number
       self.age=0
       self.marks=0
    def setAge(self):
       self.age=int(input("enter age:"))
    def setMarks(self):
        self.marks=int(input("enter marks:"))
    def Display(self):
        print("NAME->"+self.name,"AGE->"+str(self.age),"ROLL NUMBER->"+str(self.roll_number),"MARKS->"+str(self.marks),sep="\n")
Student_one=Student("pawan",1610991609)
Student_one.setAge()
Student_one.setMarks()
Student_one.Display()

#ques 3
class Temperature:
    def __init__(self,temp):
        self.temperature=temp
    def convertFahrenheit(self):
        return self.temperature*(9/5)+32
    def convertCelcius(self):
        return (self.temperature-32)*5/9
temp=int(input("enter temperature:"))
obj=Temperature(temp)
print("Temperature in Fahrenheit",obj.convertFahrenheit())
print("Temperature in Celcius",obj.convertCelcius())

#ques 4
class MovieDetails:
    def __init__(self,artistname,year_of_release,ratings):
        self.artistname=artistname
        self.year_of_release=year_of_release
        self.ratings=ratings
        self.movieNAME=0
    def Add(self):
        self.movieNAME=input("enter movie name:")
    def Display(self):
        print("MOVIE NAME->"+self.movieNAME,"ARTIST NAME->"+str(self.artistname),"YEAR OF RELEASE OF THE MOVIE IS->"+str(self.year_of_release),"MOVIE'S RATINGS->"+str(self.ratings),sep="\n")
obj=MovieDetails("abcd",1995,3.5)
obj.Add()
obj.Display()

#ques 5
class Animal:
    def __init__(self,animal_attribute=20):
        self.animal_attribute=animal_attribute
class Tiger(Animal):
    def display(self):
        print(self.animal_attribute)
obj=Tiger()
obj.display()

#ques 6
#answer of question 6 is A B
#                        A B
print("The output of question number 6 -> A B")
print("                                   A B")

#ques 7
class Shape:
    def __init__(self,length):
        self.length=0
        self.breadth=0
        self.t=()
    def setValues(self):
         self.length=int(input("enter length:"))
         self.breadth = int(input("enter breadth:"))
    def Area(self):
            if self.length==self.breadth:
                 print("area of square:",self.length*self.breadth)
            else:
                 print("area of rectangle:",self.length*self.breadth)
class square(Shape):
    def __init__(self):
        self.setValues()
        self.Area()
class rectangle(Shape):
    def __init__(self):
        self.setValues()
        self.Area()
sq=square()
rc=rectangle()


