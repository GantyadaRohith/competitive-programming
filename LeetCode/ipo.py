import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        out = []
        Maxpro = []
        for i in range(len(profits)):
            heapq.heappush(out , (capital[i] , profits[i]))
        for _ in range(k):
            while out and out[0][0] <= w:
                heapq.heappush(Maxpro, -heapq.heappop(out)[1])
            if not Maxpro:
                break
            w+= -heapq.heappop(Maxpro)
        return w