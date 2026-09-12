# 🟠 even-number-of-knight-moves — Even Number of Knight Moves

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/even-number-of-knight-moves/) &nbsp;|&nbsp; **Solved:** 2026-07-19

---

## 📝 Summary

Determine if a knight can reach a target position on a chessboard with an even number of moves.

## 🔍 Key Observation

The parity (even or odd) of the sum of the coordinates of the start and target positions determines if an even number of moves is possible.

## ⚙️ Algorithm

The solution checks if the sum of the coordinates of the start and target positions is even. If it is, then an even number of moves is possible; otherwise, it is not.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`even` `knight` `moves` `chess`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        x1,y1 = start
        x2,y2 = target
        if (x1+y1)%2 == 0:
            if (x2+y2)%2 == 0:
                return True
            else:
                return False
        
        else:
            if (x2+y2)%2 != 0:
                return True
            else:
                return False 
```

</details>
