# Write a Python program to find the kth smallest element in a given list of integers.
def smallest_element(nums):
    nums2 = min(nums)
    print(nums2)
nums = [12,49,2,7,4,19] 
smallest_element(nums) 

# Write a Python program to find the contiguous subsequence with the maximum product in a given list of integers.
# Write a Python program to find the first non-repeating element in a given list of integers.
def non_repeating_numbers(nums):
    count_dict = {}
    for n in nums:
        if n in count_dict:
            count_dict[n] += 1
        else:
            count_dict[n] = 1
    
    for n in nums:
        if count_dict[n] == 1:
            return n 
nums = [2,8,4,2,8,9,3,1,8,6,5]
print(non_repeating_numbers(nums)) 

#Write a Python program to find the maximum difference between two elements in a given list of integers.
def max_difference(nums):
    if len(nums) < 2:
        return None
    num_min = num_max = nums[0]
    for num in nums:
        if num < num_min:
            num_min = num
        elif num > num_max:
            num_max = num
            return num_max - num_min
nums = [12,78,10,27,47,82,64]
print(max_difference(nums)) 

#Write a Python program to find the intersection of n lists.
def intersection_of_lists(nums):
    
            
            
          
    


  
    