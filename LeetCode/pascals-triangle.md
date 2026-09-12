# 🟠 pascals-triangle — Pascal's Triangle

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/pascals-triangle/) &nbsp;|&nbsp; **Solved:** 2026-08-09

---

## 📝 Summary

Generate Pascal's Triangle up to the nth row.

## 🔍 Key Observation

The triangle is constructed by summing the two numbers directly above each element.

## ⚙️ Algorithm

1. Initialize the first two rows of the triangle.
2. For each subsequent row, start and end with 1.
3. For each element in the middle of the row, sum the two elements directly above it from the previous row.
4. Append the row to the triangle.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to nested loops iterating over rows and elements.` | `O(n^2) for storing the triangle.` |

## 🏷️ Tags

`python` `triangle` `math`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        elif n == 2:
            return [[1],[1,1]]
        else:
            a = [[1],[1,1]]
            n-=2
            for i in range(1,n+1):
                a.append([1])
                for j in range(1,len(a[-2])):
                    a[-1].append(a[-2][j-1]+a[-2][j])
                a[-1].append(1)
            return a

        
```

</details>
