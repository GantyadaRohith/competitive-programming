# 🟠 count-array-pairs-divisible-by-k — Count Array Pairs Divisible by K

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-array-pairs-divisible-by-k/) &nbsp;|&nbsp; **Solved:** 2026-02-23

---

## 📝 Summary

Given an array of integers and a divisor k, count the number of pairs of integers whose product is divisible by k.

## 🔍 Key Observation

Using the greatest common divisor (GCD) to find pairs of numbers whose product is divisible by k.

## ⚙️ Algorithm

1. Calculate the GCD of each number in the array with k.
2. Use a frequency counter to count occurrences of each GCD value.
3. Iterate over all pairs of GCD values and check if their product is divisible by k.
4. Count valid pairs based on the frequency of each GCD value.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log k) due to the GCD calculations and the nested loop over GCD values.` | `O(n) for the frequency counter.` |

## 🏷️ Tags

`gcd` `pair` `count`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        gcd_values = [math.gcd(num, k) for num in nums]
        freq = Counter(gcd_values)

        ans = 0
        gcd_keys = list(freq.keys())

        for i in range(len(gcd_keys)):
            g1 = gcd_keys[i]

            for j in range(i, len(gcd_keys)):
                g2 = gcd_keys[j]

                if (g1 * g2) % k == 0:
                    if i == j:
                        c = freq[g1]
                        ans += c * (c - 1) // 2
                    else:
                        ans += freq[g1] * freq[g2]

        return ans
```

</details>
