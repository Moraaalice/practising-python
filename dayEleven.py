#1. Write a Python program that prints the numbers from 1 to 10 using a for loop.
def print_one_to_ten():
    for i in range(1,11):
        print(i)  
print_one_to_ten() 

#2.Write a Python program that takes a user input string and reverses it.
def reverse_str(name):
    print(name[::-1])
name = "alicia"    
reverse_str(name)   

#3. Write a Python function that takes a list of integers as input and returns the sum of all even numbers in the list.
def sum_of_list(digits):
    add =  0
    for d in digits:
        if d%2==0:
            add+=d
            print(add)
digits = [10,23,21,4,8,6] 
sum_of_list(digits) 

#4. Write a Python function that takes a list of strings as input and returns a new list containing only the strings 
# that have a length greater than 5.
def greater_than_five(places):
    newlist = []
    for p in places:
        if len(p) >= 5:
            newlist.append(p)
            print(newlist)
places = ["Kisi","Nakuru","Nyandarua","Mau","Jody"]
greater_than_five(places)  

# Write a Python program that reads a text file and counts the number of occurrences of each word in the file.
# def text_file(txtfile):
#     counting = 0
#     for n in txtfile:
#         txt = n.split()
#         counting += len(txt)
#         print(counting)
# text_file =  

# *args and the named variables together
def check_args(a,b,*args):
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"args is {args}")
check_args(2,3,4,5,6,7,8) 
   
#addition of numbers using args
def add_multiple_numbers(*args):
    addition = 0
    for a in args:
        addition += a 
        return addition
print(add_multiple_numbers(1,5,4))  

def addition_of_numbers(a,b,*args,option = True):
    sum_Numbers = 0
    if option:
        for i in args:
            sum_Numbers += i
            return a+b+sum_Numbers
    else:
        return sum_Numbers
print(addition_of_numbers(12,34,56,78))  

#The kwargs
def check_kwargs(a,b,**kwargs):
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"kwargs is {kwargs}")
print(check_kwargs(12,4, param1=34,param2=56,param3=31))          
    
     
        
        
        
           
           
    
            
        