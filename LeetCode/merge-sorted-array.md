# 🟠 merge-sorted-array — Merge Sorted Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/merge-sorted-array/) &nbsp;|&nbsp; **Solved:** 2026-05-17

---

## 📝 Summary

Accepted solution for Merge Sorted Array on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

Direct simulation / brute force

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        j1 = m-1
        j2 = n-1
        k = len(nums1)-1
        while j1 >= 0 and j2 >= 0:
            if nums1[j1] > nums2[j2]:
                nums1[k] = nums1[j1]
                j1 -= 1
            else:
                nums1[k] = nums2[j2]
                j2 -= 1

            k -= 1
        while j2 >= 0:
            nums1[k] = nums2[j2]
            j2 -= 1
            k -= 1
```

</details>
