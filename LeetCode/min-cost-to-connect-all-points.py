from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        
        graph = defaultdict(list)
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((j, dist))
                graph[j].append((i, dist))
        
        visited = set()
        minHeap = [(0, 0)]
        total_cost = 0
        
        while len(visited) < n:
            weight, node = heapq.heappop(minHeap)
            
            if node in visited:
                continue
            
            visited.add(node)
            total_cost += weight
            
            for nei, w in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (w, nei))
        
        return total_cost