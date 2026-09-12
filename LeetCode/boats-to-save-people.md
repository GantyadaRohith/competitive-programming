# 🟠 boats-to-save-people — Boats to Save People

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/boats-to-save-people/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Accepted solution for Boats to Save People on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        cnt = 0
        high = len(people)-1
        for i in range(len(people)-1,-1,-1):
            if people[i]>=limit:
                cnt+=1
            else:
                high = i
                break
        low = 0
        while low <= high:
            if people[low]+people[high] <= limit:
                cnt+=1
                low+=1
                high-=1
            else:
                cnt+=1
                high-=1
        return cnt
```

</details>
