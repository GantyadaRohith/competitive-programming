# 🔵 1788A — One and Two

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1788/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given a sequence of integers, determine the position of the first occurrence of the number 2, or -1 if it does not appear an odd number of times.

## 🔍 Key Observation

The key insight is to count the occurrences of the number 2 and check if the count is odd or even.

## ⚙️ Algorithm

1. Read the number of test cases `t`.
2. For each test case, read the length of the sequence `n` and the sequence itself.
3. Count the occurrences of the number 2 in the sequence.
4. If the count of 2 is 0, print 1.
5. If the count of 2 is odd, print -1.
6. If the count of 2 is even, find the first occurrence of 2 and print its position (1-based index).

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the sequence to count the occurrences of 2.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `implementation` `math`

<details>
<summary>💻 View solution</summary>

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = {1: 0, 2: 0}
    te = list(map(int, input().split()))

    for i in te:
        a[i] = a.get(i, 0) + 1

    if a[2] == 0:
        print(1)

    elif a[2] & 1:
        print(-1)

    else:
        temp = a[2] // 2

        for i in range(n):
            if te[i] == 2:
                temp -= 1

            if temp == 0:
                print(i + 1)
                break 
```

</details>
