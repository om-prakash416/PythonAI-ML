#oop Pillars in Python
#1. Encapsulation - wrapping data and methods into a single unit (class)
#2. Abstraction - hiding complex implementation details and showing only the necessary parts to the user
#3. Polymorphism - ability of different objects to respond to the same method call in different ways
#4. Inheritance - mechanism to create a new class using properties and methods of an existing class


#access modifiers
#1. public - accessible from anywhere
#2. protected - accessible within the class and its subclasses
#3. private - accessible within the class only
    #in python private members are denoted by prefixing the member name with double underscore __
    #name mangling - _ClassName__memberName
    #private members can be accessed using name mangling
    #getter and setter methods are used to access private members
    #property decorator is used to create getter and setter methods for private members
    
    
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  #private member
        self.__balance = balance  #private member
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
         self.__balance = amount
        
            
account = BankAccount("1234567890", 1000)
print(account.get_balance())  #accessing private member using getter method
account.set_balance(2000)  #accessing private member using setter method
print(account.get_balance())    


#nheritance

#multilevel inheritance
class Employee:
    start_time = "9 AM"
    end_time = "6 PM"
    
    def change_time(self,new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
   def __init__(self,subject):
       self.subject = subject 
    
class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role
        
staff1 = AdminStaff("HR")
staff2 = Teacher("Maths")

staff1.change_time("5 PM")

print(staff1.role,staff1.start_time, staff1.end_time)
        
        
        
        #inheritance types
        #1. single inheritance - a class inherits from one superclass
        #2. multiple inheritance - a class inherits from multiple superclasses
        #3. multilevel inheritance - a class inherits from a superclass, which in turn inherits from another superclass
        
 #single inheritance
class Employee:
    start_time = "9 AM"
    end_time = "6 PM"
    
    def change_time(self,new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
   def __init__(self,subject):
       self.subject = subject   
       
teacher1 = Teacher("Maths")
print(teacher1.subject, teacher1.start_time, teacher1.end_time) 
teacher1.change_time("5 PM")
print(teacher1.subject, teacher1.start_time, teacher1.end_time)  

#multilevel inheritance
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
class Employee(Person):
    start_time = "9 AM"
    end_time = "6 PM"
    
    def change_time(self,new_end_time):
        self.end_time = new_end_time
class Teacher(Employee):
   def __init__(self, name, age, subject):
       super().__init__(name, age)
       self.subject = subject   
teacher1 = Teacher("monu", 30, "Maths")
print(teacher1.name, teacher1.age, teacher1.subject, teacher1.start_time,
        teacher1.end_time)
teacher1.change_time("5 PM")
print(teacher1.name, teacher1.age, teacher1.subject, teacher1.start_time,
        teacher1.end_time)  


#multiple inheritance

class Teacher:
    def __init__(self,salary):
        self.salary = salary
        
class Student:
    def __init__(self,marks):
        self.marks = marks
        
class TA(Teacher, Student):
    def __init__(self, salary, marks ,name):
        Teacher.__init__(self, salary)
        Student.__init__(self, marks)
        self.name = name
        
ta1 = TA(50000, 90, "monu")
print(f"TA Name: {ta1.name}, Salary: {ta1.salary}, Marks: {ta1.marks}")