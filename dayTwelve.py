#Below are two lists,convert the list into a dictionary in which the item from list one is the key 
#and list two as the value
names = ["Alice","Joy","Jemimah","Jeff"]
age = [21,30,24,29]
#method one to change the lists into dictionaries
def change_items(names,age): 
    names = ["Alice","Joy","Jemimah","Jeff"]
    age = [21,30,24,29]
    items = dict(zip(names,age)) 
    print(items)
change_items(names,age) 
 
#method two to change lists into dictionaries
#using a loop and update method 
def change_list(names,age):
    names = ["Alice","Joy","Jemimah","Jeff"]
    age = [21,30,24,29] 
    empty = {}
    for i in range(len(names)):
        empty.update({names[i]:age[i]})
        print(empty)
print(change_list(names,age))

#Merging two python dictionaries into one
def merging_two_dictionaries():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50} 
    dict3 = {**dict1,**dict2}  
    print(dict3) 
merging_two_dictionaries()   

#Write a function that takes two numbers as input and returns their sum.
def sum(num1,num2):
    add = num1+num2
    print(add)
sum(23,45)  
#Write a function that takes a string as input and returns the length of the string.
def length_of_the_string(str):
    print(len(str))
length_of_the_string("Alicia")    

#Write a function that takes a list of numbers as input and returns the average of the numbers.
def average(nums):
    sum = 0
    for n in nums:
        sum+=n
    average = sum/len(nums)
    return average
nums = [12,34,56,32,50]       
print(average(nums))  

#Write a function that takes a list of numbers as input and returns the maximum number in the list.
def maximum(number):
    maxi = max(number)
    return maxi
number = [12,34,56,78,5,7]   
print(maximum(number))  

#Write a function that takes a list of strings as input and returns the longest string in the list.
def longest_string_in_the_list(str):
    longest =  ""
    for s in str:
        if len(s) > len(longest):
            longest = s
    return longest        

print(longest_string_in_the_list(["alice","elephant","monkey"])) 

#Write a function that takes a list of strings as input and returns the shortest string in the list.
def shortest_str(str):
    shortest = ""
    for s in str:
        if len(s) < len(shortest):
            shortest = s
    return s
print(shortest_str(["ann","anastacia","bo"]))        

#Write a function that takes a string as input and returns a new string with all vowels removed.
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    output_string = ""
    for char in input_string:
        if char not in vowels:
            output_string += char
    return output_string
print(remove_vowels("DannyAlves")) 

#Write a function that takes a list of numbers as input and returns a new list with 
# all even numbers removed.
def even_numbers_removed(nums):
    even = []
    for n in nums:
        if n%2 != 0:
            even.append(n)
    return even
nums = [12,33,45,3,5,4,2]        
print(even_numbers_removed(nums))
 
#Write a function that takes a list of strings as input and returns a new list with all 
# strings that contain the letter 'a' removed.
def remove_letter_a(places):
    return [p for p in places if 'a' not in p]              
print(remove_letter_a(["Nakuru","Nairobi","Mombasa","Kilifi","Whitehouse","WestPokot"]))

#Write a function that takes a list of numbers as input and returns a new list with all numbers squared.
def num_squared(nums):
    squared = []
    for n in nums:
        squared.append(n*n)
    return squared 
print(num_squared([12,2,4,3,5,9]))

#Write a function that takes a list of strings as input and returns a new list with
# all strings capitalized.
def capitalize(cities):
    capitalized = []
    for c in cities:
        capitalized.append(c.upper())
    return capitalized
print(capitalize(["Kigali","Kampala","Dododma"]))

#Write a function that takes a string as input and returns a new string with all uppercase 
# letters replaced with lowercase letters and all lowercase letters replaced with uppercase letters.
def swap_str(hotels):
    for h in hotels:
        return h.swapcase()
print(swap_str(["SErena","SArova","MErica"]))               
        
     
       
                          
            
               
        
    
      
     

         
          
        