# 🔵 791A — Bear and Big Brother

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/791/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Given two integers l and b, determine the minimum number of operations required to make l equal to b by multiplying l by 3 and b by 2.

## 🔍 Key Observation

The problem can be solved by iteratively multiplying l by 3 and b by 2 until l is at least twice the size of b.

## ⚙️ Algorithm

1. Initialize l and b as input values.
2. Use a while loop to multiply l by 3 and b by 2 until l is at least twice the size of b.
3. Increment a counter i for each operation.
4. Print the counter i after the loop.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log(max(l, b))) due to the doubling and tripling operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `bear` `big` `brother`

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

l,b = invr()
i = 1
while l*(3) <= b*(2):
    l = l*3
    b = b*2
    i+=1
print(i)

```

</details>
