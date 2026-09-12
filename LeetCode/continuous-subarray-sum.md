# 🟠 continuous-subarray-sum — Continuous Subarray Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/continuous-subarray-sum/) &nbsp;|&nbsp; **Solved:** 2026-08-22

---

## 📝 Summary

Accepted solution for Continuous Subarray Sum on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^3) (estimated -- 3 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`untagged`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        pre = [nums[0]]
        for i in range(1,len(nums)):
            pre.append(pre[-1]+nums[i])
        a = defaultdict(list)
        for i in range(len(pre)):
            pre[i] = pre[i]%k
            if pre[i] == 0 and i>=1:
                return True
            a[pre[i]].append(i)
        f = 0
        for i,j in a.items():
            if len(j) >= 2:
                if max(j)-min(j)>=2:
                    f = 1
                    break
        return False if f == 0 else True
               
        
```

</details>
