#Write a Python program that prints the numbers from 1 to 10 using a for loop.
def nums():
    for i in range(1,11):
        print(i)
nums()   
#. Write a Python program that takes a user input string and reverses it
def reverse():
    word = "I love python"[::-1]
    print(word) 
reverse()  
#. Write a Python function that takes a list of integers as input and returns 
# the sum of all even numbers in the list.
def list_nums(digits):
    count = 0
    for n in digits:
        if n%2==0:
            count+=n
            print(count)
digits = [12,45,26,89,13,44,24,28]
list_nums(digits)

# Write a Python function that takes a list of strings as input and returns 
# a new list containing only the strings that have a length greater than 5.
def list_of_strings(places):
    new_list = []
    length = -1
    for p in places:
        if len(p) >5 :
            length = len(p)
            new_list.append(p)
            print(new_list)
places = ["Nakuru","Nyeri","Kisii","Nyandarua","Oloitoktok"]
list_of_strings(places)

# Write a Python program that reads in a text file and counts the number of occurrences 
# of each word in the file. 
def count_each_word(word):
    count = 0
    for w in word:
        sepearate = word.split(" ")
        count+=len(sepearate)
        print(count)
word = "I am going home"
count_each_word(word)        

#. Write a Python class called "Rectangle" that has attributes for width and height,
# and methods to calculate the area and perimeter of the rectangle.


      
    
         
           
          