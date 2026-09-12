# 🟠 check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence — Check If a Word Occurs As a Prefix of Any Word in a Sentence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/) &nbsp;|&nbsp; **Solved:** 2025-10-12

---

## 📝 Summary

Determine if a given word is a prefix of any word in a sentence.

## 🔍 Key Observation

Splitting the sentence into words and checking each word for a prefix match.

## ⚙️ Algorithm

The solution splits the input sentence into words and iterates through them. For each word, it checks if the word starts with the given search word using the `startswith` method. If a match is found, it returns the index of the word in the sentence (adjusted for 1-based indexing). If no match is found after checking all words, it returns -1.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the total number of characters in the sentence, as each word is checked for a prefix.` | `O(1) auxiliary space, as the solution uses a fixed amount of extra space regardless of the input size.` |

## 🏷️ Tags

`string` `splitting` `prefix` `search`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        w=sentence.split()
        for i,j in enumerate(w):
            if j.startswith(searchWord):
                return i+1
        return -1

```

</details>
