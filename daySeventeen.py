#Python program that takes a list of integers as input and outputs the largest and smallest numbers in the list
def take_list(nums):
    nums.sort()
    print(nums[0])
    print(nums[-1])
nums = [10,4,6,40,23,90]
take_list(nums) 

#Display Fibonacci series up to 10 terms
#Find the factorial of a given number(The factorial (symbol: !) means to multiply all whole numbers from 
# the chosen number down to 1.) 
#Calculate the cube of all numbers from 1 to a given number
def cube_of_numbers(num):
    cubes = []
    for n in range(1,num+1):
        cube = n**3
        cubes.append(cube)
    return cubes
given_number = 4
print(cube_of_numbers(given_number)) 

#Python program that takes a list of numbers as input and outputs "even" if the number is even and "odd" if 
# the number is odd using if-else statements. 
def list_of_numbers(numbers):
    for num in numbers:
        if num %2 == 0:
            print("Even")
        elif num %2 != 0:
            print("Odd")
digit = [3,9,6,4,10,40,78,99,1]
list_of_numbers(digit)  

#Python program that takes a list of numbers as input and outputs the sum of all the even numbers and the
# product of all the odd numbers using the if-else statement.
def sum_and_product(nums):
    addition = 0
    product = 1
    for n in nums:
        if n%2 == 0:
            addition += n 
        else:
            product *= n
    return product,addition
print(sum_and_product([3,9,7,2,4,10]))

#Python program that accepts a string and calculates the number of digits and letters.
def calculate_string_and_numbers(name):
    letter_count = 0
    digit_count = 0
    for n in name:
        if n.isdigit():
            digit_count += 1
        else:
            n.isalpha()
            letter_count += 1
    return letter_count,digit_count
name = "alice254"
print(calculate_string_and_numbers(name))

#Python program that takes a list of integers as input and outputs the sum of all the even numbers in the list
# until it reaches a number that is not divisible by 2.
def sum_of_even(nums):
    addition = 0
    for n in nums:
        if n%2 == 0:
            addition += n
        elif n %2 != 0:
            break
    return addition
nums = [4,8,2,3,8,9,7,]
print(sum_of_even(nums))


#Python program that takes a list of integers as input and outputs the product of all the odd numbers in the list.
def product_of_even(nums):
    product = 1
    for n in nums:
        if n %2 != 0:
            product *= n   
    return product
nums = [2,5,9,3,7,1,11,10]
print(product_of_even(nums))

#Python program that takes a string as input and outputs the string in reverse order.
def reverse_string(word):
    print(word[::-1])
reverse_string("Alice Moraa")

#Python program that takes a list of strings as input and outputs the longest string in the list.
def longest_string(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
words = ["Ann","Elephant","Alice","Ongongongo"]
print(longest_string(words))

#Python program that takes a string as input and outputs the number of vowels in the string.
def number_of_vowels(word):
    count = 0
    vowels = set("aeiouAEIOU")
    for w in word:
        if w in vowels:
            count += 1
    return count
word = "Alice Moraa"
print(number_of_vowels(word))

#Python program that takes a list of integers as input and outputs the list with all the odd numbers doubled.
def odd_numbers_doubled(numbers):
    double = []
    for num in numbers:
        if num %2 != 0: 
            double.append(num*2)
    return double
numbers = [3,8,10,6,5,7,9,11] 
print(odd_numbers_doubled(numbers))

#Python program that takes a list of strings as input and outputs the list with all the strings in uppercase.
def list_of_strings(places):
    capital = []
    for p in places:
        capital.append(p.upper())
    return capital
places = ["Nakuru","Nairobi","Mombasa"]
print(list_of_strings(places))

#Python program that takes a list of strings as input and outputs the longest string in the list.
def longest_word_in_list(cars):
    longest = ""
    for car in cars:
        if len(car) > len(longest): 
            longest =  car   
    return longest
cars = ["Toyota","Nissan","Mitsubishi"]
print(longest_word_in_list(cars))

#Python program that takes a list of integers as input and outputs the sum of all the numbers until it reaches 
# a negative number. Ignore the negative number in the sum
def list_of_integers(nums):
    addition = 0
    for n in nums:
        if n > 0:
            addition += n
        if n < 0:  
            break
    return addition
nums = [1,3,5,3,2,-2,-4,-5]
print(list_of_integers(nums))

#Python program that takes a list of integers as input and outputs the list with all the even numbers removed using a while loop.

#Python program that takes a list of integers as input and outputs the list with all the numbers up to but not 
# including the first negative number. 
def exclude_negative_number(nums):
    positive = []
    for n in nums:
        if n > 0:
            positive.append(n)
        if n < 0:
            break
    return positive 
nums = [2,4,5,7,9,10,-4,-3,-2]
print(exclude_negative_number(nums))


# Python program that takes a list of integers as input and outputs the list with all the even numbers doubled 
# and all the odd numbers tripled. 
def list_of_integers(digits):
    doubled = []
    for digit in digits:
        if digit %2 == 0:
            doubled.append(digit * 2)
        if digit %2 != 0:
            doubled.append(digit * 3)    
    return doubled
digits = [2,3,4,5,6,7,10,9,15] 
print(list_of_integers(digits))

#Python program that takes a list of strings as input and outputs the list with all the strings that contain the letter "a" 
def list_with_letter_a(names):
    empty = []
    for name in names:
        if "a" in name: 
            empty.append(name)
    return empty
names = ["alice","jeremy","winnie","mary","gubo"] 
print(list_with_letter_a(names)) 

#Python program that takes a list of integers as input and outputs the list with all the duplicate numbers removed.
def remove_duplicates(names):
    names = set(names)
    print(names)
names = ["alice","brian","dante","alice","ann","brian"]
(remove_duplicates(names))

#Python program that takes a list of numbers as input and outputs the list with all the prime numbers removed.
#Python program that takes a list of numbers as input and outputs the sum of all the numbers that are divisible by 3 
def total_of_numbers_divisible_by_3(nums):
    divisible = []
    for num in nums:
        if num %3 == 0:
            divisible.append(num)
    return divisible
nums = [12,3,5,6,3,32,24,65,15,10]
print(total_of_numbers_divisible_by_3(nums))            
#Python program that takes a list of strings as input and outputs a list of the lengths of those strings using list comprehension.
#Python program that takes a list of numbers as input and outputs a list of the squares of those numbers using list comprehension
numbers = range(2,12,2)
print(list(numbers)) 

numbers = range(1,11,3) 
print(list(numbers)) 

numbers = range(5,-6,-3) 
print(list(numbers))  

# create a variable named capitalized_fruits and use list comprehension syntax to produce output like
# ['Mango', 'Kiwi', 'Strawberry']
def capitalize_fruits(fruits):
    caps = [fruit.capitalize() for fruit in fruits]
    print(caps)
fruits = ["mango","orange","banana"]
capitalize_fruits(fruits)

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits 
# to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
def capital_fruits(fruits):
    capital = [fruit.upper()for fruit in fruits]
    print(capital)
fruits = ["mango","orange"] 
capital_fruits(fruits) 

# make a list that contains each fruit with more than 5 characters
def five_characters(names):
    more_than_five = [name for name in names if len(name) > 5 ]
    print(more_than_five)
names = ["Alicia","Dante","Ongongo"]
five_characters(names)  


#Write a python function that takes one argument as a list a = [2,4,6,8] and remove the second last item 
# from that list and returns the whole list without the removed item
def remove_second_last(nums):
    nums.pop(-2)
    return nums
print(remove_second_last([2,4,6,8,]))


#Write a python program that has a list days = [ “Monday”, “Tuesday”, “Friday”, “Monday”] and counts the 
# number occurrences of Monday
def count_number_of_occurences(days):
    count = 0
    for day in days:
        if day == "Monday":
            count += 1
    return count
print(count_number_of_occurences(["Monday","Tuesday","Wednesday","Monday"]))


#Write a Python function named smallest that accepts a list of unsorted integers and returns the smallest
# number in the list
def smallest(integers):
    integers.sort()
    print(integers[0])
smallest([9,5,1,5,3,9,-3,11]) 

def num_smallest(nums):
    return min(nums) 
print(num_smallest([4,10,12,9,15,19,20])) 

#Write a python function named divisible_by_seven that; using the range function and a for loop returns a 
# list containing all the numbers between 100 and 200 that are divisible by 7.
def divisible_by_seven():
    divisible = []
    for num in range(100,201):
        if num %7 == 0:
            divisible.append(num)
    return divisible
print(divisible_by_seven()) 

#Write a python program that takes two inputs(as integers) from a user and adds
#the 2 numbers, checks  if the sum is greater than than 10, less than 10 or equal 10 
#and prints a statement  after each check 
def take_two_inputs(num1,num2):
    addition = num1 + num2
    if addition > 10:
        print("Addition is greater than 10")
    elif addition < 10:
        print("Addition less than 10")
    else:
        addition == 10
        print("Addition is equal to 10")
take_two_inputs(1,5)        

#Write a python function that takes one argument which is a list,  a=[1,2,3,4,5] and returns    
# True if 4 is present in the list and False is 4 is not in the list
def check_membership(nums):
        if 4 in nums:
            print("True")
        else:
            print("False")
check_membership([1,2,3,4,5]) 

#Write a python function that takes one argument which is a list    
#fruits=["apples","grapes","pineapple"] and removes the last fruit  from the list then 
#returns the list without the removed fruit
def remove_from_list(fruits):
    fruits.pop(-1)
    return fruits
print(remove_from_list(["Apples","Grapes","Pineapples","Oranges"]))

#Write a python program that takes in a list of cars, cars = ['Ford', 'BMW', 'Volvo'] and returns a sorted list 
def sorted_list(cars):
    sorting = sorted(cars)
    return sorting
print(sorted_list(["Ford","Volvo","BMW"]))


           


       
        
 


  
 
     
            
              
            

       
                            
    
                       
          
                        