# 🟠 sort-list — Sort List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sort-list/) &nbsp;|&nbsp; **Solved:** 2025-12-12

---

## 📝 Summary

Sorts a singly linked list in ascending order.

## 🔍 Key Observation

The solution uses a merge sort algorithm to efficiently sort the linked list.

## ⚙️ Algorithm

The algorithm works by recursively splitting the linked list into two halves, sorting each half, and then merging the sorted halves back together. This is done using a helper function `mergesort` that calls `split` to divide the list and `merge` to combine the sorted halves.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to the merge sort algorithm.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`linked list` `sort` `merge sort`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergesort(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            left = mergesort(left)
            right = mergesort(right)
            return merge(left, right)

        def split(head):
            # Use fast = head.next so slow stops at the end of left half
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid

        def merge(l, r):
            dummy = tail = ListNode()
            while l and r:
                if l.val < r.val:
                    tail.next = l
                    l = l.next
                else:
                    tail.next = r
                    r = r.next
                tail = tail.next
            tail.next = l or r
            return dummy.next

        return mergesort(head)

```

</details>
