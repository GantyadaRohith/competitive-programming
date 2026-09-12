# 🟠 find-the-largest-almost-missing-integer — Find the Largest Almost Missing Integer

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Accepted solution for Find the Largest Almost Missing Integer on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`hash-map`

<details>
<summary>💻 View solution</summary>

```python
class Solution:

    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = Counter()

        # Iterate through every contiguous subarray of size k
        for i in range(len(nums) - k + 1):
            window = nums[i : i + k]
            # Use set() to count an element at most once per window
            for num in set(window):
                freq[num] += 1

        # Find the maximum element that appeared in exactly one subarray of size k
        ans = -1
        for num, count in freq.items():
            if count == 1:
                ans = max(ans, num)

        return ans
```

</details>
