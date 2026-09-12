# 🟠 second-highest-salary — Second Highest Salary

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/second-highest-salary/) &nbsp;|&nbsp; **Solved:** 2026-07-22

---

## 📝 Summary

Find the second highest salary in a table of employee salaries.

## 🔍 Key Observation

Use a subquery to find the maximum salary and then select the maximum salary that is less than this maximum.

## ⚙️ Algorithm

1. Use a subquery to find the maximum salary in the Employee table.
2. Select the maximum salary that is less than the maximum salary found in step 1.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sql` `subquery` `max` `second highest`

<details>
<summary>💻 View solution</summary>

```
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
```

</details>
