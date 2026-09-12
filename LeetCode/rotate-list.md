# 🟠 rotate-list — Rotate List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rotate-list/) &nbsp;|&nbsp; **Solved:** 2026-07-02

---

## 📝 Summary

Rotate the linked list to the right by k places.

## 🔍 Key Observation

The key insight is to find the new head of the rotated list by identifying the node that will be the new tail.

## ⚙️ Algorithm

1. Traverse the list to find its length and calculate the effective rotation needed (k % length).
2. Traverse the list again to find the node that will be the new tail.
3. Connect the new tail to the head to form the rotated list.
4. Break the connection between the new tail and the old tail.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the two traversals of the list.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`linked list` `rotation` `two pointers`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        if temp is None:
            return head
        if temp.next is None:
            return head
        cnt = 0
        temp = head
        while temp is not None:
            temp = temp.next
            cnt+=1
        k%=cnt
        temp = head
        for i in range(k):
            temp = head
            while temp.next.next is not None:
                temp = temp.next
            temp.next.next = head
            head = temp.next
            temp.next = None
        return head
```

</details>
