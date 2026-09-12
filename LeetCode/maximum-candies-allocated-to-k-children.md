# 🟠 maximum-candies-allocated-to-k-children — Maximum Candies Allocated to K Children

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Determine the maximum number of candies each child can receive such that the total number of candies distributed does not exceed k.

## 🔍 Key Observation

Use binary search to find the maximum number of candies each child can receive.

## ⚙️ Algorithm

1. Initialize low and high as 1 and the sum of candies divided by k, respectively.
2. While low is less than or equal to high:
   a. Calculate mid.
   b. Distribute candies to children and count how many children can receive at least mid candies.
   c. If the count is less than k, move high to mid - 1.
   d. Otherwise, move low to mid + 1.
3. Return high as the maximum number of candies each child can receive.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log m) where n is the number of candies and m is the sum of candies divided by k.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary search` `lowercase` `candies` `children`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low,high = 1,sum(candies)//k
        while low<=high:
            mid = low+(high-low)//2
            temp = candies
            cnt = 0
            for i in temp:
                cnt += math.floor(i/mid)
            if cnt<k:
                high = mid -1
            else:
                low = mid+1
        return high
```

</details>
