# 🟠 network-delay-time — Network Delay Time

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/network-delay-time/) &nbsp;|&nbsp; **Solved:** 2026-03-02

---

## 📝 Summary

Given a network of nodes and edges with weights, find the maximum time it takes for all nodes to receive a signal starting from a given node.

## 🔍 Key Observation

Use Dijkstra's algorithm to find the shortest path from the source node to all other nodes.

## ⚙️ Algorithm

1. Build an adjacency list representation of the graph from the input times list.
2. Initialize a min-heap with the source node and its distance (0).
3. While the heap is not empty:
   - Pop the node with the smallest distance.
   - If the node is already visited, skip it.
   - Mark the node as visited and update its distance in the dist dictionary.
   - For each neighbor of the current node, if the neighbor is not visited, push it into the heap with the updated distance.
4. After processing all nodes, check if all nodes are visited. If not, return -1.
5. Return the maximum distance found in the dist dictionary.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O((V + E) log V) due to Dijkstra's algorithm.` | `O(V + E) for the graph and the dist dictionary.` |

## 🏷️ Tags

`short` `lowercase` `network` `algorithm`

<details>
<summary>💻 View solution</summary>

```python
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
        
```

</details>
