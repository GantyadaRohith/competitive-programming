# 🟠 number-of-unique-xor-triplets-ii — Number of Unique XOR Triplets II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-unique-xor-triplets-ii/) &nbsp;|&nbsp; **Solved:** 2026-07-25

---

## 📝 Summary

Given an array of integers, find the number of unique XOR triplets.

## 🔍 Key Observation

The key insight is to use the properties of XOR to efficiently count unique triplets.

## ⚙️ Algorithm

1. Create a set `a` to store all possible XOR values of pairs of numbers in the array.
2. Create another set `b` to store all possible XOR values of pairs of numbers in the set `a`.
3. The size of set `b` gives the number of unique XOR triplets.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to nested loops.` | `O(n^2) for storing XOR values.` |

## 🏷️ Tags

`xor` `triplets` `set`

<details>
<summary>💻 View solution</summary>

```python
class Solution(object):
    def uniqueXorTriplets(self, nums):
        n=len(nums)
        a=set()
        if n < 3:
            return len(set(nums))
        MAXX = 2048
        m = list(set(nums))
        for i in m:
            for j in m:
                a.add(i^j)
        b=set()
        for i in a:
            for j in m:
                b.add(i^j)
        return len(b)
```

</details>
