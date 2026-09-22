class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float("inf")
        max_profit = 0

        for current in prices:
            if current < min_buy:
                min_buy = current
            elif current - min_buy > max_profit:
                max_profit = current - min_buy
        
        return max_profit