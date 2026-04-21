class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(0, len(prices)):
            s = i + 1
            while i < s and s < len(prices):
                print(prices[i],prices[s])
                p = prices[s] - prices[i]
                if p > profit:
                    profit = p
                s+=1
        return profit
