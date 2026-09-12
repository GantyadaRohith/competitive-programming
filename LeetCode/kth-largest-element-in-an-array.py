import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in nums:
            heapq.heappush(pq,-i)
        for i in range(k-1):
            heapq.heappop(pq)
        return -1*heapq.heappop(pq)