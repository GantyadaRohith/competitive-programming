# 🟠 sum-of-integers-with-maximum-digit-range — Sum of Integers with Maximum Digit Range

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/) &nbsp;|&nbsp; **Solved:** 2026-07-18

---

## 📝 Summary

Given a list of integers, find the sum of all integers whose digit range (difference between the maximum and minimum digits) matches the maximum digit range of any integer in the list.

## 🔍 Key Observation

The key insight is to first determine the maximum digit range of any integer in the list and then sum all integers whose digit range matches this maximum.

## ⚙️ Algorithm

1. Initialize variables `out` to store the result, `maxi` to track the maximum digit range, and `ans` to store the sum of integers with the maximum digit range.
2. Iterate through each number in the list, convert it to a list of digits, and calculate the digit range.
3. Update `maxi` if the current digit range is greater than the previously recorded maximum.
4. Iterate through the list again, calculate the digit range for each number, and check if it matches `maxi`.
5. If it matches, add the number to `ans`.
6. Return `ans`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting within the digit range calculation.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`python` `digit` `range` `sum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        out = []
        maxi = 0
        ans = 0
        for num in nums:
            digits = [int(d) for d in str(num)]
            ma = max(digits)
            mi = min(digits)
            maxi = max(maxi,ma-mi)
        for num in nums:
            digits = [int(d) for d in str(num)]
            ma = max(digits)
            mi = min(digits)
            if ma-mi == maxi:
                ans+=num
        return ans
```

</details>
