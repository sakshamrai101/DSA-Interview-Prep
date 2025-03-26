def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:
    l = 0
    r = len(arr) - 1

    while (r - l + 1) < k:
        if abs(x - arr[l]) > abs(x - arr[r]):
            l += 1
        else:
            r -= 1
        
    return arr[l: r]

print(findClosestElements([1, 2, 3, 4, 5], 4, 3))

