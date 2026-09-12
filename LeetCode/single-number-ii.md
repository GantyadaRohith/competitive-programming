# 🟠 single-number-ii — Single Number II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/single-number-ii/) &nbsp;|&nbsp; **Solved:** 2026-07-25

---

## 📝 Summary

Given an array of integers where every element appears three times except one, find the single number that appears only once.

## 🔍 Key Observation

The key insight is to use bitwise operations to count the occurrences of each bit position across all numbers.

## ⚙️ Algorithm

1. Initialize a variable `res` to 0. This will hold the result of the bitwise operations.
2. Iterate over each bit position (0 to 31).
3. For each bit position, count how many numbers have that bit set to 1.
4. If the count is not a multiple of 3, set the corresponding bit in `res` to 1.
5. Return `res` as the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the array and the constant number of bit operations.` | `O(1) auxiliary space as we only use a fixed amount of extra space.` |

## 🏷️ Tags

`bitwise` `counting` `single number`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            a[i] = a.get(i,0) + 1
        print(a)
        for i,j in enumerate(a.items()):
            print(i,j)
            if j[1]== 1:
                return j[0]
        
```

</details>
