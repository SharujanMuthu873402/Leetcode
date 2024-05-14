class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        maxProfit = -math.inf
        maxNumber = prices[-1]
        
        for i in range(len(prices) - 2, -1, -1):
            maxProfit = max(maxNumber - prices[i], maxProfit) 
            maxNumber = max(maxNumber, prices[i])
        
        
        return max(0, maxProfit)