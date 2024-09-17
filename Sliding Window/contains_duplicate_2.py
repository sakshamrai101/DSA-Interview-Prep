# Leetcode 219: Easy: Contains Duplicate 2

# Given: int array nums and int k
# Output: true if for two distinct i, j nums[i] == nums[j] and abs(i -j) <= k


# ex - 1: nums = [1, 2, 3, 1], k = 3, output = true because nums[3] == nums [0].

# Thought Process:
# 1. declare two pointers l and r at the start of the array and + k ahead of l, respectively.
# 2. while l < r and r < len(nums): 
# 3. check if nums[l] == nums[r]: return true 
# 4. else: increment pointers: l+= 1 and r+= k
# 5. return false outside of the loop.
 

def containsNearbyDuplicate(nums, k):
    l, r = 0, k

    while l < r and r < len(nums):

        print ("Current Val at l pointer: ", nums[l])
        print ("Current Val at r pointer: ", nums[r])
        if nums[l] == nums[r]:
            print("l pointer value: ", nums[l])
            print("r pointer value: ", nums[r])
            return True
        else:            
            l += k
            r += k
    return False 


print(containsNearbyDuplicate([1,2,3,1], 3))

# Good approach but this is is not optimal. 
# Optimal approach: use a sliding window with a set. 
# initialise L = 0 and use r in the for counter.
# check if window len is valid: if not remove character.
# check if nums[l] is in set, we have a repeated character: return true, else add the character to the set.

def containsNearbyDuplicateOptimal(nums, k):
    L = 0
    window = set()

    for r in range(len(nums)):
        if r - l > k:
            window.remove(nums[l])
            l += 1
        if nums[r] in window:
            return True
        
        window.add(nums[r])
    return False 

