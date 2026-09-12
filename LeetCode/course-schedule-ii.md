# 🟠 course-schedule-ii — Course Schedule II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/course-schedule-ii/) &nbsp;|&nbsp; **Solved:** 2026-02-27

---

## 📝 Summary

Given a list of courses and their prerequisites, determine the order in which they can be taken.

## 🔍 Key Observation

The problem can be solved using a depth-first search (DFS) approach to detect cycles and topologically sort the courses.

## ⚙️ Algorithm

1. Build an adjacency list representation of the graph where each course is a node and prerequisites are edges.
2. Use a DFS to traverse the graph. During traversal, mark nodes as visited in three states: 0 (unvisited), 1 (visiting), and 2 (visited).
3. If a node is visited and marked as 1, a cycle is detected, and the course order cannot be determined.
4. If a node is visited and marked as 2, it is part of the topological order and should be added to the stack.
5. If a node is unvisited, start a DFS from that node.
6. After the traversal, the stack contains the course order.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(V + E), where V is the number of courses and E is the number of prerequisites.` | `O(V + E) for the graph and the visited dictionary.` |

## 🏷️ Tags

`dfs` `topological sort` `graph`

<details>
<summary>💻 View solution</summary>

```python
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = {}  
        stack = []

        def dfs(node):
            if node in visited:
                if visited[node] == 1:
                    return False  
                return True      

            visited[node] = 1 

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visited[node] = 2 
            stack.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return stack[::-1]
```

</details>
