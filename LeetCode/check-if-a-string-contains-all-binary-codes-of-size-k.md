# 🟠 check-if-a-string-contains-all-binary-codes-of-size-k — Check If a String Contains All Binary Codes of Size K

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) &nbsp;|&nbsp; **Solved:** 2026-02-23

---

## 📝 Summary

Given a binary string, determine if it contains all possible binary codes of length k.

## 🔍 Key Observation

The key insight is to use a set to track unique binary codes of length k.

## ⚙️ Algorithm

1. Initialize an empty set `a` to store unique binary codes of length k.
2. Iterate through the string `s` and extract substrings of length `k`.
3. Add each substring to the set `a`.
4. After processing the entire string, check if the size of the set `a` equals 2^k.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the string `s`.` | `O(2^k) due to the set `a` storing all possible binary codes of length k.` |

## 🏷️ Tags

`set` `binary` `substring` `unique`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        a = set()
        for i in range(len(s)-k+1):
            a.add(s[i:i+k])
        if len(a) == 2**k:
            return True
        return False
```

</details>
