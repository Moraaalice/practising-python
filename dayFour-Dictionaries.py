#This section will mostly involve dictionaries
dog = {"name":"Rex","colour":"Brown","Breed":"Germansherpherd","legs":"Black","age":12}
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

