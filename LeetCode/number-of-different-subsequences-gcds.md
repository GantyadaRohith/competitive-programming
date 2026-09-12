# 🟠 number-of-different-subsequences-gcds — Number of Different Subsequences GCDs

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-different-subsequences-gcds/) &nbsp;|&nbsp; **Solved:** 2026-02-23

---

## 📝 Summary

Given a list of integers, find the number of unique GCDs of all possible non-empty subsequences.

## 🔍 Key Observation

The key insight is to iterate over all possible GCDs and check if they can be formed by any subsequence.

## ⚙️ Algorithm

1. Convert the list to a set for O(1) lookups.
2. Iterate over all possible GCDs from 1 to the maximum number in the list.
3. For each GCD, check if it can be formed by any subsequence by iterating over multiples of the GCD.
4. If a multiple is in the set, update the GCD and check if it becomes 1.
5. If the GCD becomes 1, increment the answer count.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting and the gcd function.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`medium` `math` `gcd` `subsequences`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        s = set(nums)
        maxnum = max(nums)
        ans = 0

        for g in range(1, maxnum + 1):
            cur_gcd = 0
            for multiple in range(g, maxnum + 1, g):
                if multiple in s:
                    cur_gcd = math.gcd(cur_gcd, multiple // g)
                    if cur_gcd == 1:
                        ans += 1
                        break

        return ans
```

</details>
