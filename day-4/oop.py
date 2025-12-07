#oops -object oriented programming is a programming paradigm based on the concept of "objects"
#which can contain data and code: data in the form of fields (often known as attributes
#or properties), and code, in the form of procedures (often known as methods).

#class - blueprint 
#object - instance of class

class student:
    subject = "maths"  #class variable
    college ="ABC college"
    year = 2024
    
stu1 =student()  #object creation
stu2 =student()
print(stu1.subject, stu1.college, stu1.year)


class CollegeStd:
    def __init__(self,name,cgpa):
        self.name = name  #instance variable
        self.cgpa = cgpa
        
    def get_cgpa(self):
        return self.cgpa
        
std1 = CollegeStd("monu", 9.5)
print(std1.name, std1.cgpa)

std2 = CollegeStd("vikas", 8.5)
print(std2.name, std2.cgpa)

print(f"{std1.name} has cgpa {std1.get_cgpa()}")
print(f"{std2.name} has cgpa {std2.get_cgpa()}")


#types of constructor
#default constructor
#parameterized constructor
#copy constructor

def __init__(self):
    print("default constructor called")
    
def __init__(self, name, cgpa):  #parameterized constructor
    self.name = name
    self.cgpa = cgpa
    
    
def __init__(self, other):  #copy constructor
    self.name = other.name
    self.cgpa = other.cgpa


#class and instance attribute

#class attribute - attribute shared by all objects of the class
#instance attribute - attribute unique to each object of the class


class students1:
    college_name = "ABC college"  #class attribute
    
    def __init__(self, name, cgpa):
        self.name = name  #instance attribute
        self.cgpa = cgpa
        
stu3 = students1("pal", 9.0)

  #accessing class attribute
print(stu3.college_name)
print(stu3.name, stu3.cgpa)
print(students1.college_name)  #accessing class attribute without object

#methods
#instance method -its parameter is self which refers to the current object
#access the class and instance atttributes using self
class Laptop:
    storage_types =  "SSD"  #class attribute
    
    def __init__(self,RAM,storage):
        self.RAM = RAM  #instance attribute
        self.storage = storage
        
    def get_specs(self):  #instance method
        print(f"RAM: {self.RAM}, Storage: {self.storage} and Storage types: {self.storage_types}")
    
l1= Laptop("8GB",512 )
l2=Laptop("16GB", 256)
    
l1.get_specs()
 
#class method its param cls which refers to the class itself
#access class attributes using cls
#use @classmethod decorator to define class method

class Laptop:
    storage_types =  "SSD"  #class attribute
    
    def __init__(self,RAM,storage):
        self.RAM = RAM  #instance attribute
        self.storage = storage
        
    @classmethod
    def get_storage_types(cls):  #class method
        print(f"Storage types: {cls.storage_types}")  #cls.storage_types)  #cls.storage_types
        
    def get_specs(self):  #instance method
        print(f"RAM: {self.RAM}, Storage: {self.storage} and Storage types: {self.storage_types}")
    
l1= Laptop("8GB",512 )
l2=Laptop("16GB", 256)
    
#l1.get_specs()
l1.get_storage_types()


#static method
#does not take self or cls as parameter
#use @staticmethod decorator to define static method

class Laptop:
    storage_types =  "SSD"  #class attribute
    
    def __init__(self,RAM,storage):
        self.RAM = RAM  #instance attribute
        self.storage = storage
        
    @staticmethod
    def calc_discount(price,discount):  #static method
        final_price = price - (price * discount /100)
        print(f"Final price after {discount}% discount is {final_price}")
        
    def get_specs(self):  #instance method
        print(f"RAM: {self.RAM}, Storage: {self.storage} and Storage types: {self.storage_types}")
    
l1= Laptop("8GB",512 )  
l2=Laptop("16GB", 256)

#l1.get_specs()
Laptop.calc_discount(50000,10)
Laptop.calc_discount(80000,15)

