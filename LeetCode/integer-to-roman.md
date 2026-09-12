# 🟠 integer-to-roman — Integer to Roman

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/integer-to-roman/) &nbsp;|&nbsp; **Solved:** 2025-12-10

---

## 📝 Summary

Convert an integer to its Roman numeral representation.

## 🔍 Key Observation

Use a dictionary to map integers to their corresponding Roman numeral symbols and iterate through the dictionary to construct the Roman numeral.

## ⚙️ Algorithm

1. Define a dictionary `dit` that maps integers to their Roman numeral symbols.
2. Initialize an empty string `s` to build the Roman numeral.
3. Create a list `x` of integers representing the Roman numeral symbols in descending order.
4. Use a while loop to iterate through `x`:
   - If the current integer `x[i]` is less than or equal to the remaining number `num`, append the corresponding Roman numeral to `s` and subtract `x[i]` from `num`.
   - Otherwise, increment `i` to move to the next integer in `x`.
5. Return the constructed Roman numeral string `s`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the list `x`.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `integer` `roman`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        dit = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        s=''
        x = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        i=0
        while num and i<=len(x):
            if num >= x[i] :
                s+=dit[x[i]]
                num -= x[i]
            else:
                i+=1
        return s

```

</details>
