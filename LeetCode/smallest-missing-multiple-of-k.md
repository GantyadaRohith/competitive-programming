# 🟠 smallest-missing-multiple-of-k — Smallest Missing Multiple of K

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-missing-multiple-of-k/) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

The problem asks for the smallest positive integer multiple of 'k' that is not present in the given list of integers 'nums'.

## 🔍 Key Observation

To find the smallest missing multiple, iterate through positive multiples of 'k' (k*1, k*2, k*3, ...) in increasing order and check if each is present in 'nums' using a hash set for efficient lookups.

## ⚙️ Algorithm

**Iterative Search with Hashing**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N + M)` | `O(N)` |

## 🏷️ Tags

`hash set` `iteration` `mathematics` `ad-hoc`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = 1
        nums = set(nums)
        while True:
            if k*i in nums:
                i+=1
                continue
            else:
                return k*i
```

</details>
