# 🟠 squares-of-a-sorted-array — Squares of a Sorted Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/) &nbsp;|&nbsp; **Solved:** 2026-05-17

---

## 📝 Summary

Given a sorted array of integers, return an array containing the squares of the numbers in non-decreasing order.

## 🔍 Key Observation

The key insight is to use two pointers to traverse the array from both ends, comparing the absolute values of the elements and placing the larger square at the end of the result array.

## ⚙️ Algorithm

1. Initialize two pointers, `i` at the start and `j` at the end of the input array, and a result array `sqr` of the same length initialized to -1.
2. Use a while loop to traverse the array from both ends towards the center:
   - If the absolute value of the element at `i` is less than the absolute value of the element at `j`, place the square of `nums[j]` at the current position in `sqr` and decrement `j` and `k`.
   - Otherwise, place the square of `nums[i]` at the current position in `sqr` and increment `i` and `k`.
3. Return the result array `sqr`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `sort` `squares`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        k = len(nums)-1
        sqr = [-1]*(len(nums))
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                sqr[k] = nums[j]*nums[j]
                j-=1
                k-=1
            else:
                sqr[k] = nums[i]*nums[i]
                i+=1
                k-=1
        return sqr
```

</details>
