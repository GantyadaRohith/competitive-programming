# 🟠 construct-binary-tree-from-preorder-and-inorder-traversal — Construct Binary Tree from Preorder and Inorder Traversal

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) &nbsp;|&nbsp; **Solved:** 2025-12-17

---

## 📝 Summary

Given preorder and inorder traversal arrays, construct a binary tree.

## 🔍 Key Observation

The first element of preorder is the root, and the inorder traversal divides the tree into left and right subtrees.

## ⚙️ Algorithm

1. Use a deque for preorder to efficiently pop elements.
2. Recursively build the tree by finding the root in the inorder array.
3. Split the inorder array into left and right subtrees based on the root's index.
4. Recursively build the left and right subtrees.
5. Return the root of the constructed tree.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the inorder array and the recursive calls.` | `O(n) auxiliary space due to the recursion stack and the deque.` |

## 🏷️ Tags

`binary tree` `preorder` `inorder` `recursive`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        preorder = deque(preorder)

        def build(preorder, inorder):
            if inorder:
                idx = inorder.index(preorder.popleft())
                root = TreeNode(inorder[idx])

                root.left = build(preorder, inorder[:idx])
                root.right = build(preorder, inorder[idx+1:])

                return root

        return build(preorder, inorder)
```

</details>
