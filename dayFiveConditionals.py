#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
languages = ["python","Nummpy","Pandas","Django","Flask"]
def names(languages):
    for l in languages:
        print(l)

names(languages)
#Use for loop to iterate from 0 to 100 and print only even numbers

def numbers():
    number = 101
    for n in range(number):
        print(n)
numbers() 

#
digit = 101
for d in range(101):
    if(d%2==0):
        print(d)
#Use for loop to iterate from 0 to 100 and print only odd numbers
def odd_numbers():
    odd_number = 101
    for d in range(101):
        if(d%2!=0):
            print(d)
odd_numbers() 
#Iterate 0 to 10 using for loop, do the same using while loop.
def one_to_ten():
    one = range(11)
    for i in one:
        print(i)
one_to_ten() 
#using a while loop to iterate through 1-10
n = 1  
while n<=10:
    print(n)
    n = n+1
#
def loop_while():
    n = 1
    while n<=10:
        print(n)  
        n = n+1
loop_while()
#Iterate 10 to 0 using for loop, do the same using while loop.
def loop_to_zero():
    num = range(10,0)
    for n in num:
        print(n)
loop_to_zero()        

#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
def sum_of_numbers():
    sum = 0
    digit = 101
    for d in range(digit):
        sum+=d
        print(sum)  
sum_of_numbers () 
#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
def sum_of_even_nmbers():
    sum = 0
    even = 101
    for e in range(even):
        if(e%2==0):
            sum+=e
            print(sum)
sum_of_even_nmbers()               
#sum of odd
def sum_of_odd_numbers():
    sum = 0
    odd = 101
    for o in range(odd):
        if(o%2!=0):
            sum+=o
            print(sum)
sum_of_odd_numbers()

#create a program to check whether the program is positive,negative or 0.
#For this create a variable called number and assign it a float value.Then using an
#if statement check if the number variable is positive,negative or zero
#If number is positive,print-"number is positive"
#if number is negative,print-"number is negative"
#and if number is zero,print-"number is zero"
def check_number():
    num = -5
    if(num>0):
        print("This is a positive number")
    elif(num<0):
        print("This is a negative number")
    elif(num==0):
        print("This is zero")
    else:
        print("No number")
check_number()                    
#    
                      
    
                
                     
        
