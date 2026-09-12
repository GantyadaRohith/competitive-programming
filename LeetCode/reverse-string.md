# 🟠 reverse-string — Reverse String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reverse-string/) &nbsp;|&nbsp; **Solved:** 2025-11-27

---

## 📝 Summary

Reverses a string in place without using extra space.

## 🔍 Key Observation

The solution uses a two-pointer technique to swap characters from the start and end of the string moving towards the center.

## ⚙️ Algorithm

1. Initialize two pointers, `i` at the start (0) and `n-i-1` at the end (length of the string - 1) of the list `s`.
2. Swap the characters at these two pointers.
3. Move the `i` pointer one step to the right and the `n-i-1` pointer one step to the left.
4. Repeat steps 2 and 3 until `i` is no longer less than `n-i-1`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the list.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`python` `two-pointer` `in-place`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(len(s)//2):
            s[i],s[n-i-1] = s[n-i-1],s[i]
        
```

</details>
