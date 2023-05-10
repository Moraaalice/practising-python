#Area of a circle is calculated as follows: area = π x r x r.
#Write a function that calculates area_of_circle.
def add_two_numbers(num1,num2):
    sum = num1+num2
    print(sum)

#Area of a circle is calculated as follows: area = π x r x r
#Write a function that calculates area_of_circle.
def area_of_a_circle(radius):
    pi = 3.14
    area = pi*radius*radius
    print(area)


#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments
#Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    sum = 0
    for n in nums:
        sum+=n
    return sum
 
     
#Write a function called check-season, it takes a month parameter and returns the season:
#Autumn, Winter, Spring or Summer
def check_season(*month):
    return month


#Write a function called calculate_slope which return the 
# slope of a linear equation
def slope(x1,x2,y1,y2):
    sloping = (x1-x2)/(y2-y1)
    return sloping


#Declare a function named print_list. 
# It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for l in list:
        print(l)
places = ["Mombasa","Nakuru","Nyandarua"]        


#Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(*arr):
    arr2 = []
    for r in arr:
        arr2.append(r.reverse())
        return arr2
  

#Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(*list):
    list2 = []
    for l in list:
      list2.append(l.upper())
    return list2


#Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.
#Declare a function named sum_of_numbers. It takes a number
# parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    add = 0
    for n in range(0,10):
        add+=n
#
print(9//2) 
#Accesiing elements in a multi dimensional list
names = [["Geeks","For"],["Geeks"]]
print(names[0][1])

names = "Alice,Juana,Kate"
names2 = names.split()
print(list(names2))

    
   
        
        
        
        
        
        

        
     
        
                      

    
  
    
    


                  
          


                
    
        
     

   
       
    