# 🔵 110A — Nearly Lucky Number

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/110/A) &nbsp;|&nbsp; **Solved:** 2026-07-27

---

## 📝 Summary

Given a number, determine if it contains exactly four or seven '4's or '7's.

## 🔍 Key Observation

The problem requires counting the occurrences of '4' and '7' in the number.

## ⚙️ Algorithm

The solution iterates through each digit of the number by repeatedly taking the remainder when divided by 10 (to get the last digit) and then removing the last digit by integer division. It counts how many times '4' or '7' appears and checks if the count is exactly 4 or 7.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(d) where d is the number of digits in the input number, as each digit is processed once.` | `O(1) auxiliary space, as only a few variables are used.` |

## 🏷️ Tags

`implementation` `counting` `digits`

<details>
<summary>💻 View solution</summary>

```python
n = int(input())
count = 0
le = len(str(n))
while n:
    i = n%10
    n//=10
    if i in {4,7}:
        count+=1
if count in {4,7}:
    print('YES')
else:
    print('NO')
```

</details>
