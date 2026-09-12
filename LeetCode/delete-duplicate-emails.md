# 🟠 delete-duplicate-emails — Delete Duplicate Emails

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/delete-duplicate-emails/) &nbsp;|&nbsp; **Solved:** 2026-07-21

---

## 📝 Summary

Delete duplicate email addresses from the Person table.

## 🔍 Key Observation

Identify and remove duplicate email addresses by comparing each email with every other email in the table.

## ⚙️ Algorithm

The solution uses a self-join to compare each row with every other row in the Person table. It deletes the second occurrence of each duplicate email by comparing the email addresses and the IDs of the rows.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loops in the self-join.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`mysql` `self-join` `duplicate-emails`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
DELETE p2 FROM Person p1, Person p2
WHERE p1.Email = p2. Email AND p1.Id < p2.Id
```

</details>
