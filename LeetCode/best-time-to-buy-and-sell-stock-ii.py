class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = float('inf')   
        ma = 0              
        total = 0
        for price in prices:
            if price < mi:
                mi = price
            else: 
                res = price - mi
                mi = price
                total+=res
        return total

