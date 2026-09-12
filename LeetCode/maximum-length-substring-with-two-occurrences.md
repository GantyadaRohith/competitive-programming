# 🟠 maximum-length-substring-with-two-occurrences — Maximum Length Substring With Two Occurrences

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Find the maximum length of a substring that contains at most two distinct characters.

## 🔍 Key Observation

Use a sliding window approach to track the characters and their counts.

## ⚙️ Algorithm

Initialize two pointers, `left` and `right`, to mark the current window. Use a dictionary to count occurrences of each character. Expand the window by moving `right` and update the count. If a character count exceeds two, shrink the window from the left until the count is valid again. Update the maximum length of the valid substring.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the string, as each character is processed at most twice.` | `O(1) auxiliary space, as the dictionary will store at most two characters.` |

## 🏷️ Tags

`sliding window` `hash map` `substring`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        a = {}
        left = 0
        for i in range(len(s)):
            a[s[i]] = a.get(s[i],0)+1
            while a[s[i]]>2:
                a[s[left]]-=1
                left+=1
            l = max(l,i-left+1)
        return l
                
```

</details>
