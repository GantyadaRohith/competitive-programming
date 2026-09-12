# 🟠 3sum — 3Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/3sum/) &nbsp;|&nbsp; **Solved:** 2025-12-03

---

## 📝 Summary

Given an array of integers, find all unique triplets in the array that sum up to zero.

## 🔍 Key Observation

Sorting the array and using two pointers to find triplets efficiently.

## ⚙️ Algorithm

1. Sort the array to facilitate the two-pointer technique.
2. Iterate through the array, treating each element as a potential first element of a triplet.
3. For each element, use two pointers (left and right) to find the other two elements that sum up to the negative of the current element.
4. Skip duplicate elements to avoid duplicate triplets.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loops and sorting.` | `O(1) auxiliary space (excluding the space used for the result list).` |

## 🏷️ Tags

`sort` `two-pointer` `triplet` `leetcode`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result

```

</details>
