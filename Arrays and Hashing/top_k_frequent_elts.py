# Leetcode 343: Top K Frequent Elements 
# Example: nums = [1, 1, 1, 2, 2, 3], k = 2 -> output = [1, 2] as they are the top 2 frequent elements
from collections import Counter

# My approach
def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums) # Build a frequency counter 
    res = [] # List for returning the result

    # Hashmap that stores frequencies sorted by value.
    top_freq = sorted(count.items(), key=lambda x:x[1], reverse=True)

    # Append the top k frequent items to result
    res = [items[0] for items in top_freq[:k]]

    return res

print(topKFrequent([1, 1, 1, 1, 4, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10, 10], 3))
