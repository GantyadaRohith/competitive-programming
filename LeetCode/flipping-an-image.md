# 🟠 flipping-an-image — Flipping an Image

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/flipping-an-image/) &nbsp;|&nbsp; **Solved:** 2025-12-03

---

## 📝 Summary

Flips and inverts each row of a binary image.

## 🔍 Key Observation

Flipping and inverting can be done in a single pass through the image.

## ⚙️ Algorithm

1. Reverse each row of the image.
2. For each element in the row, invert its value (0 to 1 or 1 to 0).

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `topic` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i.reverse()
            for j in range(len(i)):
                if i[j] == 1:
                    i[j] = 0
                else:
                    i[j] = 1
        return image
```

</details>
