# 🟠 string-to-integer-atoi — String to Integer (atoi)

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/string-to-integer-atoi/) &nbsp;|&nbsp; **Solved:** 2025-11-21

---

## 📝 Summary

Convert a string to an integer, handling optional signs and overflow.

## 🔍 Key Observation

The solution uses a single pass to parse the string, handling signs and overflow conditions.

## ⚙️ Algorithm

1. Strip leading and trailing whitespace from the input string.
2. Check for a sign and adjust the string accordingly.
3. Parse the string to extract digits, building the integer value.
4. Apply the sign to the integer and handle overflow conditions.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the input string.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`atoi` `string` `integer` `overflow`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        x = s.strip()
        if len(x) == 0:
            return 0
        sign = 1
        if x[0] == '-':
            sign = -1
            x=x[1:]
        elif x[0] == '+':
            x = x[1:]
        num = 0
        for i in x:
            if i.isdigit():
                num = num*10 + int(i)
            else:
                break
        if num*sign > 2**31 -1:
            return 2**31 - 1
        elif num*sign < 2**31 * -1:
            return 2**31*-1
        else:
            return num*sign 
            
```

</details>
