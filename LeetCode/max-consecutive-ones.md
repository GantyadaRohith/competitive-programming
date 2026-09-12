# 🟠 max-consecutive-ones — Max Consecutive Ones

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/) &nbsp;|&nbsp; **Solved:** 2026-02-27

---

## 📝 Summary

Accepted solution for Max Consecutive Ones on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

Direct simulation / brute force

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        tempcnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tempcnt +=1
            else:
                tempcnt = 0
            cnt = max(tempcnt,cnt)
        return cnt
```

</details>
