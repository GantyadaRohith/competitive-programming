# 🟠 largest-integer-with-given-digit-sum — Largest Integer With Given Digit Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/largest-integer-with-given-digit-sum/) &nbsp;|&nbsp; **Solved:** 2026-07-26

---

## 📝 Summary

Find the largest integer with a given digit sum.

## 🔍 Key Observation

The solution uses a greedy approach to construct the largest number by always selecting the largest possible digit that does not exceed the remaining digit sum.

## ⚙️ Algorithm

1. Check if the digit sum is greater than 9 times the number of digits. If so, return -1 as it's impossible to construct such a number.
2. If the number is 1, return the digit sum directly.
3. Initialize a string `st` containing digits from 9 to 0 and variables `cst` (remaining digit sum), `res` (result string), and `i` (index for `st`).
4. Use a while loop to construct the result string by appending the largest possible digit from `st` that does not exceed the remaining digit sum.
5. Break the loop when the result string has the required number of digits.
6. Return the result as an integer.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the string `st`.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`greedy` `string` `digit sum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s>9*n:
            return -1
        if n == 1:
            return s
        cst  = s
        res = ''
        st = '9876543210'
        i = 0
        while True:
            if cst>=int(st[i]):
                cst-=int(st[i])
                res+=st[i]
            else:
                i+=1
            if len(res) == n:
                break
        return int(res)
```

</details>
