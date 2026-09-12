# 🟠 valid-anagram — Valid Anagram

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/valid-anagram/) &nbsp;|&nbsp; **Solved:** 2026-07-09

---

## 📝 Summary

Determine if two strings are anagrams of each other.

## 🔍 Key Observation

Anagrams have the same characters with the same frequency.

## ⚙️ Algorithm

1. Check if the lengths of the two strings are equal. If not, they cannot be anagrams.
2. Iterate through each character in the first string.
3. For each character, count its occurrences in both strings.
4. If any character's count in one string does not match the count in the other, return False.
5. If all characters match, return True.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through each string.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `string` `anagram`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
     
        for i in set(s):
           
            if t.count(i)!=s.count(i):
                return False
            if i not in t:
                return False

           
        
       
        return True
```

</details>
