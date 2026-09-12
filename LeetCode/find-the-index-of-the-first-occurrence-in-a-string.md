# 🟠 find-the-index-of-the-first-occurrence-in-a-string — Find the Index of the First Occurrence in a String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) &nbsp;|&nbsp; **Solved:** 2026-07-10

---

## 📝 Summary

Given two strings, find the index of the first occurrence of the second string in the first string.

## 🔍 Key Observation

The solution uses a simple loop to check each substring of the haystack that has the same length as the needle.

## ⚙️ Algorithm

1. Calculate the lengths of the haystack and needle.
2. Iterate through the haystack, checking each substring of length equal to the needle.
3. If a match is found, return the starting index of the match.
4. If no match is found after checking all possible substrings, return -1.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m) due to the nested loop.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`string` `substring` `search`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1
```

</details>
