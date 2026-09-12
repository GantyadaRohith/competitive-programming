# 🟠 sqrtx — Sqrt(x)

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sqrtx/) &nbsp;|&nbsp; **Solved:** 2026-07-01

---

## 📝 Summary

Find the integer square root of a given non-negative integer.

## 🔍 Key Observation

Use an iterative approach with binary search to efficiently find the square root.

## ⚙️ Algorithm

1. Initialize a guess as half of the number. 2. Set a tolerance for the accuracy of the result. 3. While the difference between the guess and the better guess is greater than the tolerance, update the guess to the average of the guess and the number divided by the guess. 4. Return the integer part of the guess when it is accurate enough.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) due to the binary search.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sqrt` `binary search` `iterative`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def mySqrt(self, number: int) -> int:
        if number == 0:
            return 0

    # Start with an initial guess
        guess = number / 2.0
        tolerance = 1e-10
    
    # Repeatedly improve the guess until it is accurate enough
        while True:
            better_guess = 0.5 * (guess + number / guess)
            if abs(guess - better_guess) < tolerance:
                return int(better_guess)
            guess = better_guess
```

</details>
