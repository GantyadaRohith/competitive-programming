# 🔵 1873B — Good Kid

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1873/B) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Given an array of integers, find the product of all elements except the minimum element.

## 🔍 Key Observation

The key insight is to handle the minimum element separately to avoid it affecting the product of the rest of the elements.

## ⚙️ Algorithm

1. Initialize variables to store the minimum element and the product of all elements except the minimum element.
2. Iterate through the array to find the minimum element and calculate the product of all elements except the minimum element.
3. If the minimum element is found more than once, increment it by 1 to ensure the product is valid.
4. Print the final product.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`python` `array` `product` `minimum`

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
    a = inlt()
    prod = 1
    c = 0
    for i in a:
        if i == min(a) and c == 0:
            i+=1
            c+=1
        prod*=i
    print(prod)
```

</details>
