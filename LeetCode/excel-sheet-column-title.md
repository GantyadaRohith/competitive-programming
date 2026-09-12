# 🟠 excel-sheet-column-title — Excel Sheet Column Title

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/excel-sheet-column-title/) &nbsp;|&nbsp; **Solved:** 2026-08-09

---

## 📝 Summary

Converts a given column number to its corresponding Excel sheet column title.

## 🔍 Key Observation

The solution uses a mapping of numbers to letters to convert the column number to a title.

## ⚙️ Algorithm

The algorithm repeatedly divides the column number by 26, converting the remainder to a letter and prepending it to the result string. This process continues until the column number is reduced to zero.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) due to the division by 26.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `topic` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ch = {
                1: "A",
                2: "B",
                3: "C",
                4: "D",
                5: "E",
                6: "F",
                7: "G",
                8: "H",
                9: "I",
                10: "J",
                11: "K",
                12: "L",
                13: "M",
                14: "N",
                15: "O",
                16: "P",
                17: "Q",
                18: "R",
                19: "S",
                20: "T",
                21: "U",
                22: "V",
                23: "W",
                24: "X",
                25: "Y",
                26: "Z",
            }

        s = ""

        while columnNumber > 0:
            columnNumber -= 1
            s += chr(ord('A') + columnNumber % 26)
            columnNumber //= 26

        return s[::-1]
```

</details>
