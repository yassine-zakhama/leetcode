from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, l = 0, 0
        for r in range(1, len(prices)):
            buy_price, sell_price = prices[l], prices[r]
            if sell_price < buy_price:
                l = r
            else:
                res = max(res, sell_price - buy_price)
        return res
