# 🟠 hamming-distance — Hamming Distance

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/hamming-distance/) &nbsp;|&nbsp; **Solved:** 2025-12-08

---

## 📝 Summary

Calculate the Hamming distance between two integers.

## 🔍 Key Observation

Use bitwise XOR to find differing bits and count them.

## ⚙️ Algorithm

1. Perform a bitwise XOR operation on the two integers to find differing bits.
2. Use a loop to count the number of 1s in the result of the XOR operation.
3. Each 1 represents a differing bit, so the count gives the Hamming distance.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the loop that counts the bits.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`bitwise` `xor` `counting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c = 0
        a = x^y
        while a>0:
            a = a&(a-1)
            c+=1
        return c
```

</details>
