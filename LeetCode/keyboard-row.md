# 🟠 keyboard-row — Keyboard Row

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/keyboard-row/) &nbsp;|&nbsp; **Solved:** 2026-08-09

---

## 📝 Summary

Given a list of words, return a list of words that can be typed using letters from only one row of the keyboard.

## 🔍 Key Observation

Identify the rows of the keyboard and check if each word can be typed using only one row.

## ⚙️ Algorithm

1. Map each row of the keyboard to a set of characters for quick lookup.
2. For each word, find the row it belongs to using the first character.
3. Check if all characters in the word belong to the same row.
4. Collect words that meet the criteria.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m) where n is the number of words and m is the average length of the words.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`python` `string` `keyboard`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ch = {
            1:'qwertyuiop',
            2:'asdfghjkl',
            3:'zxcvbnm'
        }
        def find(word):
            for i,row in ch.items():
                if word[0].lower() in row:
                    return i
        out = []
        for i in words:
            temp = find(i)
            f = 1
            for j in range(1,len(i)):
                if i[j].lower() not in ch[temp]:
                    f = 0
                    break
            if f:
                out.append(i)
        return out 

```

</details>
