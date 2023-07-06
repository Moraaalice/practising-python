#Write a function that takes a list of strings as input and returns a dictionary where the keys are the strings and 
#the values are the lengths of the corresponding strings.
def list_of_strings(names):
    empty_dict = {}
    for name in names:
        empty_dict[name] = len(name)
    return empty_dict
names = ["Alice","Joy","Jemimah"]
print(list_of_strings(names))

#Write a function that takes a string as input and returns a dictionary where the keys are the unique characters in 
#the string and the values are the frequencies of those characters.
def takes_in_string(stri):
    empty_dictionary = {}
    for s in stri:
        if s in empty_dictionary:
            empty_dictionary[s] += 1
        else:
            empty_dictionary[s] = 1
    return empty_dictionary
stri = "alicemoraaongongo"
print(takes_in_string(stri))

#Write a function that takes two dictionaries as input and merges them into a single dictionary. If a key is common to 
#both dictionaries, the value in the second dictionary should overwrite the value in the first dictionary.
def take_two_dict(dict1,dict2):
    merging = dict1.copy()
    merging.update(dict2)
    return merging
dict1 = {"Nakuru":32,"Nairobi":47,"Mombasa":1}
dict2 = {"Kilifi":2,"Kisii":30,"Kericho":27}
print(take_two_dict(dict1,dict2))
    


        
