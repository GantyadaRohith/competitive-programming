# 🟠 delete-node-in-a-linked-list — Delete Node in a Linked List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/delete-node-in-a-linked-list/) &nbsp;|&nbsp; **Solved:** 2025-12-19

---

## 📝 Summary

Given a node in a singly-linked list, delete that node from the list.

## 🔍 Key Observation

The node to be deleted is replaced with its next node's value and the next node is skipped.

## ⚙️ Algorithm

1. Store the value of the next node in the current node.
2. Update the current node's value to the next node's value.
3. Skip the next node by updating the current node's next pointer to the node after the next node.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `linked list` `delete node`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        curr.val = node.next.val
        curr.next = node.next.next
```

</details>
