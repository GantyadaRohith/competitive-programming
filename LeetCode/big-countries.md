# 🟠 big-countries — Big Countries

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/big-countries/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Select countries with an area greater than or equal to 3,000,000 square kilometers or a population greater than or equal to 25,000,000.

## 🔍 Key Observation

Use a simple `SELECT` statement with a `WHERE` clause to filter countries based on their area and population.

## ⚙️ Algorithm

The solution involves writing a SQL query that selects countries from the `World` table where the `area` is greater than or equal to 3,000,000 or the `population` is greater than or equal to 25,000,000. This is achieved using the `OR` operator to combine the two conditions.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the number of rows in the `World` table, as the query needs to scan through each row to determine if it meets the criteria.` | `O(1) auxiliary space, as the query does not use any additional data structures that grow with the input size.` |

## 🏷️ Tags

`mysql` `query` `world` `countries`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
select name,population,area from World where area >= 3000000 or population >=25000000
```

</details>
