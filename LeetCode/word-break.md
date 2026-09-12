# 🟠 word-break — Word Break

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/word-break/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Given a string and a dictionary of words, determine if the string can be segmented into a space-separated sequence of one or more dictionary words.

## 🔍 Key Observation

Use dynamic programming to build a boolean array that indicates whether each prefix of the string can be segmented into dictionary words.

## ⚙️ Algorithm

1. Initialize a boolean array `dp` of size `length+1`, where `dp[i]` is `True` if the substring `s[0:i]` can be segmented into dictionary words. Set `dp[0]` to `True` since an empty string can always be segmented into words (though not necessarily dictionary words). 2. Iterate over each character in the string. For each character, check all possible prefixes up to that character. If a prefix is in the dictionary and the prefix before it is also in the dictionary, set `dp[i]` to `True`. 3. After processing all characters, `dp[length]` will indicate whether the entire string can be segmented into dictionary words.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to nested loops over the string and the dictionary.` | `O(n) auxiliary space for the `dp` array.` |

## 🏷️ Tags

`dp` `string` `word break`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        length = len(s)
        dp = [False]*(length+1)
        dp[0] = [True]
        for i in range(1,length+1):
        	for j in range(i):
        		if dp[j] and s[j:i] in word_set :
        			dp[i] = True
        			break
        return True if dp[length] else False

```

</details>
