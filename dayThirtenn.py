#Create a tuple named "fruits" with the values "apple", "banana", "cherry", and "orange".
# Print the second item in the "fruits" tuple.
fruits = ("apple","banana","cherry","orange")
print(fruits[1])
#Change the value of the third item in the "fruits" tuple to "kiwi".
fruits = list(fruits)
print(fruits)
fruits[2] = "watermelon"
print(fruits)
fruits = tuple(fruits)
print(fruits)
print(type(fruits))
#Print all the items in the "fruits" tuple using a for loop.
for f in fruits:
    print(f)
#Check if "banana" is present in the "fruits" tuple.
print("banana" in fruits)
#Create a new tuple named "numbers" with the values 1, 2, 3, 4, and 5.
numbers = (1,2,3,4,5,6)
#Concatenate the "fruits" and "numbers" tuples into a new tuple named "food".
food = numbers + fruits
print(food)
#Find the length of the "food" tuple.
print(len(food))
#Unpack the "food" tuple into two separate tuples named "fruits_list" and "numbers_list".
red,black,brown,green = fruits
print(red)
print(black)
print(green)
a,b,c,d,e,f= numbers
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
#Create a tuple named "my_tuple" with the values "a", "b", "c", and "d". Then, convert the 
# tuple to a list and print the result.
my_tuple = ('a','b','c','d','e')
my_tuple = list(my_tuple)
print(my_tuple)
print(type(my_tuple))






    


