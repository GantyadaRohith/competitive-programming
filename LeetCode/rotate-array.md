# 🟠 rotate-array — Rotate Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rotate-array/) &nbsp;|&nbsp; **Solved:** 2025-11-27

---

## 📝 Summary

Rotate an array of integers to the right by k steps.

## 🔍 Key Observation

The key insight is to use the reverse technique to rotate the array efficiently.

## ⚙️ Algorithm

1. Reverse the entire array.
2. Reverse the first k elements.
3. Reverse the rest of the array.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the three reverse operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`reverse` `array` `rotation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n     # handle large k

        # reverse helper
        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # reverse whole array
        rev(0, n-1)
        # reverse first k
        rev(0, k-1)
        # reverse rest
        rev(k, n-1)

```

</details>
