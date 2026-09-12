# 🟠 happy-number — Happy Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/happy-number/) &nbsp;|&nbsp; **Solved:** 2026-08-21

---

## 📝 Summary

Determine if a number is a happy number by repeatedly replacing it with the sum of the squares of its digits until it either becomes 1 (indicating a happy number) or enters a cycle that does not include 1.

## 🔍 Key Observation

The key insight is that a happy number will eventually reach 1 or enter a cycle that does not include 1.

## ⚙️ Algorithm

1. If the number is less than 9 and either 1 or 7, return True as these are happy numbers. 2. Otherwise, repeatedly replace the number with the sum of the squares of its digits until the number becomes 1 or enters a cycle that does not include 1. 3. If the number becomes 1, return True; otherwise, return False.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) due to the number of digits in the number.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`happy number` `digit manipulation` `cycle detection`

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
