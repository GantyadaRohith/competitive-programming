# 🟠 rearrange-string-to-avoid-character-pair — Rearrange String to Avoid Character Pair

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/) &nbsp;|&nbsp; **Solved:** 2026-07-18

---

## 📝 Summary

Rearrange a string such that no two consecutive characters are the same.

## 🔍 Key Observation

The solution uses two separate strings to alternate characters.

## ⚙️ Algorithm

The code iterates through the input string and appends characters to two separate strings, `front` and `back`. Characters from the input string are appended to `front` if they are equal to `y`, and to `back` otherwise. Finally, the two strings are concatenated to form the rearranged string.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the input string, as each character is processed once.` | `O(n) for the two separate strings used to store characters.` |

## 🏷️ Tags

`easy` `string` `two pointers`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        front = back = ''
        for ch in s:
            if ch == y:
                front = front+ch
            else:
                back = back+ch
        return front+back
```

</details>
