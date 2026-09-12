# 🟠 add-binary — Add Binary

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/add-binary/) &nbsp;|&nbsp; **Solved:** 2026-08-21

---

## 📝 Summary

Given two binary strings, add them together and return the result as a binary string.

## 🔍 Key Observation

The key insight is to use bitwise operations to simulate the addition of binary numbers.

## ⚙️ Algorithm

1. Convert the binary strings to integers (base 2).
2. Apply bitwise addition logic:
   - Sum without carry: a ^ b
   - Carry: (a & b) << 1
3. Repeat the process until there is no carry left.
4. Convert the result back to a binary string and strip the '0b' prefix.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the binary strings.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary` `bitwise` `addition`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)!=len(b):
            if len(a) < len(b):
                a = '0'*(len(b)-len(a))+a
            else:
                b = '0'*(len(a)-len(b))+b
        def bitwise_add(a: str, b: str) -> str:
            # 1. Convert binary strings to integers (base 2)
            num1 = int(a, 2)
            num2 = int(b, 2)

            # 2. Apply the same bitwise addition logic
            while num2 != 0:
                sum_without_carry = num1 ^ num2
                carry = (num1 & num2) << 1
                num1 = sum_without_carry
                num2 = carry

            # 3. Convert back to binary string and strip the '0b' prefix
            return bin(num1)[2:]
        return bitwise_add(a,b)
```

</details>
