# 🟠 unique-morse-code-words — Unique Morse Code Words

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/unique-morse-code-words/) &nbsp;|&nbsp; **Solved:** 2025-12-03

---

## 📝 Summary

Given a list of words, convert each word to its Morse code representation and count the number of unique Morse code words.

## 🔍 Key Observation

The solution uses a mapping from letters to Morse code and a set to track unique Morse code representations.

## ⚙️ Algorithm

1. Create a mapping of each letter to its Morse code representation using a list of Morse codes.
2. Iterate over each word in the input list.
3. Convert each word to its Morse code representation by mapping each letter to its Morse code and concatenating the results.
4. Use a set to store the unique Morse code representations.
5. Return the size of the set as the number of unique Morse code words.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m) where n is the number of words and m is the average length of the words.` | `O(n * m) due to storing the Morse code representations in a set.` |

## 🏷️ Tags

`python` `string` `hashing`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        values = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."] 
        mapping = {chr(97+i): values[i] for i in range(26)}
        out = []
        for word in words:
            s = ''
            for ch in word:
                s = s + mapping[ch]
            out.append(s)
        return len(set(out))

```

</details>
