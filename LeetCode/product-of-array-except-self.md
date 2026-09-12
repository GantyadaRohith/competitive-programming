# 🟠 product-of-array-except-self — Product of Array Except Self

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/product-of-array-except-self/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Given an array nums, return an array where each element is the product of all elements in the array except the element at that index.

## 🔍 Key Observation

The key insight is to use two auxiliary arrays to store the products of all elements to the left and right of each element, then multiply these arrays to get the desired result.

## ⚙️ Algorithm

1. Initialize two arrays, `pre` and `post`, of the same length as `nums`. Set `post[len(nums)-1]` to `nums[len(nums)-1]` and `pre[0]` to `nums[0]`. 2. Fill the `pre` array by multiplying each element by the previous element. 3. Fill the `post` array by multiplying each element by the next element. 4. For each element in `nums` (except the first and last), calculate the product of the corresponding elements in `pre` and `post` to get the result. 5. Set the first and last elements of the result array to the products of the `post` array for the first and last elements, respectively.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array for each auxiliary array.` | `O(1) auxiliary space as the space used for the `pre` and `post` arrays is constant.` |

## 🏷️ Tags

`array` `prefix` `postfix`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0]*len(nums)
        post = [0]*len(nums)
        post[len(nums)-1] = nums[len(nums)-1]
        pre[0] = nums[0]
        for i in range(1,len(nums)):
            pre[i] = nums[i]*pre[i-1]
        for i in range(len(nums)-2,-1,-1):
            print(i)
            post[i] = nums[i] * post[i+1]
        res = [0]*len(nums)
        for i in range(1,len(nums)-1):
            res[i] = pre[i-1]*post[i+1]
        res[0] = post[1]
        res[len(nums)-1] = pre[len(nums)-2]
        return res
```

</details>
