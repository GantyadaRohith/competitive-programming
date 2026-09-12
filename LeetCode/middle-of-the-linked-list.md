# 🟠 middle-of-the-linked-list — Middle of the Linked List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/) &nbsp;|&nbsp; **Solved:** 2025-12-12

---

## 📝 Summary

Find the middle node of a singly linked list.

## 🔍 Key Observation

Use two pointers, slow and fast, to traverse the list at different speeds. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. When the fast pointer reaches the end, the slow pointer will be at the middle.

## ⚙️ Algorithm

Initialize two pointers, slow and fast, both pointing to the head of the linked list. Traverse the list with the fast pointer moving two steps and the slow pointer moving one step at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the list.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`linked list` `two pointers` `middle`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

</details>
