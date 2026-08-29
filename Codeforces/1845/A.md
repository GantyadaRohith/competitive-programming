# 🔵 1845A — Forbidden Integer

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1845/A) &nbsp;|&nbsp; **Solved:** 2026-08-16

---

## 📝 Summary

Accepted solution for Forbidden Integer on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^4) (estimated -- 4 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`constructive algorithms` `implementation` `math` `number theory` `recursion`

<details>
<summary>💻 View solution</summary>

```python
'''import sys
input = sys.stdin.readline
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

t = inp()
for _ in range(t):
    n,k,x = invr()
    out = []
    if k == n:
        print('YES')
        print(1)
        print(k)
    elif k == x and x == 1:
        print("NO")
    elif k == x:
        res = n//(k-1)
        out.append([k-1]*res)
        rem = n%(k-1)
        for i in range(1,k-1):
            if rem%i == 0 and i != x:
                out.append([i]*(rem//i))
        out = [item for sublist in out for item in sublist]
        if sum(out) == n:
            print("YES")
            print(len(out))
            print(*out)
        else:
            print("NO")
    else:
        res = n//(k)
        out.append([k]*res)
        rem = n%(k)
        for i in range(1,k):
            if rem%i == 0 and i != x:
                out.append([i]*(rem//i))
        out = [item for sublist in out for item in sublist]
        if sum(out) == n:
            print("YES")
            print(len(out))
            print(*out)
        else:
            print("NO")'''

import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        
        # Case 1: 1 is not forbidden. We can just use all 1s.
        if x != 1:
            print("YES")
            print(n)
            print(*([1] * n))
            
        # Case 2: 1 is forbidden. We must use numbers >= 2.
        else:
            if k == 1:
                # We can only use 1, but 1 is forbidden
                print("NO")
            elif k == 2:
                # We can only use 2, so n must be even
                if n % 2 == 0:
                    print("YES")
                    print(n // 2)
                    print(*([2] * (n // 2)))
                else:
                    print("NO")
            else:
                # k >= 3, we can use 2 and 3. We can make any number >= 2.
                if n == 1:
                    print("NO")
                elif n % 2 == 0:
                    print("YES")
                    print(n // 2)
                    print(*([2] * (n // 2)))
                else:
                    print("YES")
                    # We use one '3', and the rest as '2's
                    twos_count = (n - 3) // 2
                    print(1 + twos_count) # Length is 1 (for the '3') + number of 2s
                    ans = [3] + [2] * twos_count
                    print(*ans)

if __name__ == '__main__':
    solve()
```

</details>
