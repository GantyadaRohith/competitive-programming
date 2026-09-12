# 🔵 2259B — Minus Two

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/2259/B) &nbsp;|&nbsp; **Solved:** 2026-09-05

---

## 📝 Summary

Given an array of integers, determine the maximum number of pairs that can be formed such that the sum of each pair is even.

## 🔍 Key Observation

The key insight is to count the number of odd and even numbers in the array and use their properties to determine the maximum number of pairs.

## ⚙️ Algorithm

1. Count the number of odd and even numbers in the array.
2. If there are at least two odd numbers, they can form pairs with each other, contributing to the maximum count.
3. If there are at least two even numbers, they can also form pairs with each other.
4. If there is at least one odd and one even number, they can form a pair.
5. The maximum number of pairs is the sum of the counts of odd and even numbers, minus the minimum of the counts of odd and even numbers (to avoid double-counting pairs).

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`python` `array` `counting` `pairing`

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
