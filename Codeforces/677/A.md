# 🔵 677A — Vanya and Fence

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/677/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Given a fence with heights, calculate the minimum number of posts needed to ensure all fences are at least as tall as a given height.

## 🔍 Key Observation

The key insight is to count the number of posts needed for each segment where the fence height is less than the given height.

## ⚙️ Algorithm

1. Initialize a variable `width` to 0. This will keep track of the total number of posts needed.
2. Iterate through the list of fence heights.
3. For each height, if it is less than the given height `h`, add 2 to `width` (since two posts are needed for a segment where the height is less than `h`).
4. If the height is greater than or equal to `h`, add 1 to `width` (since one post is needed for a segment where the height is at least `h`).
5. Print the final value of `width`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the list of fence heights.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `fence` `posts`

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

n,h = invr()
arr = inlt()
width = 0
for i in arr:
    if i > h:
        width+=2
    else:
        width+=1
print(width)
```

</details>
