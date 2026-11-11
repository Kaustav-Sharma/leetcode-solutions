# Last updated: 11/11/2026, 3:16:19 pm
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit