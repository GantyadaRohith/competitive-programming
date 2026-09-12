# 🟠 total-hamming-distance — Total Hamming Distance

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/total-hamming-distance/) &nbsp;|&nbsp; **Solved:** 2025-12-08

---

## 📝 Summary

Calculate the total Hamming distance between all pairs of numbers in a list.

## 🔍 Key Observation

The total Hamming distance is the sum of the Hamming distances between each pair of numbers.

## ⚙️ Algorithm

Iterate over each bit position (0 to 31). For each bit position, count how many numbers have that bit set to 1 and how many have it set to 0. The total Hamming distance for that bit position is the product of these two counts. Sum these products for all bit positions to get the total Hamming distance.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`bitwise` `counting` `hamming distance`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        
        for bit in range(32):
            count1 = 0
            for num in nums:
                if num & (1 << bit):
                    count1 += 1
                    
            count0 = n - count1
            total += count1 * count0
            
        return total

```

</details>
