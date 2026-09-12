class Solution:
    def maxProduct(self, n: int) -> int:
        pq = []
        for i in str(n):
            heapq.heappush(pq,-(int(i)))
        maxi = -(heapq.heappop(pq))
        mini = -(heapq.heappop(pq))
        return maxi*mini
        
            