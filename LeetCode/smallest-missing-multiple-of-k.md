# 🟠 smallest-missing-multiple-of-k — Smallest Missing Multiple of K

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-missing-multiple-of-k/) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

Find the smallest positive integer that is not a multiple of K and is not present in the given list of numbers.

## 🔍 Key Observation

The solution uses a set to efficiently check for the presence of multiples of K.

## ⚙️ Algorithm

1. Initialize a variable `i` to 1.
2. Convert the list `nums` to a set for O(1) average time complexity lookups.
3. Use a while loop to find the smallest missing multiple of K:
   - Check if `k*i` is in the set of numbers.
   - If it is, increment `i` and continue.
   - If it is not, return `k*i` as the smallest missing multiple.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the set operations and the while loop.` | `O(n) for the set used to store the numbers.` |

## 🏷️ Tags

`python` `set` `multiple` `k`

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
