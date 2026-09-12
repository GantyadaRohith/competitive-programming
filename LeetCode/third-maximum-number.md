# 🟠 third-maximum-number — Third Maximum Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/third-maximum-number/) &nbsp;|&nbsp; **Solved:** 2026-08-09

---

## 📝 Summary

Find the third maximum number in an array, returning the maximum if it doesn't exist.

## 🔍 Key Observation

Using a set to remove duplicates and then sorting the list helps in easily finding the third maximum.

## ⚙️ Algorithm

1. Convert the list to a set to remove duplicates.
2. Convert the set back to a list and sort it.
3. Check the length of the sorted list.
4. If the length is less than or equal to 2, return the maximum value from the original list.
5. Otherwise, return the third last element of the sorted list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(n) auxiliary space.` |

## 🏷️ Tags

`python` `set` `sort` `third maximum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        s = list(s)
        s.sort()
        print(s)
        print(len(s))
        if len(s)<=2:
            return max(nums)
        else:
            return s[-3]
        
```

</details>
