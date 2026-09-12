# 🟠 happy-number — Happy Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/happy-number/) &nbsp;|&nbsp; **Solved:** 2026-08-21

---

## 📝 Summary

The problem asks to determine if a positive integer is a 'happy number', where a happy number is defined by an iterative process of replacing it with the sum of the squares of its digits, eventually reaching 1. If the process enters a cycle that does not include 1, the number is not happy.

## 🔍 Key Observation

All numbers, when repeatedly transformed by summing squares of their digits, will eventually either reach 1 (making them happy) or enter a specific cycle of numbers that does not include 1. The solution exploits the property that a number is happy if and only if this process eventually yields 1 or 7 as a single-digit result, otherwise it yields one of the other single digits (2,3,4,5,6,8,9) which are part of the non-happy cycle.

## ⚙️ Algorithm

**Iterative digit sum of squares. The algorithm repeatedly calculates the sum of squares of digits until the number becomes a single digit. It then checks if this single digit is 1 or 7, which are the terminal happy single digits, otherwise the number is considered unhappy.**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n)` | `O(log n)` |

## 🏷️ Tags

`number theory` `digit manipulation` `mathematics` `simulation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        if n<9 and (n ==1 or n == 7):
            return True
        else:
            while len(str(n))!=1:
                count = 0
                for i in str(n):
                    count+=(int(i)**2)
                n = count
            if n<9 and (n ==1 or n == 7):
                return True
            else:
                return False
        
```

</details>
