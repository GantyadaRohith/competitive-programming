# 🔵 1766A — Extremely Round

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1766/A) &nbsp;|&nbsp; **Solved:** 2026-08-16

---

## 📝 Summary

Given a number, determine the minimum number of digits that need to be removed to make the number extremely round.

## 🔍 Key Observation

The key insight is to remove all digits except the most significant digit (MSB) and the last digit.

## ⚙️ Algorithm

1. Read the number of test cases `t`.
2. For each test case:
   - Read the number `n`.
   - If `n` is less than or equal to 9, print `n` as it is already extremely round.
   - Otherwise, calculate the number of digits to remove by subtracting the length of the number minus 1 (to exclude the last digit) from 9.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `lowercase` `math` `tags`

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
    if n<=9:
        print(n)
    else:
        l = len(str(n))
        msb = int(str(n)[0])
        cnt = 0
        while l>0:
            if l == 1:
                cnt+=msb
                break
            l-=1
            cnt+=9
        print(cnt)


```

</details>
