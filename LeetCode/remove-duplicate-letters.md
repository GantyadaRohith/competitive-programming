# 🟠 remove-duplicate-letters — Remove Duplicate Letters

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-duplicate-letters/) &nbsp;|&nbsp; **Solved:** 2026-07-19

---

## 📝 Summary

Given a string, remove duplicate letters such that no letter appears more than once and the resulting string is lexicographically smallest.

## 🔍 Key Observation

Use a stack to build the result string while maintaining a set of visited characters to ensure no duplicates.

## ⚙️ Algorithm

Iterate through the string, pushing characters onto the stack if they are not already in the stack and are lexicographically smaller than the top of the stack. Use a dictionary to track the last occurrence of each character. Pop characters from the stack when a smaller character is found that is still needed later in the string.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the string, as each character is pushed and popped from the stack at most once.` | `O(n) for the stack and the set of visited characters, as they can grow up to the length of the string.` |

## 🏷️ Tags

`stack` `string` `greedy`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last = {}
        visited = set([])
        for i in range(len(s)):
            last[s[i]] = i
        for i in range(len(s)):
            if s[i] in visited:
                continue
            while stack and stack[-1] > s[i] and last[stack[-1]] >i:
                visited.remove(stack[-1])
                stack.pop()
            if s[i] not in stack:
                stack.append(s[i])
                visited.add(s[i])
        return ''.join(stack)
```

</details>
