# 🔵 344A — Magnets

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/344/A) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

Count the total number of magnet groups given a sequence of magnet orientations. A new group starts if a magnet's orientation differs from the preceding one.

## 🔍 Key Observation

A new group of magnets begins if and only if the current magnet's polarization (orientation) is different from the previous magnet's polarization.

## ⚙️ Algorithm

**Iterative scan**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N)` | `O(N)` |

## 🏷️ Tags

`implementation` `arrays` `counting` `ad-hoc`

<details>
<summary>💻 View solution</summary>

```python
t = int(input())
arr = []
for _ in range(t):
    arr.append(input())
cnt = 1
temp = ''
for i in range(1,len(arr)):
    if arr[i-1] != arr[i]:
        cnt+=1

print(cnt)
```

</details>
