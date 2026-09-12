# 🟠 koko-eating-bananas — Koko Eating Bananas

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/koko-eating-bananas/) &nbsp;|&nbsp; **Solved:** 2026-07-06

---

## 📝 Summary

Koko wants to eat all bananas in piles within a given number of hours. Find the minimum eating speed to ensure she can finish all bananas within the time limit.

## 🔍 Key Observation

Binary search on the possible eating speeds.

## ⚙️ Algorithm

1. Initialize low and high bounds for the eating speed. Low is 1 (minimum possible speed), high is the maximum number of bananas in any pile (maximum possible speed).
2. While low is less than high:
   a. Calculate the middle speed (rate).
   b. Calculate the total hours needed to eat all bananas at the current rate.
   c. If the total hours needed is less than or equal to the given hours, update high to rate.
   d. Otherwise, update low to rate + 1.
3. Return low as the minimum eating speed.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log m) where n is the number of piles and m is the maximum number of bananas in any pile.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary search` `eating speed` `bananas`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate = 1
        l = 1
        hi = max(piles)
        while l<hi:
            rate = (hi+l)//2
            H = 0
            for i in piles:
                H += math.ceil(i/rate)
            if H<=h:
                hi = rate
            else:
                l = rate+1
        return l
```

</details>
