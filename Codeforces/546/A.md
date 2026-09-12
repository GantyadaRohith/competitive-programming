# 🔵 546A — Soldier and Bananas

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/546/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Given a soldier's capacity to carry bananas and the number of bananas available, determine how many bananas the soldier can't carry.

## 🔍 Key Observation

The total number of bananas the soldier can carry is the sum of the first w natural numbers multiplied by k.

## ⚙️ Algorithm

1. Calculate the total number of bananas the soldier can carry using the formula for the sum of the first w natural numbers: (w*(w+1))/2. Multiply this by k to get the total capacity of bananas the soldier can carry in one trip.
2. Calculate the total number of bananas the soldier can carry in n trips.
3. If the total capacity is greater than or equal to n, the soldier can't carry any bananas. Otherwise, calculate the number of bananas the soldier can't carry.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time arithmetic operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `math` `tags`

<details>
<summary>💻 View solution</summary>

```python
import sys
input = sys.stdin.readline
def invr():
    return(map(int,input().split()))

k,n,w = invr()
su = (w*(w+1))/2
to = su*k
if to >= n:
    print(int(to-n))
else:
    print(0)
```

</details>
