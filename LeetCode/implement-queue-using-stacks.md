# 🟠 implement-queue-using-stacks — Implement Queue using Stacks

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Implement a queue using two stacks to manage elements.

## 🔍 Key Observation

The key insight is to use two stacks to reverse the order of elements between them when needed.

## ⚙️ Algorithm

1. The `push` method simply appends the element to the `in_stk` stack.
2. The `pop` method first calls `peek` to ensure the `out_stk` is populated, then pops the top element from `out_stk`.
3. The `peek` method checks if `out_stk` is empty; if so, it reverses the `in_stk` to `out_stk`.
4. The `empty` method checks if both stacks are empty.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) for `pop` and `peek` due to the reversal of stacks.` | `O(n) for auxiliary space used by the stacks.` |

## 🏷️ Tags

`stacks` `queue` `implementation`

<details>
<summary>💻 View solution</summary>

```python
class MyQueue(object):
    def __init__(self):
        self.in_stk = []
        self.out_stk = []
	# Push element x to the back of queue...
    def push(self, x):
        self.in_stk.append(x)
	# Remove the element from the front of the queue and returns it...
    def pop(self):
        self.peek()
        return self.out_stk.pop()
	# Get the front element...
    def peek(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]
	# Return whether the queue is empty...
    def empty(self):
        return not self.in_stk and not self.out_stk
```

</details>
