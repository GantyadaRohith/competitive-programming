# 🟠 sequential-digits — Sequential Digits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sequential-digits/) &nbsp;|&nbsp; **Solved:** 2026-07-13

---

## 📝 Summary

Find all sequential digits between a given range.

## 🔍 Key Observation

The key insight is to generate all possible sequential digits of increasing length and check if they fall within the given range.

## ⚙️ Algorithm

1. Initialize a string 'x' containing all digits from 1 to 9.
2. Determine the minimum and maximum lengths of sequential digits needed to cover the range.
3. Iterate over the range of lengths from the minimum to the maximum.
4. For each length, generate all possible sequential digits by slicing the string 'x' from the current index to the current index plus the length.
5. Convert each generated digit to an integer and check if it falls within the given range.
6. If it does, add it to the output list.
7. Return the output list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `sequential` `digits`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        x = '123456789'
        i,j = len(str(low)),len(str(high))
        out = []
        k = min(i,j)
        while k <= max(i,j) :
            print(k)
            l = 0
            while l <= len(x)-k:
                if int(x[l:l+k])>=low and int(x[l:l+k]) <= high:
                    out.append(int(x[l:l+k])) 
                l+=1
            k+=1
        return out
```

</details>
