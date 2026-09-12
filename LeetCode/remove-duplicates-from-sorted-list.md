# 🟠 remove-duplicates-from-sorted-list — Remove Duplicates from Sorted List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Remove duplicates from a sorted linked list.

## 🔍 Key Observation

Use a set to track unique values and then sort them to reconstruct the list.

## ⚙️ Algorithm

1. Traverse the linked list and add each node's value to a set.
2. Convert the set to a list and sort it.
3. Create a new linked list with the sorted values.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(n) auxiliary space.` |

## 🏷️ Tags

`linked list` `set` `sort`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        temp = head
        s = set()
        while temp!=None:
            s.add(temp.val)
            temp = temp.next
        s = list(s)
        s.sort()
        dummy = ListNode()
        temp = dummy
        f = 0
        for i in s:
            if f == 0:
                temp.val = i
                f+=1
            else:
                temp.next = ListNode(i)
                temp = temp.next
        return dummy 

```

</details>
