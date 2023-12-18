121. Best Time to Buy and Sell Stock
Hint: Two - Pointers
Code: 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 #Buying, Selling
        maxProfit = 0
        
        #Is this transaction prfofitable?
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1

        return maxProfit
