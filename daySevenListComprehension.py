#Filter only negative and zero in the list using list comprehension
def digits(numbers):
    numbers2 = []
    for num in numbers:
        if num<=0:
            numbers2.append(num)
            print(num)
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]        
print(digits(numbers))

#Flatten the following list of lists of lists to a one dimensional list :
def dimension_list(nums):
    flattened_list = [n for sublist in nums for n in sublist]
    print(flattened_list)
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print(dimension_list(list_of_lists))

#
def list_dimension(numb):
    list2 = []
    for num in numb:
        for i in num:
            list2.append(i)
            print(i)
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print(list_dimension(list_of_lists))

#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
def flatten(places):
    empty = []
    for sublist in countries:
        for c in sublist:
            empty.append(c)
            print(c)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print(flatten(countries))   

#print all the numbers from 1-1000
def digits():
    x = 0
    while x<=1000:
        if x%7==0:
            print(x)
        x = x + 1
digits()

#Find all of the numbers from 1-1000 that have a 3 in them
def digits_contains_three():
   three = [n for n in range(0,1000) if '3' in str(n)]
   print(three)
digits_contains_three()  

#count the number of spaces in a string 
def count_spaces(name):
    count = 0
    for n in name:
        if n == " ":
            count = count + 1
    return count
name = "I love coding especially, pyhton"                         
print(count_spaces(name)) 

#Create a list of all the consonants in the string “Yellow Yaks like yelling and 
# yawning and yesturday they yodled while eating yuky yams”
def create_consonants(sentence):
    consonants = [c for c in sentence if c not in 'a,e,i,o,u, " "']
    print(consonants)
sentence = "Yellow yalks like yelling and yawning and yesturday they yodled while eating yuky yums"    
create_consonants(sentence)

#    
                       
                  

        
        



    
            
            
            