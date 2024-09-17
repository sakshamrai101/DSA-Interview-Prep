# Leetcode 1343: (Medium) Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

# Given: int array nums, int k and int threshold
# output: No. of sub-arrays to with window size k and avg >= threshold

def numOfSubarrays(arr, k, threshold):
    window_sum = 0
    l = 0
    counter = 0

    for r in range(len(arr)):
        window_sum += arr[i]

        if r - l + 1 == k:
            avg = window_sum / k
            if avg >= threshold:
                counter += 1
            
            window_sum -= arr[l]
            l -= 1

    return counter


        

        
