# 🟠 x-of-a-kind-in-a-deck-of-cards — X of a Kind in a Deck of Cards

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/) &nbsp;|&nbsp; **Solved:** 2025-10-12

---

## 📝 Summary

Determine if there exists a group of cards with the same number of cards in a deck.

## 🔍 Key Observation

Use the greatest common divisor (GCD) to check if all card counts are divisible by a common value.

## ⚙️ Algorithm

1. Count the occurrences of each card using a Counter.
2. Extract the counts into a list.
3. Use the reduce function with gcd to find the GCD of all counts.
4. Return True if the GCD is at least 2, indicating a valid group exists.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to counting and GCD computation.` | `O(n) for storing card counts.` |

## 🏷️ Tags

`gcd` `counter` `math`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        vals = list(count.values())
        g = reduce(gcd, vals)
        return g >= 2
```

</details>
