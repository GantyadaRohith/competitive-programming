# 🟠 the-kth-factor-of-n — The kth Factor of n

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/the-kth-factor-of-n/) &nbsp;|&nbsp; **Solved:** 2025-10-12

---

## 📝 Summary

Find the kth factor of a given number n.

## 🔍 Key Observation

Iterate through all numbers from 1 to n and count factors.

## ⚙️ Algorithm

1. Initialize a counter `count` to 0.
2. Loop through numbers from 1 to n.
3. For each number `i`, check if `n % i == 0` (i.e., `i` is a factor of `n`).
4. If `i` is a factor, increment the `count`.
5. If `count` equals `k`, return `i` as the kth factor.
6. If the loop completes without finding the kth factor, return -1.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the loop iterating through all numbers from 1 to n.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `math` `factorization`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i
        return -1    
```

</details>
