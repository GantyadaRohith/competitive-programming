# 🟠 number-of-digit-one — Number of Digit One

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-digit-one/) &nbsp;|&nbsp; **Solved:** 2025-12-15

---

## 📝 Summary

Count the number of times the digit '1' appears in all numbers less than or equal to n.

## 🔍 Key Observation

The problem can be solved by breaking it down into counting '1's contributed by the most significant digit and the lower digits.

## ⚙️ Algorithm

1. Convert the number to a string to easily access each digit.
2. Calculate the base value for the most significant digit (msd).
3. Count the '1's contributed by the msd:
   - If msd is 1, add rest + 1 to count all '1's from 1 to rest.
   - Otherwise, add base to count all '1's from 1 to base - 1.
4. Count the '1's in the lower positions by multiplying msd by the number of digits minus one and the base divided by 10.
5. Recursively count '1's in the rest of the number.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) due to the conversion to a string and the recursive calls.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `number` `digit`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        s = str(n)
        digits = len(s)
        base = 10 ** (digits - 1)
        msd = n // base
        rest = n % base

        # Count 1s contributed by the most significant digit
        if msd == 1:
            ones_msd = rest + 1
        else:
            ones_msd = base

        # Count 1s in lower positions
        ones_lower = msd * (digits - 1) * (base // 10)

        # Recursive call
        return ones_msd + ones_lower + self.countDigitOne(rest)
```

</details>
