# 🟠 add-digits — Add Digits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/add-digits/) &nbsp;|&nbsp; **Solved:** 2026-07-22

---

## 📝 Summary

Given a non-negative integer, repeatedly add its digits until a single-digit number is obtained.

## 🔍 Key Observation

The problem can be solved by repeatedly summing the digits of the number until a single-digit number is reached.

## ⚙️ Algorithm

1. If the number has more than one digit, repeatedly sum its digits until a single-digit number is obtained.
2. If the number has only one digit, return the number as it is.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) due to the number of times the digits are summed.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `add-digits` `problem-solving`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) !=1 :
            rem=0
            sum=0
            while num >0:
                rem=num%10
                sum+=rem
                num//=10
            return self.addDigits(sum)
        else:
            return num
```

</details>
