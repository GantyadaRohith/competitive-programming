# 🟠 merge-intervals — Merge Intervals

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/merge-intervals/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Given a list of intervals, merge overlapping intervals.

## 🔍 Key Observation

Sort intervals by start time to ensure they are processed in order.

## ⚙️ Algorithm

1. Sort the intervals based on their start time.
2. Initialize an empty list `out` to store merged intervals.
3. Iterate through the sorted intervals:
   - If `out` is not empty and the last interval in `out` overlaps with the current interval, merge them.
   - Otherwise, add the current interval to `out`.
4. Return the merged intervals list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `merge` `intervals`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda person: person[0])
        print(intervals)
        out = []
        i = 0
        while i < (len(intervals)):
            if out and out[-1][1] >= intervals[i][0] :
                k,l = out.pop()
                m,n = intervals[i]
                out.append([min(k,m),max(l,n)])
                i+=1
                print(out)
            else:
                k,l = intervals[i]
                out.append([k,l])
                i+=1
        return out
```

</details>
