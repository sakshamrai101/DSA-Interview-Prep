167. Two Sum II - Input Array Is Sorted
My Solution:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      res = []
      l, r = 0, len(numbers) - 1
      while l < r:
        totalSum = numbers[l] + numbers[r]
        if totalSum > target:
          r -= 1
        elif totalSum < target:
          l += 1
        else:
          return [l + 1, r + 1]
    return res
