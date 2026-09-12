# 🟠 diameter-of-binary-tree — Diameter of Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/) &nbsp;|&nbsp; **Solved:** 2026-07-06

---

## 📝 Summary

Given a binary tree, find the length of the longest path between any two nodes.

## 🔍 Key Observation

The diameter of the tree is the length of the longest path between any two nodes, which can be found by calculating the height of the tree and summing the heights of its left and right subtrees.

## ⚙️ Algorithm

1. Define a helper function `height` that calculates the height of a subtree and updates the diameter if the current path length is greater than the stored diameter.
2. Recursively calculate the height of the left and right subtrees.
3. Update the diameter if the sum of the heights of the left and right subtrees is greater than the current diameter.
4. Return the height of the current subtree plus one.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the number of nodes in the tree, as each node is visited once.` | `O(h) where h is the height of the tree, due to the recursion stack.` |

## 🏷️ Tags

`binary tree` `depth-first search` `diameter`

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            self.dia = max(self.dia,left+right)
            return 1+max(left,right)
        height(root)
        return self.dia
        
```

</details>
