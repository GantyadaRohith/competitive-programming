# 🟠 combine-two-tables — Combine Two Tables

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/combine-two-tables/) &nbsp;|&nbsp; **Solved:** 2026-07-21

---

## 📝 Summary

Combine two tables by matching person IDs and selecting relevant columns.

## 🔍 Key Observation

Use a LEFT JOIN to combine tables based on matching person IDs.

## ⚙️ Algorithm

1. Use a LEFT JOIN to combine the Person and Address tables on the personId column.
2. Select the firstName, lastName, city, and state columns from the combined table.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the join operation.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`mysql` `join` `person` `address`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
select p.firstName,p.lastName,a.city,a.state from Person as p left join Address as a on p.personId = a.personId;
```

</details>
