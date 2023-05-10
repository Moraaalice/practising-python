#Python program that takes a list of integers as input and outputs the 
#largest and smallest numbers in the list.
def list_of_numbers(num):
    print(min(num))
    print(max(num))
 
#Display Fibonacci series up to 10 terms
#Calculate the cube of all numbers from 1 to a given number
def calculate_cubes(nums):
    for n in nums:
        print(n**3)

#Python program that takes a list of numbers as input and outputs "even" if the number 
# is even and "odd" if the number is odd using if-else statements. 
def check_odd_or_even(numbs):
    for n in numbs:
        if n%2==0:
            print("Even")
        else:
            print("Odd")

#Python program that accepts a string and calculates the number of digits and letters.
def calculate_digits_letters(word):
    digits = 0
    letters = 0
    for i in word:
        if i.isdigit():
            digits+=1
            print(digits)
        elif i.isalpha():
            letters+=1
            print(letters)
# Python program that takes a list of integers as input and outputs the sum of all the 
# even numbers in the list until it reaches a number that is not divisible by 2.
def sum_of_even(numbers):
    sum = 0
    for n in numbers:
        if n%2==0:
            sum+=n
        if n%2!=0:
            break
        print(sum)

#Python program that takes a list of integers as input and outputs the product of all 
# the odd numbers in the list. 
def check_odd(numbers):
    multiply = 1
    for n in numbers:
        if n%2 != 0:
            multiply*=n
            print(multiply)

#Python program that takes a string as input and outputs the string in reverse order.
def input_str(word):
    print(word[::-1]) 
    
#Python program that takes a string as input and outputs the number of vowels in the string.
def num_of_vowels(str): 
    count = 0
    vowel = set("aeiouAEIOU")
    for s in str:
        if s in vowel:
            count += 1 
            print(count)
            
def odd_even(list):
    
    sum=0;
    product=1
    for x in list:
        if x%2==0:
           sum +=x
        elif x%2!=0:
            product*=x
    
    print(sum)
    print(product)  
list=[1,2,3,4,5,6,7,8,9,10]   
odd_even(list)

#Python program that takes a list of strings as input and outputs the longest string in the list.
def longest_str(strlist):
    longest = ""
    for s in strlist:
        if len(s) >len(longest):
            longest = s
    return longest         
              
print(longest_str(["moraa","run","elephant"]))    

#checking the factorial of a number
def factorial(number):
    factor = 1
    if number < 0:
        print("Factorial does not exist for negative numbers")
    elif number == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range (1,number +1):
            factor = factor*i
            print(number,factor)
number = 2
factorial(number) 

#Python program that takes a list of integers as input and outputs the list with all the numbers up to but not including the first negative number.
def exclude_negative_number(nums):
    for n in nums:
        if n < 0:
            break
        print(n)
nums = [3,5,6,7,-1,-3,-4]
exclude_negative_number(nums) 

#Python program that takes a list of strings as input and outputs the list with all the strings that contain the letter "a"
def list_contains_letter_a(names):
    for n in names:
        if 'a' in n:
            print(n)
        elif 'a'not in n:
            print("a not found")
names = ["Nick","Juana","Lisa","Mirembo"]
list_contains_letter_a(names)  

#Python program that takes a list of integers as input and outputs the list with all the duplicate numbers removed.
def remove_duplicates(nums):
     return len(nums) == (len(set(nums)))
nums = [12,12,34,34,56,78,90,90,1,1,2] 
print(remove_duplicates(nums)) 


        
                              
                               
                          
            
            
                       
            
    
    
                   
        
              
        
        
    
               
     
    
    