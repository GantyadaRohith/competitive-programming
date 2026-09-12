# 🔵 1352A — Sum of Round Numbers

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1352/A) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

Decompose a given integer into a sum of the minimum possible number of "round numbers" (numbers with only one non-zero digit) and output these round numbers.

## 🔍 Key Observation

Each non-zero digit in the decimal representation of the given number corresponds to a unique round number. For example, the digit 'd' at position 'k' (from the right, 0-indexed) corresponds to the round number d * 10^k.

## ⚙️ Algorithm

**Digit extraction / String processing**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(D)` | `O(D)` |

## 🏷️ Tags

`implementation` `math` `string processing` `digit manipulation`

<details>
<summary>💻 View solution</summary>

```python
t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    if n>0 and n<10:
        print(1)
        print(n)
    else:
        s = str(n)
        for i in range(len(s)):
            if s[i]!= '0':
                cnt+=1
        print(cnt)
        for i in range(len(s)):
            if s[i]!= '0':
                print(s[i]+'0'*(len(s)-int(i)-1),end = " ")
        print()
    
```

</details>
