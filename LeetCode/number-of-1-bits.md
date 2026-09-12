# 🟠 number-of-1-bits — Number of 1 Bits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-1-bits/) &nbsp;|&nbsp; **Solved:** 2026-08-21

---

## 📝 Summary

Count the number of 1 bits in the binary representation of an integer.

## 🔍 Key Observation

Use bitwise operations to count the number of 1 bits efficiently.

## ⚙️ Algorithm

Iterate through each bit of the integer using a while loop. Use the bitwise AND operation to check if the current bit is 1, and increment a counter if it is. Right shift the integer to process the next bit.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(32) due to the fixed number of bits in an integer.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`bitwise` `count` `integer`

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
