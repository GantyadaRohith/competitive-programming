# 🟠 first-unique-character-in-a-string — First Unique Character in a String

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/) &nbsp;|&nbsp; **Solved:** 2026-07-09

---

## 📝 Summary

Find the first character in a string that appears only once.

## 🔍 Key Observation

Use a dictionary to count character frequencies and then find the first character with a count of one.

## ⚙️ Algorithm

1. Iterate through the string to count the frequency of each character using a dictionary.
2. Iterate through the string again to find the first character with a frequency of one.
3. Return the index of the first unique character or -1 if no unique character is found.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to two passes through the string.` | `O(1) auxiliary space for the dictionary.` |

## 🏷️ Tags

`string` `hashmap` `frequency`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i

        return -1

```

</details>
