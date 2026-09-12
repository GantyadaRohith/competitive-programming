class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = float('inf')   # minimum price so far
        ma = 0              # maximum profit so far

        for price in prices:
            if price < mi:
                mi = price
            else:
                ma = max(ma, price - mi)

        return ma


