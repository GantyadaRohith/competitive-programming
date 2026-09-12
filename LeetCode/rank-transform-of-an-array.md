# 🟠 rank-transform-of-an-array — Rank Transform of an Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rank-transform-of-an-array/) &nbsp;|&nbsp; **Solved:** 2026-07-17

---

## 📝 Summary

Given an array of integers, transform it such that each element is replaced with its rank in the sorted order of the array.

## 🔍 Key Observation

The key insight is to first sort the array and then assign ranks to each unique element based on their sorted order.

## ⚙️ Algorithm

1. Sort the input array to get the sorted order of elements.
2. Create a dictionary to map each unique element to its rank.
3. Iterate through the sorted array and assign ranks to each element based on the dictionary.
4. Replace each element in the original array with its rank.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(n) auxiliary space for the dictionary.` |

## 🏷️ Tags

`sort` `rank` `transform`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(arr)

        rank = {}
        r = 1

        for num in temp:
            if num not in rank:
                rank[num] = r
                r += 1

        for i in range(len(arr)):
            arr[i] = rank[arr[i]]

        return arr
```

</details>
