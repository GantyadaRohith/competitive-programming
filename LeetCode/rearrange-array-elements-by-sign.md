# 🟠 rearrange-array-elements-by-sign — Rearrange Array Elements by Sign

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rearrange-array-elements-by-sign/) &nbsp;|&nbsp; **Solved:** 2025-12-12

---

## 📝 Summary

Rearrange an array such that all negative numbers come before positive numbers while maintaining their relative order.

## 🔍 Key Observation

Use two separate lists to store negative and positive numbers, then interleave them.

## ⚙️ Algorithm

1. Initialize two empty lists: `odd` for negative numbers and `eve` for positive numbers.
2. Iterate through the input list `nums` and append each number to the appropriate list based on its sign.
3. Initialize two pointers `x` and `y` to track the current positions in `eve` and `odd`, respectively.
4. Iterate through the combined length of `odd` and `eve` and append the next negative or positive number to the `out` list based on the current index's parity.
5. Return the `out` list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the input list.` | `O(n) for the auxiliary lists `odd` and `eve`.` |

## 🏷️ Tags

`python` `array` `rearrange` `sign`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        out = []
        odd = []
        eve = []
        for i in nums:
            if i < 0:
                odd.append(i)
            else:
                eve.append(i)
        x = y = 0
        for i in range(len(odd)+len(eve)):
            if i%2==0 and x < len(eve):
                out.append(eve[x])
                x+=1
            elif i%2!= 0 and y<len(odd):
                out.append(odd[y])
                y+=1
            else:
                continue
        return out
```

</details>
