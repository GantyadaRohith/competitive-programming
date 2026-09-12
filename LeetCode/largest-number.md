# 🟠 largest-number — Largest Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/largest-number/) &nbsp;|&nbsp; **Solved:** 2026-07-26

---

## 📝 Summary

Given a list of non-negative integers, find the largest number that can be formed by concatenating them.

## 🔍 Key Observation

The key insight is to sort the numbers based on a custom comparison that concatenates two numbers and compares the results.

## ⚙️ Algorithm

1. Convert each number in the list to a string.
2. Sort the list of strings using a custom key: concatenate each string with itself and sort based on the result.
3. If the first string in the sorted list is '0', return '0' as the result.
4. Otherwise, join the sorted list of strings to form the largest number.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sort` `string` `concatenation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_strings = [str(num) for num in nums]

        num_strings.sort(key=lambda a: a * 10, reverse=True)
        print(num_strings)
        if num_strings[0] == "0":
            return "0"

        return "".join(num_strings)
```

</details>
