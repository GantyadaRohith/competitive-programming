# 🔵 1858A — Buttons

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1858/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given a list of button presses, determine which player wins based on the number of presses and the parity of the last press.

## 🔍 Key Observation

The key insight is to compare the number of presses and the parity of the last press to determine the winner.

## ⚙️ Algorithm

1. Read the number of test cases `n`.
2. For each test case, read the number of presses `a` and `b`, and the parity of the last press `c`.
3. Compare `a` and `b`:
   - If `a > b`, the first player wins.
   - If `a == b` and `c` is odd, the first player wins.
   - Otherwise, the second player wins.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the input.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`games` `greedy` `math`

<details>
<summary>💻 View solution</summary>

```python
n = int(input())
test = []
for _ in range(n):
    test.append(list(map(int,input().split())))
for i in range(len(test)):
    if test[i][0] > test[i][1]:
        print("First")
    elif test[i][0] == test[i][1] and test[i][2]&1:
        print("First")
    else:
        print("Second")
```

</details>
