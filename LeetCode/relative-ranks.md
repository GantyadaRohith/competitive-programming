# 🟠 relative-ranks — Relative Ranks

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/relative-ranks/) &nbsp;|&nbsp; **Solved:** 2026-08-09

---

## 📝 Summary

Given a list of scores, assign relative ranks to each score based on their positions in a sorted list.

## 🔍 Key Observation

The problem can be solved by sorting the scores in descending order and assigning ranks based on their positions.

## ⚙️ Algorithm

1. Sort the scores in descending order to determine the relative ranks.
2. Use a dictionary to map each score to its corresponding rank.
3. Assign 'Gold Medal', 'Silver Medal', and 'Bronze Medal' to the top three scores.
4. Assign the remaining scores their respective ranks based on their position in the sorted list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to the sorting step.` | `O(n) auxiliary space for the dictionary.` |

## 🏷️ Tags

`sort` `rank` `medal`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = sorted(score,reverse = True)
        a = {}
        g,s,b = 0,0,0
        j = 0
        for i in temp:
            if g == 0:
                a[i] = 'Gold Medal'
                g+=1
                j+=1
            elif s == 0:
                a[i] = 'Silver Medal'
                s+=1
                j+=1
            elif b == 0:
                a[i] = 'Bronze Medal'
                b+=1
                j+=1
            else:
                j+=1
                a[i] = str(j)
        out = []
        for i in score:
            out.append(a[i])
        return out
        
```

</details>
