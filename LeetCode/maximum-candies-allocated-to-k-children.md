# 🟠 maximum-candies-allocated-to-k-children — Maximum Candies Allocated to K Children

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Accepted solution for Maximum Candies Allocated to K Children on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

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
