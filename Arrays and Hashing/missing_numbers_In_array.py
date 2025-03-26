def findDisappearedNumbers(nums: list[int]) -> list[int]:
    nums.sort()
    res = []
    n = len(nums)

    for i in range(1, n + 1):
        print(nums[i-1])
        if i != nums[i - 1] and nums[i] != nums[i - 1] and i < n:
            res.append(i)

    return res

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))