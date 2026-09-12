# 🟠 non-overlapping-intervals — Non-overlapping Intervals

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/non-overlapping-intervals/) &nbsp;|&nbsp; **Solved:** 2026-02-26

---

## 📝 Summary

Given a list of intervals, find the minimum number of intervals to remove to ensure no two intervals overlap.

## 🔍 Key Observation

The key insight is to sort intervals by their end times and then greedily select the interval that ends the earliest.

## ⚙️ Algorithm

1. Sort the intervals by their end times.
2. Initialize `end` to negative infinity and `cnt` to 0.
3. Iterate through each interval:
   - If the start of the current interval is greater than or equal to `end`, increment `cnt` and update `end` to the end of the current interval.
4. Return the total number of intervals minus `cnt`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `sort` `greedy`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        end = -inf
        cnt = 0

        for s,e in intervals:
            if s>=end:
                cnt+=1
                end = e
        return len(intervals)-cnt
```

</details>
