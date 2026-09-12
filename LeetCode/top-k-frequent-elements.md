# 🟠 top-k-frequent-elements — Top K Frequent Elements

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/) &nbsp;|&nbsp; **Solved:** 2026-07-06

---

## 📝 Summary

Given a list of integers and a positive integer k, return the k most frequent elements.

## 🔍 Key Observation

Use a dictionary to count the frequency of each element and then sort the elements based on their frequency.

## ⚙️ Algorithm

1. Count the frequency of each element in the list using a dictionary.
2. Sort the dictionary items by frequency in descending order.
3. Extract the top k elements from the sorted list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(n) auxiliary space.` |

## 🏷️ Tags

`sort` `hashmap` `frequency`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        out = [];x = 0
        d = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        for val,q in d.items():
            out.append(val)
            x+=1
            if x == k:
                break
        return out
```

</details>
