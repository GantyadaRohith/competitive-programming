# 🟠 number-of-strings-that-appear-as-substrings-in-word — Number of Strings That Appear as Substrings in Word

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/) &nbsp;|&nbsp; **Solved:** 2026-07-17

---

## 📝 Summary

Given a list of strings and a word, count how many strings in the list are substrings of the word.

## 🔍 Key Observation

The solution checks each string in the list to see if it is a substring of the given word.

## ⚙️ Algorithm

The algorithm iterates over each string in the patterns list and checks if it is a substring of the word using the `in` keyword. If it is, the count is incremented.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m) where n is the number of strings in the patterns list and m is the average length of the strings.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`string` `substring` `count`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        out = 0 
        for i in patterns:
            if i in word:
                out+=1
        return out
```

</details>
