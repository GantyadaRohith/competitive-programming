# 🟠 longest-substring-without-repeating-characters — Longest Substring Without Repeating Characters

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Find the length of the longest substring without repeating characters in a given string.

## 🔍 Key Observation

Use a sliding window approach with a set to track characters and their indices.

## ⚙️ Algorithm

Initialize two pointers, `left` and `right`, to mark the current window. Use a set to store characters in the current window. As you iterate through the string with `right`, if a character is already in the set, move the `left` pointer to the right until the duplicate character is removed from the set. Update the maximum length of the substring found so far. Continue this process until the end of the string.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n), where n is the length of the string. Each character is processed at most twice (once by `right` and once by `left`).` | `O(min(n, m)), where m is the size of the character set. The set will store at most n characters in the worst case.` |

## 🏷️ Tags

`python` `sliding window` `hash set`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxlen=0
        se=set()
        for i in range(len(s)):
            while s[i] in se:
                se.remove(s[left])
                left+=1
            se.add(s[i])
            maxlen=max(i-left+1,maxlen)
        return maxlen

```

</details>
