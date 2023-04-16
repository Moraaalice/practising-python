#This will mostly entail list methods
#Finding the lenght of a lis we use the len method
places = ["Nakuru","Mombasa","Nairobi","Nanyuki","Nyandarua","Nyamira"]
print(len(places))
middle_item = int(len(places)/2)
print(middle_item)
#we can obtain the first and last elements by their index
print(places[0])
print(places[-1])
#
mix_data_types = ["Alice",23,"single",234,55.0]
print(mix_data_types)
#
companies = ["Facebook","Google","Micrososft","Apple","IBM","Oracle","Amazon"]
print(companies)
print(len(companies))
#Getting the first and last elements in the list companies
print(companies[0])
print(companies[-1])
companies2 = companies.pop(3)
print(companies2)
#
companies.append("Netflix")
print(companies)
#
print(companies[4].upper())
print(companies)
#
companies4 = "#".join(companies)
print(companies4)
#checking if a certain element exists in list company
print("Netflix" in companies)
#sorting the list
companies.sort()
print(companies)
#reversing the list
companies.reverse()
print(companies)
#Slicing the first 3 companies
company = companies[0:3]
print(company)
#slicing out the last 3 companie
company1 = companies[-3:]
print(company1)
#removing the first company from the list
companies.pop(0)
print(companies)
#removing the last companies from the list
companies.pop(-1)
print(companies)
companies.clear()
print(companies)
#Joining lists
front_end = ["HTML","CSS","Js","React","Redux"]
back_end = ["Node","Express","MongoDb"]
full_stack = front_end+back_end
print(full_stack)
#
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)
#
ages = [19,22,19,24,20,25,26,24,25,24]
ages.pop()
print(ages)
ages.sort()
print(ages)
#finding min and max 
ages2 = max(ages)
print(ages2)
ages3 = min(ages)
print(ages3)
#
ages.extend([26,19])
print(ages)
#

