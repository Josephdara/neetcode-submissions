class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for val in prices:
            min_price = min(min_price, val)

            temp_profit = val - min_price
            max_profit = max(max_profit, temp_profit)
        return max_profit