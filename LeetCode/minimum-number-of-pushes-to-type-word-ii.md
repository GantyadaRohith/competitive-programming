# 🟠 minimum-number-of-pushes-to-type-word-ii — Minimum Number of Pushes to Type Word II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/) &nbsp;|&nbsp; **Solved:** 2026-08-02

---

## 📝 Summary

Given a word, determine the minimum number of pushes required to type it on a standard keyboard layout.

## 🔍 Key Observation

The solution uses a priority queue to sort characters by frequency and assigns them pushes in a specific order.

## ⚙️ Algorithm

1. Count the frequency of each character in the word.
2. Use a priority queue to sort characters by frequency in descending order.
3. Assign pushes to characters in groups of 8, starting with 1 push for the first 8 characters, 2 for the next 8, and so on.
4. Sum the pushes assigned to each character in the word.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting the characters by frequency.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `topic` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        x = {}
        pq = []
        for i in word:
            x[i] = x.get(i,0) + 1
        for ch,freq in x.items():
            heapq.heappush(pq,(-freq,ch))
        print(pq)
        count = 0
        i = 1
        while pq:
            freq,ch = heapq.heappop(pq)
            x[ch] = i
            count+=1
            if count == 8:
                i+=1
                count = 0
        print(x)
        res = 0
        for i in word:
            res += x[i]
        return res
```

</details>
