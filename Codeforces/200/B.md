# 🔵 200B — Drinks

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/200/B) &nbsp;|&nbsp; **Solved:** 2026-08-26

---

## 📝 Summary

Given a list of integers representing the number of drinks each person drinks, calculate the average number of drinks per person.

## 🔍 Key Observation

The key insight is to sum the total number of drinks and divide by the number of people.

## ⚙️ Algorithm

1. Read the number of people (t) and the list of drinks (arr) from input.
2. Calculate the total number of drinks by summing the elements of arr.
3. Divide the total number of drinks by the number of people to get the average.
4. Print the average.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass required to sum the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `python` `sum` `average`

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
