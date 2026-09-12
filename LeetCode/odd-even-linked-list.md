# 🟠 odd-even-linked-list — Odd Even Linked List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/odd-even-linked-list/) &nbsp;|&nbsp; **Solved:** 2025-12-19

---

## 📝 Summary

Given a linked list, rearrange it such that all odd-indexed nodes come before even-indexed nodes.

## 🔍 Key Observation

The solution uses two pointers to separate odd and even nodes while maintaining their order.

## ⚙️ Algorithm

1. Initialize two pointers, `odd` and `even`, to the head of the list and its next node, respectively.
2. Traverse the list, connecting odd-indexed nodes to each other and even-indexed nodes to each other.
3. Connect the end of the odd-indexed list to the head of the even-indexed list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the list.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`linked list` `two pointers` `odd even`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return  None
        odd = head
        evenhead= head.next
        even = evenhead

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head
```

</details>
