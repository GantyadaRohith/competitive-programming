# 🟠 rotate-string — Rotate String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rotate-string/) &nbsp;|&nbsp; **Solved:** 2025-10-12

---

## 📝 Summary

Determine if one string can be rotated to match another string.

## 🔍 Key Observation

Concatenating the original string with itself reveals all possible rotations.

## ⚙️ Algorithm

Check if the goal string is a substring of the concatenated string of s and s.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to substring search.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`string` `rotation` `substring`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        return goal in s+s
```

</details>
