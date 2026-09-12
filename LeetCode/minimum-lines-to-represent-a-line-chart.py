class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        cnt = 1
        stockPrices.sort()
        if len(stockPrices)<=1:
            return 0
        x1,y1 = stockPrices[0]
        x2,y2 = stockPrices[1]
        prev_dy = (y2-y1)
        prev_dx = (x2-x1)
        for i in range(1,len(stockPrices)-1):
            x1,y1 = stockPrices[i]
            x2,y2 = stockPrices[i+1]
            dy,dx = (y2-y1),(x2-x1)
            if prev_dy*dx!=prev_dx*dy:
                cnt+=1
                prev_dx,prev_dy = dx,dy
        return cnt
            