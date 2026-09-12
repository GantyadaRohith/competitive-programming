# 🟠 jump-game-ii — Jump Game II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/jump-game-ii/) &nbsp;|&nbsp; **Solved:** 2026-02-26

---

## 📝 Summary

Given an array of non-negative integers representing the maximum jump length at each position, find the minimum number of jumps required to reach the last index.

## 🔍 Key Observation

The key insight is to use a greedy approach to always jump to the farthest reachable position from the current position.

## ⚙️ Algorithm

1. Initialize `jump` to count the number of jumps, `curend` to the current end of the reachable range, and `far` to track the farthest position that can be reached from the current position.
2. Iterate through the array, updating `far` to be the maximum of its current value and `i + nums[i]`.
3. If the current position `i` equals `curend`, increment the jump count and update `curend` to `far`.
4. Return the jump count.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `jump` `game`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        curend = 0
        far = 0
        for i in range(len(nums)-1):
            far = max(far,i+nums[i])
            if(i==curend):
                jump+=1
                curend = far
        return jump
```

</details>
