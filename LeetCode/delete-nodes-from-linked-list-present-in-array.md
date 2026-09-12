# 🟠 delete-nodes-from-linked-list-present-in-array — Delete Nodes From Linked List Present in Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/) &nbsp;|&nbsp; **Solved:** 2025-12-19

---

## 📝 Summary

Given a linked list and an array of values, remove nodes from the linked list that have values present in the array.

## 🔍 Key Observation

Use a set for quick lookup of values to delete.

## ⚙️ Algorithm

Initialize a dummy node to simplify edge cases. Traverse the linked list, and if the next node's value is in the set, skip it. Otherwise, move to the next node.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the linked list.` | `O(m) for the set of values to delete, where m is the length of the array.` |

## 🏷️ Tags

`linked list` `array` `set` `delete`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        nums = set(nums)
        while curr and curr.next:
            if curr.next.val in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
```

</details>
