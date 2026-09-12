# 🔵 231A — Team

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/231/A) &nbsp;|&nbsp; **Solved:** 2026-07-27

---

## 📝 Summary

Given a list of three integers for each of n teams, determine how many teams have at least two of the three numbers summing to at least 2.

## 🔍 Key Observation

The key insight is to check each team's numbers to see if at least two of them sum to at least 2.

## ⚙️ Algorithm

The algorithm iterates over each team, converts the input string to integers, and checks if the sum of any two numbers is at least 2. If so, it increments a counter. Finally, it prints the count of such teams.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the input data.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`brute force` `lowercase` `team` `problem`

<details>
<summary>💻 View solution</summary>

```python
n = int(input())
count = 0
for i in range(n):
    x,y,z = map(int,input().split())
    if x+y+z >= 2:
        count+=1
print(count)
```

</details>
