# 🟠 binary-tree-maximum-path-sum — Binary Tree Maximum Path Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/) &nbsp;|&nbsp; **Solved:** 2026-03-07

---

## 📝 Summary

Given a binary tree, find the maximum path sum from any node to any node.

## 🔍 Key Observation

The key insight is to use a depth-first search (DFS) to calculate the maximum path sum for each node, considering the path that includes the node and its subtrees.

## ⚙️ Algorithm

1. Define a helper function `dfs` that takes a node as input and returns the maximum path sum that can be obtained from that node to any descendant node. This function also updates the global maximum path sum `maxi` if a larger path sum is found.
2. For each node, calculate the maximum path sum that includes the node and its left and right subtrees. If the left or right subtree path sum is negative, it is ignored as it would decrease the overall path sum.
3. Update the global maximum path sum `maxi` with the maximum of the current node's value plus the left and right subtree path sums.
4. Return the maximum path sum that includes the current node.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through each node.` | `O(h) auxiliary space due to the recursion stack, where h is the height of the tree.` |

## 🏷️ Tags

`binary tree` `dfs` `path sum`

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        maxi = -float('inf')
        def dfs(node):
            nonlocal maxi
            left_gain,right_gain = 0,0
            if node.left is not None:
                left_gain = max(dfs(node.left), 0)
            if node.right is not None:
                right_gain = max(dfs(node.right), 0)
            ans = left_gain + node.val + right_gain
            maxi = max(maxi,ans)
            return node.val + max(left_gain, right_gain)
        dfs(root)
        return maxi
```

</details>
