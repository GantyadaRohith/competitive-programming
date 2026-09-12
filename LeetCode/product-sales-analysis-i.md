# 🟠 product-sales-analysis-i — Product Sales Analysis I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/product-sales-analysis-i/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Given a table of sales and a table of products, join the tables to provide a list of product names, years, and prices.

## 🔍 Key Observation

The task requires joining two tables based on a common column to retrieve specific product details.

## ⚙️ Algorithm

1. Use the SQL `JOIN` clause to combine rows from the `Sales` and `Product` tables based on the `product_id` column, which is common to both tables.
2. Select the `product_name`, `year`, and `price` columns from the `Sales` table to display the required information.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the join operation, where n is the number of rows in the `Sales` table.` | `O(1) auxiliary space, as the join operation does not require additional space proportional to the input size.` |

## 🏷️ Tags

`mysql` `join` `product sales`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
select p.product_name,s.year,s.price from Sales as s join Product as p on s.product_id = p.product_id;
```

</details>
