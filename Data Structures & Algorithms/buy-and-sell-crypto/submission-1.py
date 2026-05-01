class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        profit_Max = 0

        while r < len(prices):
            curr_Profit = prices[r] - prices[l]

            if curr_Profit > profit_Max:
                profit_Max = curr_Profit

            elif prices[r] < prices[l]:
                l = r 
                r += 1 
            
            else: 
                r += 1

        return profit_Max