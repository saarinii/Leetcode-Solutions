#121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = max(prices)
        c = 0
        m = 0
        for i in prices:
            b = min(b,i)
            c = i - b
            m = max(m, c)
        return m