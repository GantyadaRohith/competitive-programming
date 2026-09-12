class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        cnt = 0
        for i in range(len(darts)):
            x1,y1 = darts[i]
            for j in range(360):
                h,k = x1-r*math.sin(j),y1-r*math.cos(j)
                maxDarts = 0
                for l in range(len(darts)):
                    x2,y2 = darts[l]
                    dist = math.sqrt((x2-h)**2 + (y2-k)**2) 
                    if (dist-r) <= 0.001:
                        maxDarts+=1
                cnt = max(cnt,maxDarts)
        return cnt