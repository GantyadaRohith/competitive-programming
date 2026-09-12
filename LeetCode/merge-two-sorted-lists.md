# 🟠 merge-two-sorted-lists — Merge Two Sorted Lists

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Merge two sorted linked lists into a single sorted linked list.

## 🔍 Key Observation

Use a dummy node to simplify the process of linking nodes.

## ⚙️ Algorithm

Initialize a dummy node to serve as the head of the merged list. Traverse both lists, comparing their current nodes and appending the smaller one to the merged list. Continue this process until one of the lists is exhausted. Append the remaining nodes of the other list to the merged list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n + m), where n and m are the lengths of the two lists.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`linked list` `merge` `two lists`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next
        
```

</details>
