#Python program that takes a list of integers as input and outputs the list with all the 
# odd numbers doubled.
def doubled_digits(num):
    newlist = []
    for n in num:
        newlist.append(n*2)
        print(newlist)  
# num = [2,4,2,6,7]        
# doubled_digits(num) 
       
#Python program that takes a list of strings as input and outputs the list with all the strings 
# in uppercase.
def strlists(strs):
    newlist = []
    for s in strs:
        newlist.append(s.upper())
        print(newlist)
# strs = ["alice","moraa","dante"]
# strlists(strs)        
        
#Python program that takes a list of strings as input and outputs the longest string in the list.
# def longest_str(names):
#     longest = -1
#     count = 0
#     for n in names:
#      if len[n] > longest:

#Python program that takes a list of integers as input and outputs the sum of all the numbers 
# until it reaches a negative number. Ignore the negative number in the sum.
def addition_of_nums(nums):
    add = 0
    for n in nums:
        if n > 0:
            add+=n
        if n < 0:
            break
        print(add)
# nums = [3,5,1,6,-3,-4,-2]
# addition_of_nums(nums)

#Python program that takes a list of integers as input and outputs the list with all the even numbers removed using a while loop.
def remove_even_nums(nums):
    n = 0
    while n < 10:
        n+=1
        if n%2!=0:
            print(n)
nums = [12,5,3,2,8,9,11]
remove_even_nums(nums)                      
    

         
