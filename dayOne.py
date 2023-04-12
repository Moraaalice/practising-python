names = ()
brothers = ("Brian","Jeff","Dante","Mark")
sisters = ("Mary","Winnie","Joy")
siblings = brothers + sisters
print(siblings)
print (len(siblings))
siblings = list(siblings)
print(siblings)
#adding elements to the tuple siblings
siblings.extend(["Mother","Father"])
print(siblings)
siblings = tuple(siblings)
print(siblings)
#unpacking of tuples
(red,blue,white,black,green,orange,purple,pink,grey) = siblings
print(red)
print(blue)
print(white)
print(black)
print(green)
print(orange)
print(purple)
print(pink)
print(grey)
#creating another tuple
fruits = ("banana","apple")
vegetables = ("carrots","kales")
animal_products =("pork","beef")
#joining all the tuples together
food_stuff_tp = fruits+vegetables+animal_products
print(food_stuff_tp)
#
food_stuff_tplist = ()
print(food_stuff_tplist)
#
nordiac_countries = ("Denmark","Finland","Iceland","Norway","Sweden")
print("Iceland"in nordiac_countries)
print("Estonia"in nordiac_countries)



    