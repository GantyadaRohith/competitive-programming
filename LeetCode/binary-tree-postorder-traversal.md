# 🟠 binary-tree-postorder-traversal — Binary Tree Postorder Traversal

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/binary-tree-postorder-traversal/) &nbsp;|&nbsp; **Solved:** 2025-12-16

---

## 📝 Summary

Given a binary tree, return its postorder traversal.

## 🔍 Key Observation

Use a depth-first search (DFS) approach to traverse the tree in postorder.

## ⚙️ Algorithm

1. Define a helper function `dfs` that takes a node as input.
2. If the node is `None`, return.
3. Recursively call `dfs` on the left child.
4. Recursively call `dfs` on the right child.
5. Append the node's value to the result list `res`.
6. Return the result list `res`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to visiting each node once.` | `O(h) auxiliary space due to the recursion stack, where h is the height of the tree.` |

## 🏷️ Tags

`binary tree` `postorder traversal` `dfs`

<details>
<summary>💻 View solution</summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

        dfs(root)
        return res
```

</details>
