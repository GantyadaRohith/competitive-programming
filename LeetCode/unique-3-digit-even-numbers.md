# 🟠 unique-3-digit-even-numbers — Unique 3-Digit Even Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/unique-3-digit-even-numbers/) &nbsp;|&nbsp; **Solved:** 2026-09-11

---

## 📝 Summary

Given a list of digits, find the number of unique 3-digit even numbers that can be formed.

## 🔍 Key Observation

The key insight is to use a set to store unique numbers and iterate through all possible combinations of digits to form valid 3-digit even numbers.

## ⚙️ Algorithm

1. Check if all digits are odd. If so, return 0 since no even numbers can be formed.
2. Initialize an empty set to store unique numbers.
3. Iterate through all possible combinations of three digits (i, j, k) where i, j, and k are distinct.
4. Ensure i is not equal to j, j is not equal to k, and i is not equal to k to avoid duplicate numbers.
5. Ensure the first digit is not zero to form a valid 3-digit number.
6. Ensure the last digit is even to form an even number.
7. Form the number by concatenating digits i, j, and k.
8. Add the number to the set.
9. Return the size of the set as the count of unique 3-digit even numbers.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^3) due to the triple nested loop iterating through all combinations of three digits.` | `O(n^3) in the worst case due to storing all unique numbers in the set.` |

## 🏷️ Tags

`python` `set` `combinations` `3-digit` `even`

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
