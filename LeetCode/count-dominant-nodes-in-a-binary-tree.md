# 🟠 count-dominant-nodes-in-a-binary-tree — Count Dominant Nodes in a Binary Tree

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/) &nbsp;|&nbsp; **Solved:** 2026-07-19

---

## 📝 Summary

Count the number of nodes in a binary tree where the node's value is greater than or equal to the maximum value of its left and right subtrees.

## 🔍 Key Observation

The key insight is to recursively traverse the tree and compare each node's value with the maximum values of its subtrees.

## ⚙️ Algorithm

1. Define a recursive function `dfs` that returns a tuple `(maxi, cnt)` where `maxi` is the maximum value in the subtree rooted at the current node, and `cnt` is the count of nodes in the subtree rooted at the current node that are greater than or equal to `maxi`. 2. If the current node is `None`, return `(-inf, 0)`. 3. Recursively call `dfs` on the left and right subtrees. 4. Calculate `maxi` as the maximum of the current node's value and the maximum values of its subtrees. 5. If the current node's value is equal to `maxi`, increment `cnt` by 1. 6. Return `(maxi, cnt)`. 7. Call `dfs` on the root of the tree and return `cnt`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the tree.` | `O(h) auxiliary space due to the recursion stack.` |

## 🏷️ Tags

`binary tree` `recursion` `tree traversal`

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
    def countDominantNodes(self, root):
        cnt = 0
        def dfs(node):
            if not node:
                return float("-inf"), 0
            lm,lc = dfs(node.left)
            rm,rc = dfs(node.right)
            maxi = max(node.val, lm, rm)
            cnt = lc + rc
            if node.val == maxi:
                cnt += 1
            return maxi, cnt
        maxi,cnt = dfs(root)
        return cnt
```

</details>
