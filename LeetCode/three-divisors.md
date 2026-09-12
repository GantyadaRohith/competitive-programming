# 🟠 three-divisors — Three Divisors

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/three-divisors/) &nbsp;|&nbsp; **Solved:** 2025-10-12

---

## 📝 Summary

Determine if a number has exactly three divisors.

## 🔍 Key Observation

The number must be a perfect square and have no divisors other than 1 and itself.

## ⚙️ Algorithm

1. Calculate the integer square root of the number and check if it is a perfect square.
2. Iterate from 2 to the square root of the number, checking if the number is divisible by any of these values.
3. If no divisors are found, return True; otherwise, return False.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(sqrt(n)) due to the loop iterating up to the square root of n.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `math` `number-theory`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isThree(self, n: int) -> bool:
        root = int(math.sqrt(n))
        if root * root != n:
            return False
        for i in range(2, int(math.sqrt(root)) + 1):
            if root % i == 0:
                return False
        return root > 1
```

</details>
