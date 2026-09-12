# 🔵 734A — Anton and Danik

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/734/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Given a string of 'A's and 'B's, determine who wins the game based on the number of 'A's and 'B's.

## 🔍 Key Observation

The key insight is to count the occurrences of 'A' and 'B' and compare them to determine the winner.

## ⚙️ Algorithm

1. Initialize counters for 'A' and 'B'.
2. Iterate through the string and update the counters based on the character encountered.
3. Compare the counters to determine the winner: 'Friendship' if equal, 'Anton' if 'A' is more, 'Danik' if 'B' is more.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the string.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`simple` `counting` `comparison`

<details>
<summary>💻 View solution</summary>

```python
n = int(input())
st = input()
a = b = 0
for i in st:
    if i == 'A':
        a+=1
    else:
        b+=1
if a == b:
    print("Friendship")
elif a>b:
    print("Anton")
else:
    print("Danik")
```

</details>
