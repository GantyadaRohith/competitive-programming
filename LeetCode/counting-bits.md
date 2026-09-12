# 🟠 counting-bits — Counting Bits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/counting-bits/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Given a non-negative integer n, return an array of size n+1 where the ith element is the number of 1's in the binary representation of i.

## 🔍 Key Observation

The number of 1's in the binary representation of a number is equal to the number of 1's in the binary representation of the number minus the largest power of 2 less than or equal to the number.

## ⚙️ Algorithm

The solution uses dynamic programming to store the number of 1's for each number up to n. It iterates through each number, checking if it is a power of 2. If it is, it sets the count to 1. Otherwise, it calculates the count by counting the number of 1's in the binary representation of the number.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to the use of bit manipulation.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`dynamic-programming` `bit-manipulation` `binary-representation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        dp[0] = 0
        j = 1
        for i in range(1,n+1):
            if i%(2**j) == 0:
                dp[i] = 1
                j+=1
            else:
                temp = i
                cnt = 0
                while i:
                    if i&1:
                        cnt+=1
                    i = i>>1
                dp[temp] = cnt
        return dp
```

</details>
