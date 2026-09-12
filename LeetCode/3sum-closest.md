# 🟠 3sum-closest — 3Sum Closest

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/3sum-closest/) &nbsp;|&nbsp; **Solved:** 2025-12-03

---

## 📝 Summary

Find the triplet in the array that sums closest to the target value.

## 🔍 Key Observation

Sort the array and use a two-pointer technique to efficiently find the closest sum.

## ⚙️ Algorithm

1. Sort the array to facilitate the two-pointer approach.
2. Initialize `bestSum` with the sum of the first three elements.
3. Iterate through the array, fixing one element at a time.
4. For each fixed element, use two pointers (`l` and `r`) to find the other two elements that sum to the closest value to the target.
5. Update `bestSum` if the current sum is closer to the target than the previous best sum.
6. Adjust the pointers based on the comparison of the current sum with the target.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loops.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`python` `sorting` `two-pointer`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        bestSum = nums[0]+nums[1]+nums[2]

        for i in range(n - 2):
            l, r = i + 1, n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if abs(total - target) < abs(bestSum - target):
                    bestSum = total
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else :
                    return total
        return bestSum
```

</details>
