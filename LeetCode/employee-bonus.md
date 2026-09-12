# 🟠 employee-bonus — Employee Bonus

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/employee-bonus/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Given an employee table and a bonus table, find employees who do not have a bonus or have a bonus less than 1000.

## 🔍 Key Observation

Use a LEFT JOIN to combine employees with their bonuses, then filter based on the bonus condition.

## ⚙️ Algorithm

1. Perform a LEFT JOIN between the Employee and Bonus tables on empId to include all employees, even those without bonuses.
2. Filter the result to include only rows where the bonus is NULL or less than 1000.
3. Select the employee's name and bonus.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the join operation, where n is the number of employees.` | `O(1) auxiliary space, as no additional data structures are used.` |

## 🏷️ Tags

`sql` `join` `filter`

<details>
<summary>💻 View solution</summary>

```
SELECT 
    e.name, 
    b.bonus 
FROM Employee e 
LEFT JOIN Bonus b 
    ON e.empId = b.empId 
WHERE b.bonus IS NULL 
   OR b.bonus < 1000;
```

</details>
