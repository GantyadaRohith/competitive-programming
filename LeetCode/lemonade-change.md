# 🟠 lemonade-change — Lemonade Change

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/lemonade-change/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Given a list of bills, determine if it's possible to provide change for each customer.

## 🔍 Key Observation

The solution uses a greedy algorithm to manage the change efficiently.

## ⚙️ Algorithm

The algorithm iterates through each bill. For a 5-dollar bill, it increments the 5-dollar count. For a 10-dollar bill, it checks if there's a 5-dollar bill available to exchange. For a 20-dollar bill, it checks if there's a 10-dollar and a 5-dollar bill available to exchange, or if there are three 5-dollar bills available. If at any point it's impossible to provide change, it returns False. Otherwise, it returns True.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the number of bills, as each bill is processed once.` | `O(1) auxiliary space, as only a few variables are used.` |

## 🏷️ Tags

`greedy` `change` `bills`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        x,y,z = 0,0,0
        if bills[0] != 5:
            return False
        for i in bills:
            if i == 5:
                x+=1
            elif i == 10:
                if x >= 1:
                    x-=1
                    y+=1
                else:
                    return False
            elif i == 20:
                if y >= 1 and x >= 1:
                    y-=1
                    x-=1
                elif x >= 3:
                    x-=3
                else:
                    return False
            
        return True
```

</details>
