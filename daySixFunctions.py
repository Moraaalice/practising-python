#Area of a circle is calculated as follows: area = π x r x r.
#Write a function that calculates area_of_circle.
def add_two_numbers(num1,num2):
    sum = num1+num2
    print(sum)
add_two_numbers(23,34) 
#Area of a circle is calculated as follows: area = π x r x r
#Write a function that calculates area_of_circle.
def area_of_a_circle(radius):
    pi = 3.14
    area = pi*radius*radius
    print(area)
area_of_a_circle(radius=23)

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments
#Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    sum = 0
    for n in nums:
        sum+=n
    return sum
print(add_all_nums(23,24,25))   
     
#Write a function called check-season, it takes a month parameter and returns the season:
#Autumn, Winter, Spring or Summer
def check_season(*month):
    return month
print(check_season("Autumn","Winter","Spring","Summer"))

#Write a function called calculate_slope which return the slope of a linear equation
def slope(x1,x2,y1,y2):
    sloping = (x1-x2)/(y2-y1)
    return sloping
print(slope(90,50,45,100))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for l in list:
        print(l)
places = ["Mombasa","Nakuru","Nyandarua"]        
print_list(places)

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    arr2 = []
    for r in arr:
        arr2.append(r)
        arr2.reverse()
        print(arr2)
names = ["Alice","Dante","Mary","Mark"]
(reverse_list(names))  

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list1):
    list2 = []
    for l in list1:
        list2.append(l.upper())
        return list2
city = ["Nairobi","Kisumu","Mombasa"]
print(capitalize_list_items(city))  

#  
        

#              
          


                
    
        
     

   
       
    