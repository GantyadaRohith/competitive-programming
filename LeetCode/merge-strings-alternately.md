# 🟠 merge-strings-alternately — Merge Strings Alternately

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/merge-strings-alternately/) &nbsp;|&nbsp; **Solved:** 2025-08-28

---

## 📝 Summary

Merge two strings alternately, appending characters from each string in order.

## 🔍 Key Observation

Use two pointers to iterate through both strings and append characters alternately.

## ⚙️ Algorithm

Initialize two pointers, i and j, to traverse word1 and word2 respectively. Append characters from word1 to ans, then from word2, incrementing the pointers accordingly. After one string is fully traversed, append the remaining characters from the other string.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n), where n is the length of the longer string.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`python` `string` `two pointers`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans =""

        i=0
        j=0

        while i < len(word1) and j<len(word2):
            ans+=word1[i]
            ans+=word2[j]
            i+=1
            j+=1

        if len(word1)<len(word2):
            ans +=word2[len(word1):]
        else:
            ans +=word1[len(word2):]

        return ans
```

</details>
