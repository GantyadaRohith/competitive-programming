# 🟠 next-greater-element-ii — Next Greater Element II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/next-greater-element-ii/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Given an array, find the next greater element for each element in the array, considering the array as circular.

## 🔍 Key Observation

The key insight is to use a stack to keep track of indices of elements for which the next greater element has not been found yet, and to handle the circular nature of the array by extending the array length.

## ⚙️ Algorithm

1. Initialize an empty stack and a result array of the same length as the input array, filled with -1 to indicate no greater element found yet.
2. Extend the input array to make it circular by duplicating it.
3. Iterate through the extended array, using the index modulo the length of the extended array to handle the circular nature.
4. For each element, while the stack is not empty and the current element is greater than the element at the index stored at the top of the stack, pop the stack and update the result array with the current element.
5. Push the current index onto the stack.
6. Return the result array.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array and stack operations.` | `O(n) for the stack and result array.` |

## 🏷️ Tags

`stack` `circular` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1]*len(nums)
        N = 2*len(nums) - 1
        for i in range(N):
            i = i%len(nums)
            while stack and nums[stack[-1]] < nums[i]:
                p_i = stack.pop()
                result[p_i] = nums[i]        
            stack.append(i)
        return result

```

</details>
