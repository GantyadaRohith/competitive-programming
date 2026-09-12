# 🟠 binary-tree-inorder-traversal — Binary Tree Inorder Traversal

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/binary-tree-inorder-traversal/) &nbsp;|&nbsp; **Solved:** 2025-12-16

---

## 📝 Summary

Inorder traversal of a binary tree, visiting nodes in left-root-right order.

## 🔍 Key Observation

Use a depth-first search (DFS) approach with recursion to traverse the tree.

## ⚙️ Algorithm

1. Define a helper function `dfs` that takes a node as an argument.
2. If the node is `None`, return.
3. Recursively call `dfs` on the left child.
4. Append the node's value to the result list.
5. Recursively call `dfs` on the right child.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to visiting each node once.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary` `tree` `inorder` `traversal`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)   
            res.append(node.val) 
            dfs(node.right)     

        dfs(root)
        return res

```

</details>
