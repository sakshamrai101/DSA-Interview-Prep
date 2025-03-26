# Leetcode 27. Remove Element (Easy)

# ex - 1: nums = [3, 2, 2, 3], val = 3 -> nums = [2,2], 2 ( len(nums) after in place modification )

def removeElement(nums: list[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


nums = [0,1,2,2,3,0,4,2]
print(removeElement(nums, 2))
print(nums)