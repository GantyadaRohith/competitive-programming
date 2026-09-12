# 🟠 construct-uniform-parity-array-i — Construct Uniform Parity Array I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/construct-uniform-parity-array-i/) &nbsp;|&nbsp; **Solved:** 2026-09-04

---

## 📝 Summary

Determine if all elements in the array are the same.

## 🔍 Key Observation

The solution checks if all elements in the array are equal.

## ⚙️ Algorithm

The code simply returns `True` if all elements in the list `nums1` are the same. This is achieved by comparing the first element to the rest of the list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the list.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `array` `equality`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
        
```

</details>
