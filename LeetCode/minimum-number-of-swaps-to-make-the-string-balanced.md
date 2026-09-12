# 🟠 minimum-number-of-swaps-to-make-the-string-balanced — Minimum Number of Swaps to Make the String Balanced

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/) &nbsp;|&nbsp; **Solved:** 2025-11-27

---

## 📝 Summary

Given a string of '[' and ']' characters, determine the minimum number of swaps needed to make the string balanced.

## 🔍 Key Observation

The problem can be solved by counting the number of unmatched '[' characters and then calculating the minimum swaps required to balance the string.

## ⚙️ Algorithm

1. Initialize two counters: `b` for unmatched '[' characters and `ib` for unmatched ']' characters.
2. Iterate through the string, incrementing `b` for '[' and decrementing `b` for ']'.
3. If `b` becomes negative, it means there is an unmatched ']' character, so increment `ib`.
4. The minimum swaps needed is `(ib + 1) // 2`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the string.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `string` `balance`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minSwaps(self, s: str) -> int:
        b = 0
        ib = 0
        st = list(s)
        for i in st:
            if i == '[':
                b+=1
            else:
                if b > 0:
                    b-=1
                else:
                    ib+=1
        return (ib+1)//2
```

</details>
