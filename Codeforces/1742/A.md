# 🔵 1742A — Sum

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1742/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Given three integers, determine if any one of them is equal to the sum of the other two.

## 🔍 Key Observation

Since there are only three numbers, we can directly check all three possible pairs to see if their sum equals the remaining number.

## ⚙️ Algorithm

**Direct conditional checks**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`implementation` `math` `conditionals`

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
for _ in range(t):
    a,b,c = invr()
    if a+b == c or a+c == b or b+c == a:
        print("YES")
    else:
        print("NO")
```

</details>
