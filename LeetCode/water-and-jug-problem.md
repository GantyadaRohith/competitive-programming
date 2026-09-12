# 🟠 water-and-jug-problem — Water and Jug Problem

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/water-and-jug-problem/) &nbsp;|&nbsp; **Solved:** 2026-02-23

---

## 📝 Summary

Determine if it's possible to measure a specific amount of water using two jugs of different capacities.

## 🔍 Key Observation

The problem can be solved using the greatest common divisor (GCD) of the two jug capacities.

## ⚙️ Algorithm

The solution involves checking if the target amount can be expressed as a linear combination of the two jug capacities. This is true if the target is less than or equal to the sum of the jug capacities and if the target is divisible by the GCD of the jug capacities.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log(min(x, y))) due to the GCD calculation.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`math` `gcd` `linear combination`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        if target<=x+y and target%gcd(x,y) == 0:
            return True
        return False
```

</details>
