# 🟠 minimum-number-of-days-to-make-m-bouquets — Minimum Number of Days to Make m Bouquets

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) &nbsp;|&nbsp; **Solved:** 2026-02-25

---

## 📝 Summary

Given a list of days flowers bloom and the number of bouquets and flowers per bouquet, find the minimum number of days required to have at least m bouquets.

## 🔍 Key Observation

The problem can be solved using binary search to find the minimum number of days required.

## ⚙️ Algorithm

1. Determine the minimum and maximum bloom days from the list.
2. Use binary search to find the minimum number of days required:
   - Calculate the middle day.
   - Count the number of bouquets that can be made with the middle day as the maximum bloom day.
   - If the number of bouquets is at least m, adjust the upper bound to the middle day minus one.
   - Otherwise, adjust the lower bound to the middle day plus one.
3. Return the lower bound as the minimum number of days required.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log(max(bloomDay) - min(bloomDay))) due to the binary search.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary search` `minimum days` `bouquets`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if(m*k) > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low <= high:
            mx = low + (high-low)//2
            cnt,mi = 0,0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=mx:
                    mi+=1
                else:
                    mi=0
                if mi==k:
                    cnt+=1
                    mi=0
            if cnt>=m:
                high = mx-1
            else:
                low = mx+1
        return low
```

</details>
