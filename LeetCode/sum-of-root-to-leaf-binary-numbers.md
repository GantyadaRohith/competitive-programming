# 🟠 sum-of-root-to-leaf-binary-numbers — Sum of Root To Leaf Binary Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Calculate the sum of all root-to-leaf binary numbers in a binary tree.

## 🔍 Key Observation

Convert each path from root to leaf into a binary number and sum them up.

## ⚙️ Algorithm

Use a stack to traverse the tree. For each node, append its value to the current binary number string. If a node is a leaf, convert the binary string to an integer and add it to the total sum.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n), where n is the number of nodes in the tree, as each node is visited once.` | `O(h), where h is the height of the tree, due to the stack's space usage.` |

## 🏷️ Tags

`binary tree` `dfs` `binary number`

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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        tot = 0
        stack = [(root,str(root.val))]
        while stack:
            node, binVal = stack.pop()
            if node.left:
                stack.append((node.left,binVal+str(node.left.val)))
            if node.right:
                stack.append((node.right,binVal+str(node.right.val)))
            if not node.left and not node.right:
                tot += int(binVal,2)
        return tot
```

</details>
