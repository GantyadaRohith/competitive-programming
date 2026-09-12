# 🟠 h-index — H-Index

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/h-index/) &nbsp;|&nbsp; **Solved:** 2025-07-03

---

## 📝 Summary

Given a list of citations for a researcher's papers, determine the researcher's h-index.

## 🔍 Key Observation

The h-index is the largest number h such that the researcher has at least h papers with at least h citations each.

## ⚙️ Algorithm

1. Sort the citations in descending order.
2. Initialize h to 0.
3. Iterate through the sorted list:
   - If the current citation is greater than or equal to h + 1, increment h.
   - If the current citation is less than h + 1, break the loop.
4. Return h.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `h-index` `sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i in range(0,len(citations)):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
        return h
```

</details>
