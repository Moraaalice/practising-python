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

#     

        
        



    
            
            
            