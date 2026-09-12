# 🟠 min-cost-to-connect-all-points — Min Cost to Connect All Points

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/min-cost-to-connect-all-points/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Find the minimum cost to connect all points in a plane using the minimum spanning tree algorithm.

## 🔍 Key Observation

Use Kruskal's algorithm to find the minimum spanning tree.

## ⚙️ Algorithm

1. Build an adjacency list representation of the graph where each node is connected to all other nodes with their Manhattan distances.
2. Use a priority queue (min-heap) to always expand the cheapest edge.
3. Keep track of visited nodes to avoid cycles.
4. Add the cost of the edge to the total cost and mark the nodes as visited.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting and heap operations.` | `O(n) auxiliary space for the graph and visited set.` |

## 🏷️ Tags

`short` `lowercase` `algorithm` `graph`

<details>
<summary>💻 View solution</summary>

```python
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
```

</details>
