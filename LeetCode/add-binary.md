# 🟠 add-binary — Add Binary

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/add-binary/) &nbsp;|&nbsp; **Solved:** 2026-08-21

---

## 📝 Summary

The problem asks to add two binary strings, `a` and `b`, and return their sum as a new binary string.

## 🔍 Key Observation

Binary addition can be performed using bitwise operations: XOR calculates the sum without carry, and (AND << 1) calculates the carry to be added in the next step, repeating until no carry is left.

## ⚙️ Algorithm

**Bitwise addition (XOR for sum, AND-shift for carry)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N)` | `O(N)` |

## 🏷️ Tags

`strings` `binary` `bitwise operations` `math`

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
