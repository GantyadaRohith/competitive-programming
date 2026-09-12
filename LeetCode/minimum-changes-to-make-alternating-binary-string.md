# 🟠 minimum-changes-to-make-alternating-binary-string — Minimum Changes To Make Alternating Binary String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/) &nbsp;|&nbsp; **Solved:** 2026-03-05

---

## 📝 Summary

Given a binary string, find the minimum number of changes required to make it an alternating binary string.

## 🔍 Key Observation

The solution leverages the fact that an alternating binary string can start with either '0' or '1'. By comparing the string to both possible alternating patterns, the minimum changes required can be determined.

## ⚙️ Algorithm

1. Initialize two counters, `op1` and `op2`, to count the number of changes needed for two possible alternating patterns: starting with '0' and starting with '1'.
2. Iterate through the string, comparing each character to the expected character for the current position in the alternating pattern.
3. Increment the respective counter for each mismatch.
4. Return the minimum of the two counters as the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n), where n is the length of the string, as we iterate through the string once.` | `O(1) auxiliary space, as we only use a constant amount of extra space.` |

## 🏷️ Tags

`short` `lowercase` `binary` `string`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minOperations(self, s: str) -> int:
        op1 = 0
        op2 = 0

        for i in range(len(s)):
            if s[i] != ('0' if i % 2 == 0 else '1'):
                op1 += 1
            if s[i] != ('1' if i % 2 == 0 else '0'):
                op2 += 1

        return min(op1, op2)
```

</details>
