# 🟠 plus-one — Plus One

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/plus-one/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Given a non-empty array of digits representing a non-negative integer, increment the integer by one and return the result as an array of digits.

## 🔍 Key Observation

The key insight is to convert the list of digits into a number, increment it, and then convert it back to a list of digits.

## ⚙️ Algorithm

1. Convert the list of digits into a string to easily manipulate the number.
2. Convert the string back to an integer and add one.
3. Convert the resulting integer back to a string to iterate over each digit.
4. Convert each character back to an integer and append it to the output list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the conversion and iteration steps.` | `O(n) for storing the string and the output list.` |

## 🏷️ Tags

`easy` `string` `conversion` `math`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for i in digits:
            num += str(i)
        num = int(num)+1
        out = []
        for i in str(num): 
            out.append(int(i))
        return out
        
```

</details>
