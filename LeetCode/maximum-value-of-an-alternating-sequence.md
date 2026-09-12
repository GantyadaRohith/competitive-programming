# 🟠 maximum-value-of-an-alternating-sequence — Maximum Value of an Alternating Sequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/) &nbsp;|&nbsp; **Solved:** 2026-07-18

---

## 📝 Summary

Given a sequence of numbers, find the maximum value of an alternating sequence.

## 🔍 Key Observation

The solution involves calculating the maximum value of an alternating sequence by considering the number of peaks and the difference between consecutive elements.

## ⚙️ Algorithm

1. If the sequence length is 1, return the first element as the maximum value.
2. Calculate the number of peaks in the sequence.
3. The maximum value of the alternating sequence is the sum of the first element and the difference between consecutive elements multiplied by the number of peaks minus one.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `problem` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s
        no_of_peaks = n//2
        return (s+m) + (no_of_peaks-1)*(m-1)
```

</details>
