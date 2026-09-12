# 🔵 1834A — Unit Array

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1834/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given an array of integers, determine the minimum number of operations required to make all elements equal by incrementing or decrementing elements.

## 🔍 Key Observation

The key insight is to balance the number of negative and positive elements to minimize operations.

## ⚙️ Algorithm

1. Count the occurrences of -1 and 1 in the array.
2. Increment the count of -1 until it is less than or equal to the count of 1.
3. If the count of -1 is odd after the loop, decrement it by 1 to balance the counts.
4. The number of operations required is the difference between the counts of -1 and 1.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`greedy` `math`

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
    x = {-1:0,1:0}
    for i in a:
        x[i] += 1
    cnt = 0
    while x[-1]>x[1]:
           x[-1]-=1
           cnt+=1
           x[1]+=1
    if x[-1]&1:
        x[-1]-=1
        cnt+=1
    print(cnt)
```

</details>
