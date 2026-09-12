# 🟠 median-of-two-sorted-arrays — Median of Two Sorted Arrays

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/) &nbsp;|&nbsp; **Solved:** 2026-07-02

---

## 📝 Summary

Find the median of two sorted arrays without merging them.

## 🔍 Key Observation

Use two pointers to merge the arrays in sorted order.

## ⚙️ Algorithm

1. Initialize two pointers i and j for nums1 and nums2, and a pointer k for the output array out.
2. Iterate through both arrays, comparing elements and appending the smaller one to out.
3. After one array is exhausted, append the remaining elements of the other array to out.
4. Calculate the median based on the length of out.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n + m) where n and m are the lengths of nums1 and nums2.` | `O(n + m) for the output array out.` |

## 🏷️ Tags

`merge` `two pointers` `sorted arrays` `median`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        k = 0
        x = len(nums1)+len(nums2)
        out = [0]*x
        while i < len(nums1) and j < len(nums2) :
            if nums1[i] < nums2[j]:
                out[k] = nums1[i]
                i+=1
            else:
                out[k] = nums2[j]
                j+=1
            k+=1
        while i < len(nums1):
            out[k] = nums1[i]
            i+=1
            k+=1
        while j < len(nums2):
            out[k] = nums2[j]
            j+=1
            k+=1
        median = 0
        if x % 2 == 0:
            median = (out[x//2]+out[(x//2)-1])/2
        else:
            median = out[(x-1)//2]
        return float(median)

```

</details>
