#Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

#Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the
# area of ​​the rectangle.

#Create a method display() that display the length, width, perimeter and area of an object created using an
# instantiation on rectangle class.

#Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another
# Volume() method to calculate the volume of the Parallelepiped.

class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length
        
    def area_of_rectangle(self):
        return self.width * self.length  
    
    def perimetre(self):
        return self.width*2 + self.length*2  
    
    def display(self):
        print("width:",self.width)
        print("length:",self.length)
        print("area_of_rectangle:",self.area_of_rectangle())
        print("perimetre:",self.perimetre)
   
class Parallelepipede(Rectangle):
    def __init__(self, width, length,height):
        super().__init__(width, length)
        self.height = height
    
    def volume(self):
        return self.length*self.height*self.width
        
  #QUESTION2               
#Create a Python class Person with attributes: name and age of type string.
#Create a display() method that displays the name and age of an object created via the Person class.
#Create a child class Student  which inherits from the Person class and which also has a section attribute.
#Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
#Create a student object via an instantiation on the Student class and then test the displayStudent method.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print("name:",self.name)
        print("age:",self.age) 
    

class Student(Person):
    def __init__(self, name, age,section):
        super().__init__(name, age) 
        self.section = section
        
    def display_student(self):
        print("name:",self.name)
        print("age:",self.age)
        print("section:",self.section)



#QUESTION3
#Create a Python class called BankAccount which represents a bank account, having as attributes: 
# accountNumber (numeric type), name (name of the account owner as string type), balance.

#Create a constructor with parameters: accountNumber, name, balance.
#Create a Deposit() method which manages the deposit actions.
#Create a Withdrawal() method  which manages withdrawals actions.
#Create a bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
#Create a display() method to display account details.
#Give the complete code for the  BankAccount class.     
class BankAccount:
    account_number = None
    account_name = ""
    def __init__(self,account_number,name,balance):
        self.accountNumber = account_number
        self.name = name
        self.balance = balance
        
    def deposit(self,deposit):
        self.balance += deposit
        print(f"deposit of {deposit} is successful total balance is {self.balance}")
    
    def withdraw(self,withdrawal):
        if self.balance >= withdrawal:
            self.balance -= withdrawal
            print(f"{withdrawal} was successful balance is {self.balance}")
        else:
            print(f"Not enough money to withdraw {withdrawal}  current balance is {self.balance}")
            
    def bank_fees(self):
        fees = self.balance * 0.05
        self.balance -= fees
        print(f"Bank fees is {fees}")        
    
    def display_details(self):
        print("Name:",self.name)
        print("AccountNumber:",self.account_number)
        print("Balance:",self.balance)

        
#QUESTION4
#Define a Book class with the following attributes: Title, Author (Full name), Price.
#Define a constructor used to initialize the attributes of the method with values entered by the user.
#Set the View() method to display information for the current book.
#Write a program to testing the Book class.
class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        
    def display_information(self):
        print("Title:",self.title) 
        print("Author:",self.author) 
        print("Price:",self.price)
        

#QUESTION5
#Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations 
# on integers numbers.

# Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by 
# instantiating the class

#Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. 
# Test this method.

#Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
#Create  a method called testPrims() allowing to test if two numbers are prime between them.

#Create a tableMult() method which creates and displays the multiplication table of a given integer. 
# Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.

#Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. 
# Create another listDivPrim() method that gets all the prime divisors of a given integer.







        
    
       
          
               