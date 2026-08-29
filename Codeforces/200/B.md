# 🔵 200B — Drinks

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/200/B) &nbsp;|&nbsp; **Solved:** 2026-08-26

---

## 📝 Summary

Calculate the average percentage of orange juice in a mixture of several drinks, where each drink contributes equally and has a given percentage of orange juice.

## 🔍 Key Observation

The final percentage of orange juice in the mixture is simply the arithmetic mean of the individual percentages of each drink.

## ⚙️ Algorithm

**Direct calculation / Basic arithmetic**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`implementation` `math` `arithmetic` `average`

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

t = inp()
arr = inlt()
s = sum(arr)
print(s/t)
```

</details>
