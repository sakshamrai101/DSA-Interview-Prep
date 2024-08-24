# Binary Search Algorithm Template


def binarySearch(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = 0, len(array)  # In general, left, right = min(search_space), max(search_space), INCLUDE ALL ELEMENTS

    while left < right: 
        mid = (left + (right - left)) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1

    return left

# 278. First Bad Version [Easy]
# You are a product manager and currently leading a team to develop a new product. Since each version is developed 
# based on the previous version, all the versions after a bad version are also bad. Suppose you have n versions 
# [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad. 
# You are given an API bool isBadVersion(version) which will return whether version is bad.


def firstBad(stream) -> int:
    left, right = 1, len(stream)

    while left < right:
        mid = (left + (right - left)) // 2
        if isBadVersion(stream[mid]):
            right = mid
        left = mid + 1
    return left 




def mySqrt(x: int) -> int:
    left, right = 0, x + 1

    while left < right:
        mid = (left + (right - left)) // 2
        if mid * mid > x:
            right = mid
        else:
            left = mid + 1
    return left - 1

def insertPos(array: List[int], number: int) -> int:
    left, right = 0, len(array)

    while left < right:
        mid = (left + (left - right)) // 2
        if array[mid] >= number:
            right = mid
        else:
            left = mid + 1
    return left 





