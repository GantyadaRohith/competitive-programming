# 🟠 longest-subarray-with-at-most-k-distinct-prime-factors — Longest Subarray With at Most K Distinct Prime Factors

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-subarray-with-at-most-k-distinct-prime-factors/) &nbsp;|&nbsp; **Solved:** 2026-08-23

---

## 📝 Summary

Find the longest subarray with at most k distinct prime factors.

## 🔍 Key Observation

Use a sliding window approach to maintain a window of subarrays with at most k distinct prime factors.

## ⚙️ Algorithm

1. Precompute the prime factors for each number in the array.
2. Use a sliding window to expand and contract the window while maintaining the count of distinct prime factors.
3. If the number of distinct prime factors exceeds k, shrink the window from the left until it is valid again.
4. Keep track of the maximum length of valid subarrays.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting and prime factor computation.` | `O(n) auxiliary space for storing prime factors and frequency counts.` |

## 🏷️ Tags

`sliding window` `prime factors` `subarray`

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
