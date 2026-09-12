# 🔵 1777A — Everybody Likes Good Arrays!

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1777/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Given an array, determine the minimum number of elements to remove to make all elements in the array have the same parity (all odd or all even).

## 🔍 Key Observation

The key insight is to track the parity of the last element added to the output array and ensure that the parity of the current element matches the last added element.

## ⚙️ Algorithm

1. Initialize an empty list `out` with the first element of the input array `arr` and a counter `cnt` to zero.
2. Iterate through the rest of the array starting from the second element.
3. For each element, check if the parity of the last element in `out` matches the parity of the current element.
4. If they match, increment the counter `cnt` and multiply the last element in `out` by the current element, then append the result to `out`.
5. If they do not match, append the current element to `out`.
6. Print the counter `cnt` after processing all elements.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`bitwise` `parity` `array`

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
