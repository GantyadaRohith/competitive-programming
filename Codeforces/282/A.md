# 🔵 282A — Bit++

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/282/A) &nbsp;|&nbsp; **Solved:** 2026-07-27

---

## 📝 Summary

Given a sequence of '+' and '-' characters, determine the final value after processing all characters.

## 🔍 Key Observation

The final value is the sum of the '+' and '-' characters.

## ⚙️ Algorithm

The solution iterates through each character in the input string. It increments a counter 'x' for each '+' and decrements it for each '-'. The final value of 'x' is the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the input string.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`implementation` `string` `iteration`

<details>
<summary>💻 View solution</summary>

```python
n = int(input())
x = 0
for i in range(n):
    s = input()
    if '+' in s:
        x+=1
    else:
        x-=1
        
print(x)
```

</details>
