class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(i + 1, len(nums) - i):
                print(j)
                if nums[j] == diff:
                    print (i, j)
                    return (i, j)
        
        return None 

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))

