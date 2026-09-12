# 🟠 longest-common-prefix — Longest Common Prefix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-common-prefix/) &nbsp;|&nbsp; **Solved:** 2026-08-09

---

## 📝 Summary

Find the longest common prefix among an array of strings.

## 🔍 Key Observation

Iterate through each character position and compare it across all strings.

## ⚙️ Algorithm

1. Initialize an empty string `prefix` to store the common prefix.
2. Iterate over each character position in the first string.
3. For each position, extract the substring from the first string up to that position.
4. Compare this substring with the corresponding substring in all other strings.
5. If any substring does not match, return the current `prefix`.
6. If all substrings match, return the `prefix` after the loop.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m) where n is the number of strings and m is the length of the shortest string.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`string` `prefix` `iteration`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        for i in range(len(strs[0])):
            prefix = strs[0][:i+1]

            for s in strs:
                if s[:i+1] != prefix:
                    return strs[0][:i]

        return strs[0]
```

</details>
