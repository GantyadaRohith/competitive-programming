# 🔵 344A — Magnets

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/344/A) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

Given a list of strings, count the number of unique strings.

## 🔍 Key Observation

The solution uses a simple counter to track unique strings.

## ⚙️ Algorithm

The algorithm iterates through the list of strings, comparing each string to the previous one. If they are different, it increments a counter. This effectively counts the number of unique strings.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the list.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `string` `count`

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
