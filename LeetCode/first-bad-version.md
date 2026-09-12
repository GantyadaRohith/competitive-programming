# 🟠 first-bad-version — First Bad Version

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/first-bad-version/) &nbsp;|&nbsp; **Solved:** 2025-12-11

---

## 📝 Summary

Given a list of version numbers, find the first version that is bad.

## 🔍 Key Observation

Binary search efficiently narrows down the range of bad versions.

## ⚙️ Algorithm

1. Initialize two pointers, low and high, to the start and end of the version list, respectively.
2. While low is less than high:
   - Calculate the middle index mid.
   - If the middle version is bad, move the high pointer to mid.
   - Otherwise, move the low pointer to mid + 1.
3. Return the low pointer, which points to the first bad version.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) due to binary search.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary search` `lowercase` `leetcode` `first bad version`

<details>
<summary>💻 View solution</summary>

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        while(low<high):
            mid = (low+high)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid+1
        return low
```

</details>
