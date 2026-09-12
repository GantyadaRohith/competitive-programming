# 🟠 remove-nth-node-from-end-of-list — Remove Nth Node From End of List

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) &nbsp;|&nbsp; **Solved:** 2026-07-02

---

## 📝 Summary

Remove the nth node from the end of a singly linked list.

## 🔍 Key Observation

Use a dummy node to handle edge cases and a two-pointer technique to find the node to remove.

## ⚙️ Algorithm

1. Initialize a dummy node pointing to the head and a temporary pointer to the dummy node.
2. Traverse the list to count the total number of nodes.
3. Calculate the position of the node to remove from the start of the list.
4. Move the temporary pointer to the node before the one to be removed.
5. Update the next pointer of the node before the one to be removed to skip the node to be removed.
6. Return the next of the dummy node as the new head of the list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the list.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`linked list` `two pointers` `dummy node`

<details>
<summary>💻 View solution</summary>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=1
        dummy=ListNode(0,head)
        temp=dummy
        while temp.next:
            c+=1
            temp=temp.next
        pos=c-n-1
        temp=dummy
        for _ in range(pos):
            temp=temp.next
        temp.next=temp.next.next
        return dummy.next
```

</details>
