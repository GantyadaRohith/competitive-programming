# 🟠 boats-to-save-people — Boats to Save People

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/boats-to-save-people/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given a list of people's weights and a boat's weight limit, determine the minimum number of boats required to rescue all people.

## 🔍 Key Observation

The key insight is to sort the people by weight and use two pointers to pair the lightest and heaviest people in each boat.

## ⚙️ Algorithm

1. Sort the people's weights in ascending order.
2. Initialize two pointers, `low` at the start and `high` at the end of the sorted list.
3. While `low` is less than or equal to `high`:
   - If the sum of the weights of the people at `low` and `high` is less than or equal to the boat's limit, they can share a boat. Move both pointers inward.
   - Otherwise, the heaviest person must use a boat alone. Move the `high` pointer inward.
4. Increment the boat count for each pair or single person in a boat.
5. Return the total number of boats used.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `boats` `rescue`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        cnt = 0
        high = len(people)-1
        for i in range(len(people)-1,-1,-1):
            if people[i]>=limit:
                cnt+=1
            else:
                high = i
                break
        low = 0
        while low <= high:
            if people[low]+people[high] <= limit:
                cnt+=1
                low+=1
                high-=1
            else:
                cnt+=1
                high-=1
        return cnt
```

</details>
