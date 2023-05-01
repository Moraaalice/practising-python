#This section will mostly involve dictionaries
dog = {}
dog["name"] = "Rex"
dog["color"] = "Brown"
dog["Breed"] = "GermanShepherd"
dog["Legs"] = "Black"
dog["age"] = 12
print(dog)
print(type(dog))
student = {"fname":"Alice","lname":"Moraa","gender":"female","marital_status":"single","skills":"soft_skills","country":"Kenya","city":"Nakuru","address":231}
print(len(student))
print(type(student))
student1 = student.get("Skills")
print(student1)
print(type(student1))
student["skills"]="hardskills","softskills","communicationskills"
print(student)
student3=list(student.keys())
print(student3)
student4 = list(student.values())
print(student4)
#Get the dictionary keys as a list
studen5 = list(student.keys())
print(studen5)
print(type(studen5))
#Get the dictionary values as a list
student6 = list(student.values())
print(student6)
print(type(student6))
# Change the dictionary to a list of tuples using items() method
student7 = [(x,y)for x,y in student.items()]
print(student7)
print(type(student7))
#Delete one of the items in the dictionary
student8 = student.pop("skills")
print(student8)
print(student)
#Delete one of the dictionaries
del student ["lname"]
print(student)
#sort all the items in the dictionary by key or value
for s in student:
    print(student[s])
for s in student:
    print(s) 
for s in student.items():
    print(s)       
f
