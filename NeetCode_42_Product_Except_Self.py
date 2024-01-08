238. Product of Array Except Self
My Solution:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        preFix = 1
        for i in range(len(nums)):
            res[i] = preFix
            preFix *= nums[i]
        postFix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postFix
            postFix *= nums[i]
        return res
