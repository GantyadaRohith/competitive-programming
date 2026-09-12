# 🟠 assign-cookies — Assign Cookies

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/assign-cookies/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Given two lists, one of children's greed factors and another of cookie sizes, determine how many children can be satisfied with the cookies.

## 🔍 Key Observation

The solution involves sorting both lists and using a two-pointer technique to match each child's greed factor with the smallest available cookie size.

## ⚙️ Algorithm

1. Sort both the greed factors (g) and the cookie sizes (s) in ascending order.
2. Initialize two pointers, i for greed factors and j for cookie sizes, and a counter cnt to track satisfied children.
3. Iterate through both lists simultaneously:
   - If the current cookie size is greater than or equal to the current child's greed factor, increment the counter and move both pointers forward.
   - If the current cookie size is less, move only the cookie size pointer forward.
4. Return the counter cnt, which represents the number of children satisfied.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting both lists.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`greedy` `two-pointer` `sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=0
        j=0
        cnt = 0
        while i<len(g) and j<len(s):
            if s[j] >= g[i]:
                cnt+=1
                i+=1
                j+=1
            else:
                j+=1
        return cnt
```

</details>
