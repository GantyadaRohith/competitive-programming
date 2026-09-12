# 🟠 di-string-match — DI String Match

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/di-string-match/) &nbsp;|&nbsp; **Solved:** 2025-12-03

---

## 📝 Summary

Given a string of 'I's and 'D's, construct a permutation of numbers from 0 to n such that the permutation is increasing before a 'D' and decreasing after a 'D'.

## 🔍 Key Observation

The key insight is to use two pointers, one starting at 0 and one at n, to fill the permutation array based on the direction of the string.

## ⚙️ Algorithm

1. Initialize two pointers, `x` at 0 and `y` at n. These pointers will represent the current smallest and largest available numbers to place in the permutation array, respectively.
2. Iterate through the string:
   - If the current character is 'I', place `x` in the current position and increment `x`.
   - If the current character is 'D', place `y` in the current position and decrement `y`.
3. After the loop, place `x` in the last position of the array to complete the permutation.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the string and a constant-time operation for each character.` | `O(1) auxiliary space, as we only use a fixed number of extra variables.` |

## 🏷️ Tags

`short` `lowercase` `string` `permutation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        s.split()
        perm = [0]*(len(s)+1)
        x=0
        y = len(s) 
        for i in range(len(s)):
            if s[i] == 'I':
                perm[i] = x
                x+=1
            elif s[i] == 'D':
                perm[i] = y
                y-=1
        perm[len(s)] = x
        return perm
```

</details>
