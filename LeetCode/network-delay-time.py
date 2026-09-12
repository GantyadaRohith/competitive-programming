class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])
        minHeap = [(0,k)]
        dist = {}
        while minHeap:
            d, node = heapq.heappop(minHeap)

            if node in dist:
                continue   

            dist[node] = d

            for nei, weight in graph[node]:
                if nei not in dist:
                    heapq.heappush(minHeap, (d + weight, nei))
    
        if len(dist) != n:
            return -1
        return max(dist.values())
        