# 🟠 cheapest-flights-within-k-stops — Cheapest Flights Within K Stops

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Find the cheapest price to travel from a source city to a destination city within a maximum number of stops.

## 🔍 Key Observation

Use a dynamic programming approach to keep track of the minimum cost to reach each city within the allowed number of stops.

## ⚙️ Algorithm

Initialize a distance array to store the minimum cost to reach each city. Iterate through each stop up to k, updating the distance array based on the flights available. The final distance to the destination city is returned, or -1 if it's not reachable within the given constraints.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(k * n^2) due to the nested loops iterating over flights and the distance array.` | `O(n) auxiliary space for the distance array.` |

## 🏷️ Tags

`short` `lowercase` `dynamic programming` `shortest path`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            temp = dist.copy()
            for u, v, w in flights:
                if dist[u] != float('inf'):
                    temp[v] = min(temp[v], dist[u] + w)
            dist = temp

        return dist[dst] if dist[dst] != float('inf') else -1
```

</details>
