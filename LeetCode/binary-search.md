# 🟠 binary-search — Binary Search

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-cpp-00599C?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/binary-search/) &nbsp;|&nbsp; **Solved:** 2026-07-06

---

## 📝 Summary

Given a sorted array and a target value, find the index of the target value or return -1 if it is not present.

## 🔍 Key Observation

The binary search algorithm efficiently narrows down the search space by repeatedly dividing it in half.

## ⚙️ Algorithm

1. Initialize two pointers, `first` and `last`, to the start and end of the array, respectively.
2. Calculate the middle index `mid`.
3. While `first` is less than `last`:
   - If the element at `mid` is equal to the target, return `mid`.
   - If the element at `mid` is less than the target, move `first` to `mid + 1` to search in the right half.
   - Otherwise, move `last` to `mid` to search in the left half.
4. If the loop exits without finding the target, return -1.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) due to the binary search algorithm.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary` `search` `algorithm`

<details>
<summary>💻 View solution</summary>

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int first = 0;
        int last = nums.size(); // Correctly get the vector size
        int mid = (first + last) / 2;

        while (first < last) {
            if (nums[mid] == target) {
                return mid; // Target found, return index
            } else {
                if (nums[mid] < target) {
                    first = mid + 1; // Search in the right half
                } else {
                    last = mid; // Search in the left half
                }
            }
            mid = (first + last) / 2; // Recalculate mid
        }
        return -1; // Target not found
    }
};
```

</details>
