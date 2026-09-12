# 🟠 group-anagrams — Group Anagrams

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/group-anagrams/) &nbsp;|&nbsp; **Solved:** 2026-07-10

---

## 📝 Summary

Given a list of strings, group all anagrams together.

## 🔍 Key Observation

Anagrams can be identified by sorting their characters.

## ⚙️ Algorithm

1. Create a dictionary `out` to store lists of anagrams.
2. Iterate through each string in `strs`.
3. Sort the characters of each string to form a key.
4. Append the original string to the list corresponding to its sorted key in `out`.
5. Return the values of `out` as a list of lists.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m log m) due to sorting each string.` | `O(n * m) for storing the sorted strings.` |

## 🏷️ Tags

`sort` `hashing` `anagrams`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1 and strs[-1] == '':
            return [strs]
        out = defaultdict(list)
        for i in range(len(strs)):
            x = ''.join(sorted(strs[i]))
            out[x].append(strs[i])
        return list(out.values())
```

</details>
