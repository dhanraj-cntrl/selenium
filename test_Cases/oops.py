class Employee:     #class is blueprint of ob

    comp = "TCS"   #class variable

    def __init__(self,name,sal):   #constructor -it auto involved when ob is created
        self.name = name            #instance variable
        self.sal = sal              #instance variable

    def is_info(self):              #instance method -self belong to class
        print(self.name)
        print(self.sal)
        print(self.comp)
    @classmethod                    #class method
    def change_comp(cls,new):
        cls.comp = new
    @staticmethod
    def greeting():
        print("Hello")

ob1=Employee("Dhanraj",12000)
ob1.is_info()
Employee.change_comp("Infosys")
ob1.is_info()
#polymorphism - same method but diff behaviour
#method overloading/

def is_name(name=None):
    if name is not None:
        print("Hello")
    else:
        print("HelloHello")
is_name()
#method overiding
class RBI:
    def roi(self):
        print("9%")
class Bank(RBI):
    def roi(self):
        print("10%")

ob1=Bank()
ob1.roi()

#encapsulation:
#inheretence - multiple Inheretence -MRO
#list_comp -elegant way of difining new list wo changing existing list
#lambda  -anonymus function
#filter  -it applied condition
#map    - its applied on element
import copy
l1 = [12,23,34]

l2= copy.copy(l1)
l2[0] = 122
print(l2)
print(l1)

l1 = [12,23,34]

l2= copy.deepcopy(l1)
l2[0] = 122
print(l2)
print(l1)

file=open("C:\\Users\\DHANRAJ\\Downloads\\Sample.py.txt","r")
file.readline()
file.readlines()

#decorator  - it changes behaviour of a method wo changing code
#generator  - by using yield we can understand it

#posi args
#key args
#*args
#**kwargs

