# 🔵 1829B — Blank Space

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1829/B) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given a sequence of 0s and 1s, find the maximum number of consecutive 1s that can be obtained by removing at most one 0.

## 🔍 Key Observation

The key insight is to use a sliding window approach to track the maximum number of consecutive 1s while allowing at most one 0 to be removed.

## ⚙️ Algorithm

1. Initialize two pointers, `left` and `right`, to mark the current window and a variable `max_ones` to store the maximum number of consecutive 1s found so far. Also, initialize `zero_count` to count the number of zeros in the current window.
2. Iterate with the `right` pointer through the array:
   - If the current element is 0, increment `zero_count`.
   - If `zero_count` exceeds 1, move the `left` pointer to the right until `zero_count` is less than or equal to 1.
   - Update `max_ones` with the maximum of its current value and the length of the current window (`right - left + 1`).
3. Return `max_ones` as the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the input array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`implementation` `sliding window`

<details>
<summary>💻 View solution</summary>

```python
a = int(input())
for _ in range(a):
    n = int(input())
    s = list(map(int,input().split()))
    cnt = 0
    temp = 0
    for i in range(n):
        if s[i] == 0:
            temp+=1
        elif temp>0 and s[i] == 1:
            cnt = max(cnt,temp)
            temp = 0
        cnt = max(cnt,temp)
    print(cnt)

```

</details>
