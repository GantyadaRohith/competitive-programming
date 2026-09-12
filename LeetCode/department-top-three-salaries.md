# 🟠 department-top-three-salaries — Department Top Three Salaries

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/department-top-three-salaries/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Given a table of employees and their salaries, find the top three salaries in each department.

## 🔍 Key Observation

The use of DENSE_RANK() to assign a rank to each employee within their department based on salary, allowing for ties to be handled correctly.

## ⚙️ Algorithm

The solution uses a Common Table Expression (CTE) to first rank employees within each department by salary in descending order. It then selects the top three salaries from each department using a WHERE clause with the rank condition.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to the sorting operation performed by DENSE_RANK().` | `O(1) auxiliary space, as the solution does not use additional data structures that scale with input size.` |

## 🏷️ Tags

`sql` `rank` `dense_rank`

<details>
<summary>💻 View solution</summary>

```
WITH RankedEmployees AS (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.DepartmentId
            ORDER BY e.salary DESC
        ) AS dr
    FROM Employee e
    JOIN Department d
        ON e.DepartmentId = d.id
)

SELECT
    Department,
    Employee,
    Salary
FROM RankedEmployees
WHERE dr <= 3;
```

</details>
