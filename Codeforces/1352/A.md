# 🔵 1352A — Sum of Round Numbers

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1352/A) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

Given a positive integer, count the number of digits that are not zero and print them in order.

## 🔍 Key Observation

The problem requires counting non-zero digits and printing them in order, which can be efficiently achieved by converting the number to a string and iterating over it.

## ⚙️ Algorithm

1. Read the number of test cases `t`.
2. For each test case:
   a. Read the integer `n`.
   b. If `n` is between 1 and 9, print 1 and `n`.
   c. Otherwise, convert `n` to a string.
   d. Count the number of non-zero digits.
   e. Print the count.
   f. Print each non-zero digit followed by the appropriate number of zeros to match its original position in the number.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the conversion of the number to a string and the iteration over its digits.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `string` `count`

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
