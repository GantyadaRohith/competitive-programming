# 🟠 smallest-subsequence-of-distinct-characters — Smallest Subsequence of Distinct Characters

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/) &nbsp;|&nbsp; **Solved:** 2026-07-19

---

## 📝 Summary

Find the lexicographically smallest subsequence of distinct characters from a given string.

## 🔍 Key Observation

Use a stack to maintain the order of characters and a dictionary to track the last occurrence of each character.

## ⚙️ Algorithm

Iterate through the string, maintaining a stack of characters. For each character, if it's not already in the stack and is lexicographically smaller than the last character in the stack, and the last occurrence of the stack's top character is after the current index, pop the stack. Add the current character to the stack if it's not already in the stack.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n), where n is the length of the string, due to a single pass through the string and a constant-time stack operations.` | `O(n), where n is the length of the string, due to the stack and the dictionary used to track characters.` |

## 🏷️ Tags

`stack` `string` `subsequence` `distinct`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
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
