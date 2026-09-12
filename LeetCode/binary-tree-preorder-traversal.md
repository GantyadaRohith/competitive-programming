# 🟠 binary-tree-preorder-traversal — Binary Tree Preorder Traversal

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/binary-tree-preorder-traversal/) &nbsp;|&nbsp; **Solved:** 2025-12-16

---

## 📝 Summary

Given a binary tree, return its preorder traversal.

## 🔍 Key Observation

Preorder traversal involves visiting the root node first, then the left subtree, and finally the right subtree.

## ⚙️ Algorithm

The solution uses a recursive approach to traverse the tree. It defines a helper function `dfs` that appends the value of the current node to the result list and then recursively traverses the left and right subtrees.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to visiting each node exactly once.` | `O(h) auxiliary space due to the recursion stack, where h is the height of the tree.` |

## 🏷️ Tags

`binary tree` `preorder` `traversal` `recursion`

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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return res

```

</details>
