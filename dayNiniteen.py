#Write a program that takes a list of numbers as input and calculates the sum of all the even numbers in the list
def sum_of_even(nums):
    count = 0
    for num in nums:
        if num%2 ==0:
            count += num
    return count
nums = [17,4,10,13,11,18,24]
print(sum_of_even(nums))




#Write a function that takes a string as input and returns the number of uppercase letters, lowercase letters, 
#and digits in the string.
def uppercase_lower_digits(words):
 upper_case = 0
 lower_case = 0
 digits = 0
 
 for word in words:
     
    if word.isupper():
         upper_case += 1
    elif word.islower():
         lower_case += 1
    elif word.isdigit():
    
         digits += 1
 return upper_case ,lower_case ,digits    
print(uppercase_lower_digits("Alicia254")) 
          
#Write a program that prompts the user to enter a password. The program should continue to ask for a password
# until the user enters a password that meets the following criteria: at least 8 characters long, contains both 
# uppercase and lowercase letters, and includes at least one digit 
def enter_password(password):
    if len(password) > 8:
        return False
    if not any (passw.isupper() for passw in password):
        return False
    if not any(passw.islower() for passw in password):
        return False
    if not any(passw.isdigit() for passw in password):
        return False
    return True
print(enter_password("AliciaMoraa254"))  

#Write a function that takes a list of integers as input and returns the second smallest element from the list
def second_smallest_element(elements):
    sorting = sorted(elements)
    return sorting[1]
print(second_smallest_element([20,89,45,38,90,12])) 


#Write a function that takes a list of strings as input and returns a new list containing only the strings 
# that start with a vowel (a, e, i, o, u) regardless of case
def start_with_vowel(strs):
    new = []
    vowels = tuple("AEIOUaeiou")
    for word in strs:
        if word.startswith(vowels):
            new.append(word)
    return new
print(start_with_vowel(["Alice","Joy","Elisha","Winnie"]))


#Write a function that takes a string as input and checks if it is a palindrome (reads the same forwards and 
# backwards). Ignore spaces, punctuation, and capitalization.
def check_palindrome(strn):
    palindrome = strn.rsplit(" ")
    palindrome.reverse()
    if strn  ==  palindrome:
        print("Is palindrome")
    else:
        print("Is not palindrome")
check_palindrome("dad")

#Write a program that takes a list of words as input and prints the longest word(s) in the list. 
#If there are multiple words with the same length, print all of them 
def longest_word(words):
    longest = ""
  
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(longest_word(["Alice","Joy","Elephant","Ongongo","Winnifrida"]))

         
            
            
            
    
    
            