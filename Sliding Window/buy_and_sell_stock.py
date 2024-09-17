# Leetcode 121 (Easy)
# Given: an input array prices 
# Output: maxProfit that can be achieved by buying and selling on apprpriate days.


# ex-1: prices = [7, 1, 5, 3, 6, 4]
# output = 6 - 1 = 5

# Observations
# 1. find first smallest price 
# 2. find largest price from that point up until end 
# 3. compute the result

def maxProfit(prices):
    minPrice = float('inf') # sufficiently large value
    maxProfit = -float('inf') # sufficiently small value

    for price in prices:
        if price < minPrice:
            minPrice = price
        else:
            profit = price - minPrice

            maxProfit = max(profit, maxProfit)

    return maxProfit if maxProfit != -float('inf') else 0

print(maxProfit([7,6,4,3,1]))