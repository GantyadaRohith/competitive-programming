# 🟠 kth-smallest-element-in-a-bst — Kth Smallest Element in a BST

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) &nbsp;|&nbsp; **Solved:** 2025-12-16

---

## 📝 Summary

Find the kth smallest element in a binary search tree (BST) using an in-order traversal.

## 🔍 Key Observation

In-order traversal of a BST visits nodes in ascending order.

## ⚙️ Algorithm

1. Define a helper function `dfs` that performs an in-order traversal of the BST.
2. Append each node's value to the `res` list.
3. Return the kth element from the `res` list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to visiting each node once.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary search tree` `in-order traversal` `recursion`

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)

        return res[k-1]
```

</details>
