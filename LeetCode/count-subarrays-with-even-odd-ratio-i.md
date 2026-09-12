# 🟠 count-subarrays-with-even-odd-ratio-i — Count Subarrays With Even Odd Ratio I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/) &nbsp;|&nbsp; **Solved:** 2026-08-02

---

## 📝 Summary

Given an array of integers and two integers a and b, count the number of subarrays where the ratio of odd to even numbers is less than or equal to a/b.

## 🔍 Key Observation

The key insight is to use a two-pointer technique to count valid subarrays efficiently.

## ⚙️ Algorithm

1. Initialize a counter `count` to zero.
2. Iterate over each element in the array using a left pointer `i`.
3. For each `i`, initialize two counters `oc` (odd count) and `ec` (even count) to zero.
4. Use a right pointer `j` to traverse the array starting from `i`.
5. For each `j`, update `oc` and `ec` based on whether the current element is odd or even.
6. If `oc` is greater than zero and the ratio `ec/oc` is less than or equal to `a/b`, increment the `count`.
7. Return the `count`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loops.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`python` `two-pointer` `counting` `subarrays`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        count = 0
        for i in range(len(nums)):
            oc,ec = 0,0
            for j in range(i,len(nums)):
                if nums[j]&1:
                    oc += 1
                else:
                    ec += 1
                if oc > 0 and (ec/oc) <= (a/b):
                    count+=1
        return count
```

</details>
