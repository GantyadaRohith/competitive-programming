# 🟠 clone-graph — Clone Graph

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/clone-graph/) &nbsp;|&nbsp; **Solved:** 2026-07-25

---

## 📝 Summary

Clone a given undirected graph where each node has a unique value.

## 🔍 Key Observation

Use a depth-first search (DFS) to traverse the graph and clone each node while maintaining connections.

## ⚙️ Algorithm

1. Create a hash map to store cloned nodes for quick lookup.
2. Define a helper function `dfs` that takes a node and returns its clone.
3. If the node is already cloned, return the clone.
4. Create a new node with the same value as the current node and store it in the hash map.
5. Recursively clone all neighbors of the current node and add them to the clone's neighbors list.
6. Return the clone of the starting node.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the number of nodes in the graph, as each node is visited once.` | `O(n) for the hash map storing cloned nodes and the recursion stack.` |

## 🏷️ Tags

`dfs` `graph` `clone`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Base Case 1: Empty input returns None
        if not node:
            return None
        
        cloned = {}

        def dfs(curr: 'Node') -> 'Node':
            # If already cloned, return the cloned instance to preserve connections/cycles
            if curr in cloned:
                return cloned[curr]
            
            # Create clone and store in hash map BEFORE recursive calls
            copy = Node(curr.val)
            cloned[curr] = copy
            
            # Recursively copy all neighbors (handles empty neighbors list automatically)
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy

        return dfs(node)
```

</details>
