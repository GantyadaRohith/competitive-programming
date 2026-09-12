# 🟠 minimum-window-substring — Minimum Window Substring

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-window-substring/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Find the smallest substring in `s` that contains all characters of `t`.

## 🔍 Key Observation

Use a sliding window to track characters in `s` and ensure they match those in `t`.

## ⚙️ Algorithm

1. Initialize a dictionary `dic` to count characters in `t`, and `win` to track characters in the current window of `s`. Set `req` to the number of unique characters in `t`, `formed` to count matched characters, and `left` to the start of the window. Initialize `minlen` to infinity and `start` to 0.

2. Iterate through `s` with a right pointer `r`. For each character, update `win` and check if it matches `dic`. If it does, increment `formed`.

3. When `formed` equals `req`, it means the current window contains all characters of `t`. Update `minlen` and `start` if the current window is smaller.

4. Move the left pointer `left` to the right to shrink the window while ensuring the window still contains all characters of `t`. Decrement `win` and `formed` as needed.

5. Return the minimum window substring or an empty string if no such window exists.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m + n) where m is the length of `s` and n is the length of `t`.` | `O(1) auxiliary space for the `dic` and `win` dictionaries.` |

## 🏷️ Tags

`sliding window` `hash map` `substring`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m=len(s)
        n=len(t)
        if m<n:
            return ""
        dic={}
        for c in t:
            dic[c]=dic.get(c,0)+1
        req=len(dic)
        formed=0
        left=0
        win={}
        start=0
        minlen=float('inf')
        for r in range(len(s)):
            win[s[r]] = win.get(s[r], 0) + 1
            if s[r] in dic and win[s[r]]==dic[s[r]]:
                formed+=1
            while formed==req:
                if r-left+1<minlen:
                    minlen=r-left+1
                    start=left
                win[s[left]]-=1
                if s[left] in dic and win[s[left]] <dic[s[left]] :
                    formed-=1
                left+=1
        return "" if minlen==float('inf') else s[start:start+minlen]
```

</details>
