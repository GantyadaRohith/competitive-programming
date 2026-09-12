# 🟠 invert-binary-tree — Invert Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/invert-binary-tree/) &nbsp;|&nbsp; **Solved:** 2025-12-16

---

## 📝 Summary

Invert a binary tree by swapping the left and right children of each node.

## 🔍 Key Observation

Swapping the children of each node is the key insight to inverting the tree.

## ⚙️ Algorithm

1. If the current node is null, return it.
2. Swap the left and right children of the current node.
3. Recursively invert the left subtree.
4. Recursively invert the right subtree.
5. Return the current node.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to visiting each node once.` | `O(h) auxiliary space due to recursion stack, where h is the height of the tree.` |

## 🏷️ Tags

`binary` `tree` `invert` `recursion`

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
            

```

</details>
