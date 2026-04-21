class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        l = 0
        profit = 0
        for r in range(0, len(prices)):
            p = prices[r] - prices[l]
            print("l", l, "r", r)
            print('p', p)
            print("profit", profit)
            print("minPrice", minPrice)
            if p > profit:
                profit = p
            if prices[r] < minPrice:
                minPrice = prices[r]
                l = r
            print("aprofit", profit)
            print("aminPrice", minPrice)
        return profit        
    