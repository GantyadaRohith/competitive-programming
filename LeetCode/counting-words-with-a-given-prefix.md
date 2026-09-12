# 🟠 counting-words-with-a-given-prefix — Counting Words With a Given Prefix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/counting-words-with-a-given-prefix/) &nbsp;|&nbsp; **Solved:** 2025-10-12

---

## 📝 Summary

Given a list of words and a prefix, count how many words start with the given prefix.

## 🔍 Key Observation

The solution uses the `startswith` method to efficiently check if each word begins with the prefix.

## ⚙️ Algorithm

The algorithm iterates over each word in the list and uses the `startswith` method to determine if the word starts with the given prefix. If it does, the counter `c` is incremented.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) time complexity, where n is the total number of words in the list, as each word is checked once.` | `O(1) auxiliary space, as only a constant amount of extra space is used.` |

## 🏷️ Tags

`python` `string` `startswith` `counting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        for i in words:
            if i.startswith(pref):
                c+=1
        return c
```

</details>
