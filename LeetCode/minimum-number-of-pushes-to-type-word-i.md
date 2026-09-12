# 🟠 minimum-number-of-pushes-to-type-word-i — Minimum Number of Pushes to Type Word I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/) &nbsp;|&nbsp; **Solved:** 2026-07-30

---

## 📝 Summary

Calculate the minimum number of pushes required to type a given word on a standard keyboard layout.

## 🔍 Key Observation

The solution involves categorizing the positions of characters in the word based on their frequency and calculating the total pushes required for each category.

## ⚙️ Algorithm

The algorithm categorizes characters into 4 groups based on their position in the word (1-8, 9-16, 17-24, 25-32). It then calculates the total pushes required for each group, considering the number of characters in each group and their position in the word.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the word, as we iterate through the word once.` | `O(1) auxiliary space, as we only use a few extra variables.` |

## 🏷️ Tags

`short` `lowercase` `topic` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        n = len(word)
        if n<=8:
            return n
        elif n<=16:
            print(n-8)
            print(2*(n-8))
            return 8+2*(n-8)
        elif n<=24:
            return 8+2*8+3*(n-16)
        else:
            return 8+2*8+3*8+4*(n-24)
```

</details>
