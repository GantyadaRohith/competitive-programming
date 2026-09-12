# 🟠 search-insert-position — Search Insert Position

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/search-insert-position/) &nbsp;|&nbsp; **Solved:** 2025-12-10

---

## 📝 Summary

Given a sorted array of integers and a target value, find the index where the target should be inserted to maintain sorted order.

## 🔍 Key Observation

Use binary search to efficiently find the insertion point.

## ⚙️ Algorithm

1. Initialize two pointers, `l` and `r`, to the start and end of the array, respectively.
2. While `l` is less than `r`:
   - Calculate the middle index `mid`.
   - If the element at `mid` is equal to the target, set `f` to True and return `mid`.
   - If the target is greater than the element at `mid`, move the left pointer `l` to `mid + 1`.
   - Otherwise, move the right pointer `r` to `mid`.
3. If `f` is False, return `l` as the insertion point.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) due to binary search.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary` `search` `lowercase`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def searchInsert(self, n: List[int], t: int) -> int:
        l,r = 0,len(n)
        f = False
        while l<r:
            mid = (l+r)//2
            if n[mid] == t:
                f = True
                return mid
            elif t>n[mid]:
                l=mid+1
            else:
                r=mid
        return l
```

</details>
