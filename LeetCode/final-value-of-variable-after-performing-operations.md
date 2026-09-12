# 🟠 final-value-of-variable-after-performing-operations — Final Value of Variable After Performing Operations

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/) &nbsp;|&nbsp; **Solved:** 2025-11-27

---

## 📝 Summary

Given a list of operations, determine the final value of a variable after performing all operations.

## 🔍 Key Observation

The solution iterates through each operation and updates the variable accordingly.

## ⚙️ Algorithm

The algorithm initializes a variable `x` to 0 and iterates through each operation in the list. It increments `x` for '++X' and 'X++', and decrements `x` for '--X' and 'X--'. Finally, it returns the updated value of `x`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the list of operations.` | `O(1) auxiliary space as only a single variable `x` is used.` |

## 🏷️ Tags

`python` `operations` `variable` `iteration`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if i == '++X' :
                x+=1
            elif i == '--X':
                x-=1
            elif i == 'X++':
                x+=1
            elif i == 'X--':
                x-=1
        return x
```

</details>
