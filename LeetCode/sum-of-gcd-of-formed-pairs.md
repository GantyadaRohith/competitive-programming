# 🟠 sum-of-gcd-of-formed-pairs — Sum of GCD of Formed Pairs

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/) &nbsp;|&nbsp; **Solved:** 2026-07-17

---

## 📝 Summary

Calculate the sum of the greatest common divisors (GCDs) of all pairs formed by elements in the array.

## 🔍 Key Observation

The key insight is to sort the array and use the fact that the GCD of two numbers is maximized when they are consecutive.

## ⚙️ Algorithm

1. Find the maximum element in the array and replace each element with its GCD with this maximum element. This ensures that the GCDs are maximized for consecutive elements.
2. Sort the array.
3. Calculate the sum of the GCDs of each pair of consecutive elements.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`gcd` `sorting` `pairwise`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def gcdSum(self, A: list[int]) -> int:
        maxi, n = 0, len(A)

        for i in range(n):
            maxi = max(maxi, A[i])
            A[i] = gcd(A[i], maxi)

        A.sort()

        return sum(gcd(A[i], A[~i]) for i in range(n // 2))
```

</details>
