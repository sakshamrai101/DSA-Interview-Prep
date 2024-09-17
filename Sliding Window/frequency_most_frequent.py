# Leetcode 1838. Frequency of the most Frequent Element 


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        # Step 1. Sort the array
        nums.sort()

        # Step 2. Initialise variables 
        l = 0
        total_operations = 0
        max_frequency = 0

        # Step 3. Sliding Window Approach 
        for r in range(len(nums)):
            # Add the difference to total_operations
            total_operations += nums[r]

            # Step 4: Check if operations exceed k
            while total_operations + k < nums[r] * (r - l + 1):
                total_operations -= nums[l]
                l += 1

            # Calculate the current window size and update max frequency 
            max_frequency = max(max_frequency, r - l + 1)

        return max_frequency


