# 🟠 number-of-1-bits — Number of 1 Bits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-1-bits/) &nbsp;|&nbsp; **Solved:** 2026-08-21

---

## 📝 Summary

The problem asks to count the number of set bits (1s) in the binary representation of a given unsigned integer.

## 🔍 Key Observation

The least significant bit can be checked using a bitwise AND operation with 1 (n & 1), and then the number can be right-shifted (n >>= 1) to examine the next bit.

## ⚙️ Algorithm

**Bit manipulation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`bit manipulation` `easy` `fundamentals`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n!=0:
            if n&1:
                cnt+=1
            n>>=1
        return cnt
        
```

</details>
