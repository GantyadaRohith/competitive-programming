# 🟠 minimum-number-of-flips-to-make-the-binary-string-alternating — Minimum Number of Flips to Make the Binary String Alternating

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/) &nbsp;|&nbsp; **Solved:** 2026-03-07

---

## 📝 Summary

Given a binary string, find the minimum number of flips required to make it alternating.

## 🔍 Key Observation

The solution uses two alternating patterns and compares them to the original string to find the minimum flips needed.

## ⚙️ Algorithm

1. Concatenate the string with itself to handle edge cases at the boundaries.
2. Create two alternating patterns: one starting with '0' and the other with '1'.
3. Use two pointers to track the current window of length equal to the original string.
4. For each character in the window, compare it with the corresponding characters in the two patterns.
5. Count the number of mismatches for each pattern.
6. Slide the window across the concatenated string, updating the counts and keeping track of the minimum number of flips.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the concatenated string.` | `O(n) for storing the concatenated string and the two patterns.` |

## 🏷️ Tags

`python` `string` `sliding window` `alternating patterns`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minFlips(self, s: str) -> int:
        ss = s+s
        temps_1 = []
        temps_2 = []
        for i in range(len(ss)):
            if i%2 == 0:
                 temps_1.append('0')
                 temps_2.append('1')
            else:
                temps_1.append('1')
                temps_2.append('0')
        temps_1 = ''.join(temps_1)
        temps_2 = ''.join(temps_2)
        l = 0
        diff1 = 0
        diff2 = 0
        ans  = float('inf')
        n = len(s)
        for r in range(len(ss)):
            if ss[r] != temps_1[r]:
                diff1+=1
            if ss[r] != temps_2[r]:
                diff2+=1

            if r-l+1 > n:
                if ss[l] != temps_1[l]:
                    diff1 -= 1
                if ss[l] != temps_2[l]:
                    diff2 -= 1
                l += 1

            if r-l+1 == n:
                ans = min(ans,diff1,diff2)
        return ans
```

</details>
