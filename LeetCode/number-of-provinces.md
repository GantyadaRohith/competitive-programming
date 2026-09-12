# 🟠 number-of-provinces — Number of Provinces

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-provinces/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Given a graph representing connections between provinces, determine the number of distinct provinces.

## 🔍 Key Observation

The problem can be solved using Depth-First Search (DFS) to explore connected components in the graph.

## ⚙️ Algorithm

1. Initialize a counter `cnt` to keep track of the number of provinces and a boolean array `va` to mark visited cities.
2. Iterate through each city in the graph.
3. For each unvisited city, perform a DFS to mark all connected cities as visited.
4. Increment the province count after completing a DFS for a new province.
5. Return the total count of provinces.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loop in the DFS function.` | `O(n) auxiliary space for the boolean array `va`.` |

## 🏷️ Tags

`dfs` `graph` `connected-components`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #dfs
        n = len(isConnected)
        cnt = 0
        va = [False]*n
        def dfs(graph,city):
            for nei in range(n):
                if graph[city][nei] == 1 and not va[nei] :
                    va[nei] = True
                    dfs(graph,nei)
        for i in range(n):
            if not va[i]:
                va[i] = True
                dfs(isConnected,i)
                cnt+=1
        return cnt
```

</details>
