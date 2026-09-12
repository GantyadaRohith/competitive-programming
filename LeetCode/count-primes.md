# 🟠 count-primes — Count Primes

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-primes/) &nbsp;|&nbsp; **Solved:** 2025-10-12

---

## 📝 Summary

Count the number of prime numbers less than a given integer n.

## 🔍 Key Observation

Use the Sieve of Eratosthenes to efficiently count primes.

## ⚙️ Algorithm

1. Initialize a boolean array `p` of size `N+1` with all elements set to 1 (indicating potential primes).
2. Set `p[0]` and `p[1]` to 0 (not prime).
3. Iterate through each number `i` starting from 2.
4. If `p[i]` is still 1, it is a prime number.
5. Mark all multiples of `i` starting from `i*i` as non-prime.
6. Increment the count of primes by the value of `p[i]` at each step.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log log n) due to the Sieve of Eratosthenes.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `sieve` `prime`

<details>
<summary>💻 View solution</summary>

```python
N = 5*10**6
p = [1]*(N+1)
p[0] = p[1] = 0
for i in range(2, N+1):
    if p[i]:
        for j in range(i*i, N+1, i):
            p[j] = 0
    p[i] += p[i-1]
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        return p[n-1]
```

</details>
