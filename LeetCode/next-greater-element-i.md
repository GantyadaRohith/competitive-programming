# 🟠 next-greater-element-i — Next Greater Element I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/next-greater-element-i/) &nbsp;|&nbsp; **Solved:** 2026-07-19

---

## 📝 Summary

Given two arrays, find the next greater element for each element in the first array based on the second array.

## 🔍 Key Observation

Use a stack to keep track of indices of elements in the second array, allowing for efficient lookup of next greater elements.

## ⚙️ Algorithm

1. Initialize a stack and a result array filled with -1s. The result array will store the next greater element for each element in nums1.
2. Iterate through nums2. For each element, while the stack is not empty and the top element of the stack is less than the current element, pop the stack and set the result for the popped element to the current element.
3. Push the current index of nums2 onto the stack.
4. After processing all elements in nums2, the result array contains the next greater element for each element in nums1.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n + m), where n is the length of nums1 and m is the length of nums2.` | `O(m) for the stack and O(n) for the result array.` |

## 🏷️ Tags

`stack` `array` `next-greater-element`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = [-1]*len(nums1)

        for i in range(len(nums1)):
            f = -1
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    f+=1
                if f == 0:
                    if nums1[i] < nums2[j]:
                        result[i]  = nums2[j]
                        break
        return result

```

</details>
