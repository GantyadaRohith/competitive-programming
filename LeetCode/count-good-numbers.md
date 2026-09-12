# 🟠 count-good-numbers — Count Good Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-good-numbers/) &nbsp;|&nbsp; **Solved:** 2026-05-02

---

## 📝 Summary

Count the number of n-digit numbers that are divisible by 2 but not by 5.

## 🔍 Key Observation

The problem can be solved by considering the number of even and odd digits separately.

## ⚙️ Algorithm

1. Calculate the number of even digits (even) and odd digits (odd) in the n-digit number.
2. Calculate the power of 5 for even digits and 4 for odd digits.
3. Multiply the results and take modulo 1000000007 to get the final count.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the power function.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`count` `good` `numbers` `even` `odd` `digits` `modular` `exponentiation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = (n+1)//2
        odd = n//2
        mod = 10**9+7
        def power(a,b):
            res = 1
            a%=mod
            while b>0:
                if b%2 == 1:
                    res = (res*a)%mod
                a = (a*a)%mod
                b//=2
            return res
        p1 = power(5,even)
        p2 = power(4,odd)
        return (p1*p2)%1000000007

```

</details>
