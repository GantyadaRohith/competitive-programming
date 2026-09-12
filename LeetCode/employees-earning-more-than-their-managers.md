# 🟠 employees-earning-more-than-their-managers — Employees Earning More Than Their Managers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/employees-earning-more-than-their-managers/) &nbsp;|&nbsp; **Solved:** 2026-07-21

---

## 📝 Summary

Find employees who earn more than their managers.

## 🔍 Key Observation

Use a common table expression (CTE) to identify managers and then compare their salaries with their employees.

## ⚙️ Algorithm

1. Create a CTE named 'manager' that selects all rows from the 'employee' table where 'managerId' is not null.
2. Select the 'name' column from the 'employee' table where the 'id' matches the 'managerId' in the 'manager' CTE and the 'salary' is greater than the 'salary' in the 'manager' CTE.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the join operation between the 'employee' and 'manager' CTEs.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`mysql` `cte` `join`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
with manager as(
    select * from employee where managerId is not NUll
)
select m.name as Employee from Employee as e,manager as m where m.managerId=e.id and e.salary<m.salary;
```

</details>
