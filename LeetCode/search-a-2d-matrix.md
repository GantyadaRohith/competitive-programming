# 🟠 search-a-2d-matrix — Search a 2D Matrix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/search-a-2d-matrix/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Given a 2D matrix of integers, determine if a target value exists within the matrix.

## 🔍 Key Observation

The matrix is sorted in ascending order row-wise and column-wise, allowing for a binary search approach.

## ⚙️ Algorithm

1. Iterate through each row of the matrix until finding the row where the target could potentially be located (i.e., the row with the largest element less than or equal to the target).
2. Perform a binary search on the found row to check if the target exists.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) due to the binary search on each row.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary search` `2d matrix` `search`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(arr,k):
            l,r = 0,len(arr)-1
            while(l<=r):
                mid = l+((r-l)//2)
                if arr[mid] == k:
                    return True
                elif arr[mid] > k:
                    r = mid-1
                else:
                    l = mid+1
            return False
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                return search(matrix[i],target)
        return False
 
        
```

</details>
