import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxheap = []
        fuel = startFuel
        n = len(stations)
        stopC = 0
        i = 0
        while fuel < target:
            while i < n and stations[i][0] <= fuel:
                heapq.heappush(maxheap,-stations[i][1])
                i+=1
            if not maxheap :
                return -1
            fuel += -heapq.heappop(maxheap)
            stopC += 1
        return stopC