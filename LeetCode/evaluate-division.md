# 🟠 evaluate-division — Evaluate Division

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/evaluate-division/) &nbsp;|&nbsp; **Solved:** 2026-03-02

---

## 📝 Summary

Given a set of equations and their values, evaluate the value of division queries.

## 🔍 Key Observation

The solution uses a graph to represent the relationships between variables and employs depth-first search (DFS) to find the value of each query.

## ⚙️ Algorithm

1. Build a graph where each variable is a node and each equation is an edge with a weight representing the division value. 2. For each query, perform a DFS starting from the numerator to the denominator, multiplying weights along the path. 3. If a variable is not found or the path does not exist, return -1.0.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `graph` `dfs`

<details>
<summary>💻 View solution</summary>

```python
from typing import List
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        i=0
        for x,y in equations:
            graph[x].append([y,values[i]])
            graph[y].append([x,1/values[i]])
            i+=1
        def dfs(src, dst, visited):
            if src not in graph:
                return -1.0

            if src == dst:
                return 1.0

            visited.add(src)

            for neighbor, weight in graph[src]:
                if neighbor not in visited:
                    result = dfs(neighbor, dst, visited)
                    if result != -1.0:
                        return result * weight

            return -1.0
        result = []
        for x,y in queries:
            result.append(dfs(x,y,set())) 
        return result
        
```

</details>
