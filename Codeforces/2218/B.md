# 🔵 2218B — The 67th 6-7 Integer Problem

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/2218/B) &nbsp;|&nbsp; **Solved:** 2026-08-16

---

## 📝 Summary

Given an array of integers, find the maximum sum of the first element and the minimum sum of the remaining elements.

## 🔍 Key Observation

The solution involves sorting the array and then calculating the sum of the first element and the sum of the remaining elements in reverse order.

## ⚙️ Algorithm

1. Read the number of test cases 't'.
2. For each test case:
   a. Read the array of integers.
   b. Sort the array in descending order.
   c. Calculate the sum of the first element.
   d. Calculate the sum of the remaining elements by iterating through the sorted array starting from the second element.
   e. Print the difference between the sum of the first element and the sum of the remaining elements.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sort` `sum` `difference`

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

t = inp()
for _ in range(t):
    arr = inlt()
    arr.sort(reverse=True)
    s = arr[0]
    for i in range(1,len(arr)):
        s-=arr[i]
    print(s)
```

</details>
