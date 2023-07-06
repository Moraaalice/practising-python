#Write a function that takes in a variable number of arguments and returns the average of all the numbers passed
#as arguments
def average_of_numbers(*args):
    count = 0
    for arg in args:
        count += arg
        average = count / len(args)
    return average
print(average_of_numbers(2,5,9,15,20))

#Write a function that takes in a variable number of strings and returns a new string that concatenates all 
#the input strings,separated by a specified delimiter.
def concatenate(delimetre,*args):
    return delimetre.join(args)
print(concatenate("Alice","Brian","Dante","Mark","Mary"))

#Write a function that takes in a dictionary and a variable number of keys. The function should return a new dictionary 
#containing only the key-value pairs from the input dictionary that correspond to the provided keys.
def take_in_dict(input_dict,*keys):
    new_dict = {}
    for key in keys:
        if key in input_dict:
            new_dict[key] = input_dict[key]
    return new_dict
student_data = {"Name":"Alice","School":"AkiraChix","Age":24}
filtered_data = take_in_dict(student_data,"Name")
print(filtered_data)

#Write a function that takes in a list of numbers and a variable number of filters. Each filter is a function that takes 
#in a number and returns True or False. The function should return a new list containing only the numbers that pass all 
#the filters
def list_of_nums(nums,*filters):
    new_list = []
    for num in nums:
        if all (filter_fun(num) for filter_fun in filters):
            new_list.append(num)
    return new_list
def is_even(num):
    return num %2 == 0
def is_positive(num):
    return num > 0 
def is_divisible_by_three(num):
    return num %3 == 0
nums = [1,2,3,4,5,6,7,8,9,10]
filter_numbers = list_of_nums(nums,is_even,is_positive,is_divisible_by_three)
print(filter_numbers)

#Write a function that takes in a variable number of strings and a keyword argument "reverse". If "reverse" is set to True, 
#the function should return a new list with the strings reversed. Otherwise, it should return the strings as they are.
def reverse_strings(*strns,reverse = True): 
    new_strings = []
    for str in strns:
        if reverse:
            new_strings.append(str[::-1])
        else:
            new_strings.append(str)
    return new_strings
print(reverse_strings("Alicia","Brian","Dante","Mark"))

#Write a function that takes in a variable number of dictionaries and merges them into a single dictionary. 
#If there are duplicate keys, the value from the last dictionary should be used.
def merge_dict(*dicts):
    merged = {}
    for dit in dicts:
        merged.update(dit)
    return merged
dict1 = {"Name":"Alice","School":"AkiraChix"}
dict2 = {"County":"Nakuru","Status":"single"}
dict3 = {"Estate":"Pipleine","Age":24}
merged = merge_dict(dict1,dict2,dict3)
print(merged)

#Write a function that takes in a list of tuples, where each tuple contains a student's name and their corresponding 
#scores in multiple subjects. The function should calculate the average score for each student and return a dictionary
#with the student names as keys and their average scores as values.



        
    
       
       
    