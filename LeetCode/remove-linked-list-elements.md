# 🟠 remove-linked-list-elements — Remove Linked List Elements

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-linked-list-elements/) &nbsp;|&nbsp; **Solved:** 2025-12-12

---

## 📝 Summary

Remove all nodes from a linked list that have a specific value.

## 🔍 Key Observation

Use a dummy node to simplify edge cases and handle the head node removal.

## ⚙️ Algorithm

Iterate through the linked list. If the current node's value matches the target value, skip it by adjusting the previous node's next pointer. Otherwise, move to the next node. Continue this process until the end of the list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the number of nodes in the linked list.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`linked list` `remove` `dummy node`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next

```

</details>
