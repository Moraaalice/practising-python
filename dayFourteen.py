#Write a Python program to find the sum of all elements in a list.
def add_list(numbers):
    add = 0
    for n in numbers:
        add+=n
    return add
print(add_list([12,4,1,3,]))
#Write a Python program to find the largest and smallest elements in a list.
def smallest_largest(nums):
    print(min(nums))
    print(max(nums))
smallest_largest([12,45,89,10])
# Write a Python program to find the second largest and second smallest elements in a list.
def second_largest_second_smallest(digits):
    digits.sort()
    print(digits[1])
    print(digits[-2])
second_largest_second_smallest([12,4,5,14,20,49,10,20])
# Write a Python program to find the frequency of all elements in a list.
def frequency(places):
    empty = {}
    for p in places:
        if p in empty:
            empty[p] =+ 1
        else:
            empty[p] = 1
    print(empty)
frequency(["kisii","nakuru","nairobi","kisii","nakuru","migori","nakuru","mombasa"]) 
#Write a Python program to remove all duplicates from a list.
def remove_duplicates(fruits):
    fruits = set(fruits)
    print(fruits)
remove_duplicates(["kiwi","mango","mango","mango","kiwi","orange","watermelon","orange"])  
#Write a Python program to reverse a list in place.
def reverse_list(nums):
    print(nums[::-1])
reverse_list([12,56,32,90,45,38]) 
#Write a Python program to find the union and intersection of two lists.
digits1 = [12,4,2,3,8,9,10]
digits2 = [12,5,3,2,10,4,29,30]
    #finding the union
union = set(digits1) | set(digits2) 
    #finding the intersection
intersection = set(digits1)  & set(digits2) 
print(union) 
print(intersection)

# Write a Python program to find the missing number in a given list of integers.
def find_missing_number(numbers):
    total = sum(range(1,len(numbers)+ 1))
    return total-sum(numbers)

numbers = [1,3,5,8,6,2]
missing_number = find_missing_number(numbers)
print(missing_number)

# Write a Python program to find the subsequence with the maximum sum in a given list of integers.

# Write a Python program to find the median of a given list of integers.
def find_median(nums):
    nums.sort()
    count = len(nums)
    if count %2 == 0:
        median = (nums[count // 2] + nums(count // 2 - 1))/2
    else:
        median = nums[count // 2]
    return median
nums = [2,6,4,9,1,6,3]
print(find_median(nums))

#Write a Python program to remove all negative numbers from a list.
def remove_negative(nums):
    newList = []
    for n in nums:
        if n > 0:
            newList.append(n)
    return newList
nums = [12,-3,3,4,-7,9,1,-5,-7,-9]
print(remove_negative(nums))

#Write a Python program to sort a list in descending order.
def sort_list(num):
    num.sort()
    print(num)
num = [3,4,9,19,5,35,23,48]    
sort_list(num)  

# Write a Python program to merge two sorted lists into a single sorted list.
def merging_two_lists(num,nums):
    merged = []
    a = 0
    b = 0
    while a < len(num) and b < len(nums):
        if num[a] <= nums[b]:
            merged.append(num[a])
        a += 1
   
    else:
        merged.append(nums[b])
        b += 1
    merged += num[a:]
    merged += nums[b:]
    return merged
num = [23,12,6,7,8,9]
nums = [10,2,15,18,5,11]
merged = merging_two_lists(num,nums)
print(merged)        

 
        
 
        
    
        
        

     
    
   
  
    
    

        

