# 🟠 longest-subarray-with-at-most-k-distinct-prime-factors — Longest Subarray With at Most K Distinct Prime Factors

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-subarray-with-at-most-k-distinct-prime-factors/) &nbsp;|&nbsp; **Solved:** 2026-08-23

---

## 📝 Summary

Find the length of the longest subarray such that the total number of distinct prime factors among all elements in that subarray is at most 'k'.

## 🔍 Key Observation

The problem structure suggests a sliding window approach. We can efficiently track the count of distinct prime factors within the current window using a hash map, expanding the window to the right and shrinking it from the left when the constraint is violated.

## ⚙️ Algorithm

**Sliding Window + Prime Factorization (Trial Division)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N * sqrt(M))` | `O(N * log M)` |

## 🏷️ Tags

`sliding window` `prime factorization` `hash map` `number theory`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        def p_f(n):
            factors = []
            d = 2
            while d*d <= n:
                if n%d == 0:
                    factors.append(d)
                    while n%d == 0:
                        n//=d
                d+=1
            if n > 1:
                factors.append(n)
            return factors
        a = {}
        for i in nums:
            a[i] = p_f(i)
        freq = {}
        dist = 0
        l = ans = 0
        for r in range(len(nums)):
            for x in a[nums[r]]:
                if freq.get(x,0) == 0:
                    dist+=1
                freq[x] = freq.get(x,0) + 1
            while dist > k:
                for p in a[nums[l]]:
                    freq[p]-=1
                    if freq[p] == 0:
                        dist-=1
                l+=1
            ans = max(ans,r-l+1)
        return ans
        
```

</details>
