# 🟠 jump-game — Jump Game

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/jump-game/) &nbsp;|&nbsp; **Solved:** 2026-07-07

---

## 📝 Summary

Determine if you can reach the last index of the array by jumping from each index.

## 🔍 Key Observation

The solution uses a greedy approach with a table to keep track of reachable indices.

## ⚙️ Algorithm

The algorithm iterates from the second-to-last element to the first. For each element, it calculates the farthest index it can jump to. It then updates a table to mark all indices reachable from the current element. Finally, it checks if the first index is reachable.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array and a constant-time table update.` | `O(1) auxiliary space as the table size is fixed at n.` |

## 🏷️ Tags

`short` `lowercase` `jump` `game`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        table = [False] * n
        table[-1] = True

        for i in range(n-2, -1, -1):
            far = min(i + nums[i], n - 1)
            for j in range(i + 1, far + 1):
                if table[j]:
                    table[i] = True
                    break

        return table[0]
```

</details>
