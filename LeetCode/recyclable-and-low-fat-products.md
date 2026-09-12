# 🟠 recyclable-and-low-fat-products — Recyclable and Low Fat Products

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/recyclable-and-low-fat-products/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Identify products that are both recyclable and low fat.

## 🔍 Key Observation

The query directly filters products based on the specified conditions.

## ⚙️ Algorithm

The query uses a simple `SELECT` statement with `WHERE` clauses to filter products based on the `low_fats` and `recyclable` columns. This approach is efficient and straightforward.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the number of rows in the `Products` table, as each row is processed once.` | `O(1) auxiliary space, as no additional data structures are used.` |

## 🏷️ Tags

`mysql` `query` `filter` `recyclable` `low fat`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
select product_id from Products where low_fats = 'Y' and recyclable = 'Y'
```

</details>
