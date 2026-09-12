# 🟠 nth-highest-salary — Nth Highest Salary

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/nth-highest-salary/) &nbsp;|&nbsp; **Solved:** 2026-06-02

---

## 📝 Summary

Find the Nth highest salary from a table of employee salaries.

## 🔍 Key Observation

Use a subquery with ORDER BY and LIMIT to efficiently find the Nth highest salary.

## ⚙️ Algorithm

1. Subtract 1 from N to adjust for zero-based indexing.
2. Use a subquery to order the salaries in descending order.
3. Apply LIMIT 1 to get the highest salary.
4. Use OFFSET N to skip the first N salaries and get the Nth highest.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sql` `subquery` `sorting` `offset`

<details>
<summary>💻 View solution</summary>

```
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
  RETURN (
        select DISTINCT salary from employee order by salary desc limit 1 offset N
  );
END
```

</details>
