# 🟠 sort-integers-by-the-number-of-1-bits — Sort Integers by The Number of 1 Bits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/) &nbsp;|&nbsp; **Solved:** 2026-02-25

---

## 📝 Summary

Sort integers based on the number of 1 bits in their binary representation.

## 🔍 Key Observation

Use the `bin` function to convert integers to binary strings and count the number of '1's.

## ⚙️ Algorithm

Sort the array using a custom key that combines the count of '1's in the binary representation of each integer with the integer itself. This ensures that integers with fewer '1's come first, and in case of a tie, the integers are sorted by their value.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to the sorting operation.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sort` `bit manipulation` `binary`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr ,key = lambda x:(bin(x).count('1'),x))
        return arr
```

</details>
