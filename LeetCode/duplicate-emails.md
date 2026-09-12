# 🟠 duplicate-emails — Duplicate Emails

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/duplicate-emails/) &nbsp;|&nbsp; **Solved:** 2026-07-21

---

## 📝 Summary

Identify duplicate email addresses in a database table.

## 🔍 Key Observation

Grouping by email and using the HAVING clause to filter out emails with a count greater than 1.

## ⚙️ Algorithm

The solution uses a SQL query to group the emails in the 'Person' table by their values. It then filters the groups to include only those with more than one occurrence, effectively identifying duplicate email addresses.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting the grouped emails.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`mysql` `grouping` `filtering` `duplicates`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
select email as Email from Person group by(email) having count(*) > 1 
```

</details>
