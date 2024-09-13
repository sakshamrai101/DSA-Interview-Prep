78. Subsets
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # Case of including the element case. 
            subset.append(nums[i])
            dfs(i+1)

            # Case of not inlcuding the not including the element. 
            subset.pop()
            dfs(i+1)
        dfs(0)
        return result
