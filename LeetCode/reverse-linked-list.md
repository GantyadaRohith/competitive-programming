# 🟠 reverse-linked-list — Reverse Linked List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reverse-linked-list/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Reverse a singly linked list.

## 🔍 Key Observation

The key insight is to use three pointers: prev, curr, and nxt to reverse the links.

## ⚙️ Algorithm

1. Initialize three pointers: prev, curr, and nxt. prev is initially set to the head, curr is set to head.next, and nxt is set to head.next.next.
2. Iterate through the list, reversing the direction of each link by setting curr.next to prev.
3. Move the prev, curr, and nxt pointers forward.
4. Once the loop ends, prev will be pointing to the new head of the reversed list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the number of nodes in the linked list.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`linked` `list` `reverse`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if head == None:
            return head
        elif prev.next == None:
            return head
        elif prev.next.next == None:
            head = prev.next
            head.next = prev
            prev.next = None
            return head
        else:
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev


            
        
```

</details>
