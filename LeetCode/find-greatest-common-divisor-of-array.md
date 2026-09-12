# 🟠 find-greatest-common-divisor-of-array — Find Greatest Common Divisor of Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array/) &nbsp;|&nbsp; **Solved:** 2026-07-18

---

## 📝 Summary

Find the greatest common divisor (GCD) of an array of integers.

## 🔍 Key Observation

The GCD of an array can be found by determining the GCD of the minimum and maximum values in the array.

## ⚙️ Algorithm

1. Identify the maximum and minimum values in the array.
2. Use the Euclidean algorithm to compute the GCD of these two values.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `gcd` `algorithm`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        ma = max(nums)
        mi = min(nums)
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        return gcd(mi,ma) 
```

</details>
