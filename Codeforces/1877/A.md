# 🔵 1877A — Goals of Victory

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1877/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Given the scores of n-1 teams, find the score for the n-th team such that the sum of scores of all n teams is exactly zero.

## 🔍 Key Observation

To achieve a total sum of zero for all n scores, the n-th team's score must be the negative of the sum of the other n-1 team's scores.

## ⚙️ Algorithm

**Direct calculation / Summation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N)` | `O(N)` |

## 🏷️ Tags

`math` `arrays` `implementation` `ad-hoc`

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
    n = inp()
    arr = inlt()
    print(-sum(arr))


```

</details>
