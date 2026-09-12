# 🟠 unique-3-digit-even-numbers — Unique 3-Digit Even Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/unique-3-digit-even-numbers/) &nbsp;|&nbsp; **Solved:** 2026-09-11

---

## 📝 Summary

The problem asks to form all possible unique 3-digit even integers by concatenating three distinct digits from a given list, ensuring the first digit is non-zero.

## 🔍 Key Observation

The direct enumeration of all distinct permutations of three digits, followed by filtering based on the 3-digit number criteria (first digit non-zero, last digit even), efficiently generates all valid numbers, with a hash set ensuring uniqueness.

## ⚙️ Algorithm

**Brute-force permutation generation with filtering and hash set for uniqueness.**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^3)` | `O(1)` |

## 🏷️ Tags

`brute force` `permutations` `hash set` `counting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        if all(num % 2 != 0 for num in digits):
            return 0
            
        s = set()
        n = len(digits)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        if digits[i] != 0 and digits[k] % 2 == 0:
                            num = digits[i] * 100 + digits[j] * 10 + digits[k]
                            s.add(num)    
        return len(s)

```

</details>
