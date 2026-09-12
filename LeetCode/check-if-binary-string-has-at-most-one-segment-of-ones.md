# 🟠 check-if-binary-string-has-at-most-one-segment-of-ones — Check if Binary String Has at Most One Segment of Ones

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/) &nbsp;|&nbsp; **Solved:** 2026-03-06

---

## 📝 Summary

Determine if a binary string contains at most one segment of ones.

## 🔍 Key Observation

Identify the first occurrence of '1' and check if the next character is also '1'.

## ⚙️ Algorithm

Iterate through the string starting from the second character. If a '1' is found and the previous character is also '1', return False. If the loop completes without finding such a pair, return True.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the string, as we traverse the string once.` | `O(1) auxiliary space, as we only use a few extra variables.` |

## 🏷️ Tags

`python` `string` `iteration`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        for i in range(1,len(s)):
            if s[i] == '1' and s[i-1] == '0':
                return False
        return True

```

</details>
