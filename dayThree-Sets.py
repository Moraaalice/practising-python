companies = {"Facebbok","Google","Amazon","Oracle","Apple","Microsoft","IBM"}
#finding the length of the set
print(len(companies))
#Adding a single item to a set
companies.add("Twitter")
print(companies)
#Adding multpile elements to a set
companies.update(["Netflix","Instagram"])
print(companies)
#removing a company from a set
companies.remove("Instagram")
print(companies)
#Diference between remove and discard is that when using the discard function if the
#item does not exist on the set then the set remains unchanged whereas the remove
#function will through an error
a = {"Football","Volleyball","Tennis","Netball","Basketball"}
b = {"Badminton","Athletics","Football","Netball","Hockey","LongJump"}
c = a.intersection(b)
print(c)
a.intersection_update(b)
print(a)
d = a.symmetric_difference(b)
print(d)
a.pop()
print(a)
print(a.isdisjoint(b))
e = a.issubset(b)
print(e)
a.clear()
b.clear()
print(a)
print(b) 
#
t = "I am a teacher and i love to inspire and teach people"
v = set(t.split(" "))
print(v)
