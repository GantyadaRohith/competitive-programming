# 🟠 maximum-length-substring-with-two-occurrences — Maximum Length Substring With Two Occurrences

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Accepted solution for Maximum Length Substring With Two Occurrences on LeetCode.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

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
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        a = {}
        left = 0
        for i in range(len(s)):
            a[s[i]] = a.get(s[i],0)+1
            while a[s[i]]>2:
                a[s[left]]-=1
                left+=1
            l = max(l,i-left+1)
        return l
                
```

</details>
