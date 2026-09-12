# 🟠 flood-fill — Flood Fill

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/flood-fill/) &nbsp;|&nbsp; **Solved:** 2026-08-02

---

## 📝 Summary

Given an image represented as a 2D list, change the color of a specified pixel and all connected pixels of the same color to a new color.

## 🔍 Key Observation

The problem is a classic graph traversal problem where we need to visit all connected components of a specific color.

## ⚙️ Algorithm

The solution uses Depth-First Search (DFS) to traverse the image. It starts from the specified pixel and changes its color. It then recursively visits all connected pixels of the same color, ensuring no pixel is visited more than once.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the total number of pixels in the image, as each pixel is visited once.` | `O(n) for the recursion stack in the worst case, where all pixels are of the same color.` |

## 🏷️ Tags

`dfs` `image-processing` `flood-fill`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row,cols = len(image),len(image[0])
        old_color = image[sr][sc]
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        if old_color == color:
            return image
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=cols:
                return
            if image[r][c] != old_color:
                return
            image[r][c] = color
            for dr,dc in d:
                dfs(r+dr,c+dc)
        dfs(sr,sc)
        return image
```

</details>
