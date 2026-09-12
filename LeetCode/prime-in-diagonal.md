# 🟠 prime-in-diagonal — Prime In Diagonal

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/prime-in-diagonal/) &nbsp;|&nbsp; **Solved:** 2026-07-17

---

## 📝 Summary

Given a square matrix of integers, find the largest prime number located on the main diagonal or its anti-diagonal.

## 🔍 Key Observation

Identify the main diagonal and anti-diagonal of the matrix and check for prime numbers in each.

## ⚙️ Algorithm

1. Define a helper function `isPrime` to check if a number is prime.
2. Iterate through the matrix:
   - Check the main diagonal (nums[i][i]) for primality.
   - Check the anti-diagonal (nums[i][len(nums)-i-1]) for primality, except when the index is the middle of the matrix.
3. Collect all prime numbers found.
4. Return the maximum prime number found, or 0 if no primes are found.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loop iterating through the matrix.` | `O(1) auxiliary space as only a few variables are used.` |

## 🏷️ Tags

`prime` `diagonal` `matrix` `check`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(n):
            if n<=1:
                return False
            if n ==2 :
                return True
            if n%2 == 0:
                return False
            for i in range(3,math.ceil(n**0.5)+1):
                if n%i == 0:
                    return False
            return True
        out = []
        for i in range(len(nums)):
            if isPrime(nums[i][i]):
                out.append(nums[i][i])
            if isPrime(nums[i][len(nums)-i-1]) and i!=len(nums)-i-1:
                out.append(nums[i][len(nums)-i-1])
        return max(out) if out else 0
            
```

</details>
