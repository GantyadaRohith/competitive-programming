# 🔵 2259B — Minus Two

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/2259/B) &nbsp;|&nbsp; **Solved:** 2026-09-05

---

## 📝 Summary

The problem asks to find the maximum number of elements in a given array that can be made equal to some non-negative integer `K` by repeatedly applying the operation `x -> x-2` on any chosen element.

## 🔍 Key Observation

When only the operation `x -> x-2` is allowed, numbers can only be made equal if they belong to the same congruence class modulo 4. Specifically, odd numbers form one class (`x % 2 == 1`), numbers of the form `4k+2` form another class (`x % 4 == 2`), and numbers of the form `4k` form a third class (`x % 4 == 0`). Elements cannot transition between these classes, so the solution is to find the largest of these three distinct groups.

## ⚙️ Algorithm

**Counting / Frequency Map**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N)` | `O(1)` |

## 🏷️ Tags

`math` `number theory` `counting` `greedy`

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
    cnt = 0
    s = {}
    for i in arr:
        if i&1:
            s[1] = s.get(1,0) + 1
        else:
            diff = i//2
            if diff&1:
                s[4] = s.get(4,0) + 1
            else:
                s[2] = s.get(2,0) + 1
    print(max(s.values()))
```

</details>
