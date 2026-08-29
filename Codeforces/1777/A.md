# 🔵 1777A — Everybody Likes Good Arrays!

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1777/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

The problem asks for the minimum number of operations to make an array "good", where a good array has no two adjacent elements with the same parity. An operation involves multiplying two adjacent elements and replacing them with their product.

## 🔍 Key Observation

If two adjacent elements have the same parity, they must be combined. Since the product of two odd numbers is odd, and the product of two even numbers is even, combining them always results in a single element with the same parity type. Each such instance of two adjacent elements having the same parity absolutely requires one operation to resolve that specific bad adjacency, making a greedy approach optimal.

## ⚙️ Algorithm

**Greedy**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N)` | `O(N)` |

## 🏷️ Tags

`greedy` `math` `parity`

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
    out = [arr[0]]
    cnt = 0
    for i in range(1,n):
        if (out[-1]&1 == 1 and arr[i]&1 == 1)or (out[-1]&1 == 0 and arr[i]&1 == 0):
            cnt+=1
            temp = out.pop()
            out.append(temp*arr[i])
        else:
            out.append(arr[i])
    print(cnt)
```

</details>
