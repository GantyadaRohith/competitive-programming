# 🟠 length-of-last-word — Length of Last Word

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/length-of-last-word/) &nbsp;|&nbsp; **Solved:** 2026-02-25

---

## 📝 Summary

Given a string, return the length of the last word.

## 🔍 Key Observation

The solution uses `strip()` to remove leading and trailing spaces and `split(' ')` to split the string into words, allowing easy access to the last word.

## ⚙️ Algorithm

1. Strip the input string to remove any leading or trailing spaces.
2. Split the string into a list of words using space as the delimiter.
3. Return the length of the last word in the list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the strip and split operations.` | `O(n) for the list of words.` |

## 🏷️ Tags

`easy` `string` `split` `strip`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.strip().split(' ')
        return len(x[-1])
```

</details>
