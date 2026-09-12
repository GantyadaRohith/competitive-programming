import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        out = []
        res = []
        for i in range(len(points)):
            x1,y1 = points[i]
            dist = math.sqrt(x1**2+y1**2)
            heapq.heappush(out , (dist , i , [x1,y1]))
        for i in range(k):
            res.append(heapq.heappop(out)[2])
        return res