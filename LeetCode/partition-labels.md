# 🟠 partition-labels — Partition Labels

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/partition-labels/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Given a string, partition it into the minimum number of substrings such that each substring contains unique characters.

## 🔍 Key Observation

The key insight is to use a dictionary to track the last occurrence of each character and then merge overlapping intervals of these characters.

## ⚙️ Algorithm

1. Build a dictionary to store the first and last occurrence of each character in the string.
2. Sort the intervals based on their starting index.
3. Merge overlapping intervals.
4. Calculate the length of each merged interval and return the lengths as a list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting the intervals.` | `O(n) auxiliary space for storing character intervals.` |

## 🏷️ Tags

`short` `lowercase` `string` `partitioning`

<details>
<summary>💻 View solution</summary>

```python
from collections import defaultdict
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}

        # Build [first, last] interval for each character
        for i, ch in enumerate(s):
            if ch not in intervals:
                intervals[ch] = [i, i]
            else:
                intervals[ch][1] = i

        # Sort intervals by their starting index
        intervals = sorted(intervals.values(), key=lambda x: x[0])

        merged = []

        # Merge overlapping intervals
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        # Convert merged intervals to partition lengths
        return [end - start + 1 for start, end in merged]
```

</details>
