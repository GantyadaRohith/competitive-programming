# 🟠 linked-list-cycle — Linked List Cycle

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/linked-list-cycle/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Determine if a linked list contains a cycle by using Floyd's Tortoise and Hare algorithm.

## 🔍 Key Observation

The algorithm uses two pointers moving at different speeds to detect cycles.

## ⚙️ Algorithm

1. Initialize two pointers, slow and fast, both starting at the head of the list.
2. Move slow one step at a time and fast two steps at a time.
3. If there is a cycle, the fast pointer will eventually meet the slow pointer.
4. If the fast pointer reaches the end of the list (null), there is no cycle.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the two-pointer traversal.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`linked list` `cycle detection` `floyd's tortoise and hare`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False
        else:
            slow  = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False
```

</details>
