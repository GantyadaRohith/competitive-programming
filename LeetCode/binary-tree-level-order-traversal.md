# 🟠 binary-tree-level-order-traversal — Binary Tree Level Order Traversal

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/) &nbsp;|&nbsp; **Solved:** 2025-12-16

---

## 📝 Summary

Given a binary tree, return its level order traversal (top-down) as a list of lists of integers.

## 🔍 Key Observation

Use a queue to perform a breadth-first search (BFS) to traverse the tree level by level.

## ⚙️ Algorithm

1. Initialize an empty list `res` to store the result and a queue `q` with the root node.
2. While the queue is not empty, do the following:
   - Initialize an empty list `level` to store the current level's values.
   - Get the size of the queue to know how many nodes are at the current level.
   - For each node at the current level, add its value to `level` and enqueue its left and right children if they exist.
   - Append `level` to `res`.
3. Return `res`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the number of nodes in the tree, as each node is processed once.` | `O(n) for the queue and the result list, as they store all nodes and levels.` |

## 🏷️ Tags

`binary tree` `level order traversal` `queue` `bfs`

<details>
<summary>💻 View solution</summary>

```python
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level = []
            size = len(q)   

            for _ in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res

```

</details>
