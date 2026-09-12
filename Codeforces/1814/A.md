# 🔵 1814A — Coins

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1814/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given a number of coins and a target sum, determine if it's possible to make the target sum using the coins.

## 🔍 Key Observation

The key insight is to check if the number of coins is even or if the target sum is odd.

## ⚙️ Algorithm

The algorithm checks if the number of coins is even or if the target sum is odd. If either condition is true, it prints 'YES', indicating that the target sum can be made using the coins. Otherwise, it prints 'NO'.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`implementation` `math`

<details>
<summary>💻 View solution</summary>

```python
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    f =  0
    if n % 2 == 0 or k % 2 == 1:
            print("YES")
    else:
            print("NO")
```

</details>
