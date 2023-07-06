#Write a Python function that takes in two sets as parameters and returns a new set that contains only 
# the elements that are common to both sets.
def elements_common(set1,set2):
    common = set1.intersection(set2)
    return common
set1 = {"Nairobi","Kisumu","Mombasa","Nakuru"}
set2 = {"Muyale","Marsabit","Nairobi","Mombasa"}
print(elements_common(set1,set2))

#Given a list of integers, write a Python function to find the sum of all the even numbers in the list
def sum_of_even(nums_list):
    count = 0
    for num in nums_list:
        if num %2== 0:
            count += num
    return count
nums_list = [9,4,1,5,10,8]
print(sum_of_even(nums_list))

#Create a Python function that takes in a list of tuples, where each tuple contains a student's name and 
#their corresponding score. The function should return a list of the names of the top three students with the
#highest scores.
def top_three_highest_scores(list_of_tuples):
      sorted_students = sorted(list_of_tuples, key=lambda x: x[1], reverse=True)
      top_three = [list1[0] for list1 in sorted_students[:3]]
      return top_three
list_of_tuples = [("Alice",40),("Danny",98),("Mary",78),("Brian",84),("Mark",88)]
print(top_three_highest_scores(list_of_tuples)) 

#Create a Python dictionary that represents a student database, where the keys are the student IDs 
# (integer values) and the values are dictionaries containing the student's name (string), age (integer),
# and subjects (a list of strings). Write a function to print the names of all the students who are older 
# than 20 years old. 
student_data_base = {
1:{"Name":"Alice","Age":24,"Subjects":["Maths","Science","Kiswahili"]},
2:{"Name":"Dante","Age":4,"Subjects":["Maths","Chemstry","Physics"]},
3:{"Name":"Mary","Age":30,"Subjects":["Biology","Literature","Physics"]},
4:{"Name":"Joy","Age":27,"Subjects":["Maths","Kiswahili","History"]},
5:{"Name":"Jeff","Age":19,"Subjects":["Literature","Biology","Physics"]},
6:{"Name":"Jemimah","Age":22,"Subjects":["Geography","History","Business"]},
7:{"Name":"Mark","Age":5,"Subjects":["Physics","Maths","Geography"]},
}
def student_data(student_data_base):
    for student_id, data_base in student_data_base.items():
        if data_base["Age"] > 20:
            print(data_base["Name"])
student_data(student_data_base)

#Write a Python program that accepts a list of sentences as input and counts the number of unique words across 
# all the sentences. Consider using frozen sets to store the unique words.  
def count_unique_words(sentences):
    unique = set()
    for sentence in sentences:
        words = sentence.split()
        unique.update(words)
    return len(unique)
sentences = ["I love python","I will be going to Nakuru","I am a good girl","I am a student at Akirachix"]
print(count_unique_words(sentences))

#Write a Python function that takes in a list of strings and returns a new list containing the strings 
#that have a length greater than 5.
def element_greater_than_five(names):
    new_list = []
    for name in names:
        if len(name) > 5:
            new_list.append(name)
    return new_list
names = ["Dan","Alicia","Joy","Jemimah","Winnifrida"]
print(element_greater_than_five(names))

#Create a Python function that takes in a list of tuples, where each tuple contains a 
# student's name, age, and grade. The function should return a new list of tuples with only the 
# students who are older than 18 years old and have a grade higher than 80.
def student_oder_than_eighteen(students):
    new_list = []
    for student in students:
        name,age,grade = student
        if age > 18 and grade > 80:
            new_list.append(student)
    return new_list
students = [("Alice",24,89),("Dante",5,99),("Mark",4,100),("Mary",27,89),("Joyce",29,72)]
print(student_oder_than_eighteen(students))

#Create a Python dictionary that represents a movie database, where the keys are movie titles (strings) 
# and the values are dictionaries containing the director's name (string), release year (integer), and 
# a list of actors (strings). Write a function to print all the movies released in a specific year
# movie_data_base = {
#     {"Title":"Unseen","Directors Name":"Sebastian Osorio","Release Year":2023,"Actors":["Zenzile Mwale","Brooks","Detector"]},
#     {"Title":"Fake Profile","Directors Name":"Rulli Michael","Release Year":2022,"Actors":["Camilla","David","Angela"]},
#     {"Title":"Night Agent","Directors Name":"Alicia Calderon","Release Year":2023,"Actors":["Rose","Fima","Damian"]},
#     {"Title":"Diplomat","Directors Name":"Vincent David","Release Year":2023,"Actors":["Ambassador","Wailer","John"]},
#     {"Title":"365 days","Directors Name":"Mike Mathew","Release Year":2021,"Actors":["Brad","Dante","Danny Alves"]}
# }
# def movies_released_in_specific_year(movie_data_base,year):
#     movies_released_in_year = []
#     for movies, movie in movie_data_base:
#         if movie ["Released Year"] == year:
#             movies_released_in_year.append(movies)
#             if movies_released_in_year:
#                 print(f"Movies released in {year}")
#                 for movie in movies_released_in_year:
#                     print(movies)
#                 else:
#                     print(f"No movies released in {year}")
# movies_released_in_specific_year(movie_data_base,2023)  



#Write a Python program that accepts a list of sentences as input and counts the number of times each word 
#appears across all the sentences. Store the word counts in a dictionary where the keys are the words and the
#values are the counts.
def count_the_number_of_appearances(sentences):
    empty_count = {}
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word in empty_count:
                empty_count[word] += 1
            else:
                empty_count[word] = 1
    return empty_count
sentences = ["I love my life","Coding is what i love most","I will be heading to Nakur"]
print(count_the_number_of_appearances(sentences))

#
                
        
        
    
            
           

    
             
        
  
    
