# 🟠 binary-number-with-alternating-bits — Binary Number with Alternating Bits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/binary-number-with-alternating-bits/) &nbsp;|&nbsp; **Solved:** 2026-07-17

---

## 📝 Summary

Determine if a binary number has alternating bits.

## 🔍 Key Observation

Convert the number to binary and check for alternating bits efficiently.

## ⚙️ Algorithm

Convert the integer to a binary string, iterate through it, and check for alternating bits. If a mismatch is found, return False; otherwise, return True.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the conversion and iteration through the binary string.` | `O(n) for storing the binary string.` |

## 🏷️ Tags

`binary` `bitwise` `conversion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)[2:]
        cnt = 0
        for i in s:
            if cnt!=1 and i == '1':
                cnt +=1
            elif cnt == 1 and i == '1':
                return False
            elif cnt!=0 and i == '0':
                cnt-=1
            elif cnt == 0 and i == '0':
                return False
        return True
```

</details>
