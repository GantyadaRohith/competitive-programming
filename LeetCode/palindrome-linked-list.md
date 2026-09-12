# 🟠 palindrome-linked-list — Palindrome Linked List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/palindrome-linked-list/) &nbsp;|&nbsp; **Solved:** 2026-07-02

---

## 📝 Summary

Determine if a singly linked list is a palindrome.

## 🔍 Key Observation

Reverse the second half of the list and compare it to the first half.

## ⚙️ Algorithm

1. Use two pointers, `slow` and `high`, to find the middle of the list.
2. Reverse the second half of the list starting from the middle.
3. Compare the reversed second half with the first half of the list.
4. Return `True` if they are the same, otherwise `False`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass to find the middle and the second pass to compare the halves.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`linked list` `two pointers` `reverse`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head 
        high = head 
        while high is not None and high.next is not None:
            slow = slow.next
            high = high.next.next
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first = head
        second = prev
        
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
```

</details>
