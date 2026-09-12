# 🟠 lowest-common-ancestor-of-a-binary-tree — Lowest Common Ancestor of a Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) &nbsp;|&nbsp; **Solved:** 2026-05-13

---

## 📝 Summary

Find the lowest common ancestor (LCA) of two nodes in a binary tree.

## 🔍 Key Observation

The solution uses a recursive approach to traverse the tree and find the LCA.

## ⚙️ Algorithm

The algorithm recursively searches for nodes p and q in the tree. If both nodes are found in different subtrees, the current node is the LCA. If only one node is found, the other node must be in its subtree.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the need to visit each node in the tree.` | `O(h) auxiliary space due to the recursion stack, where h is the height of the tree.` |

## 🏷️ Tags

`binary tree` `recursion` `lowest common ancestor`

<details>
<summary>💻 View solution</summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        return left or right
```

</details>
