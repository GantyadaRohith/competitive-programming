# 🟠 find-customer-referee — Find Customer Referee

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-customer-referee/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Given a table of customers and their referee IDs, find all customers who do not have a referee ID of 2 or are not assigned a referee ID.

## 🔍 Key Observation

The solution uses a simple SQL query to filter customers based on their referee ID.

## ⚙️ Algorithm

The query selects the 'name' column from the 'Customer' table where the 'referee_id' is not equal to 2 or is NULL. This effectively filters out customers who do not have a referee ID of 2 or are not assigned a referee ID.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the number of rows in the 'Customer' table, as the query processes each row once.` | `O(1) auxiliary space, as the query does not use any additional data structures that grow with the input size.` |

## 🏷️ Tags

`sql` `filter` `referee` `customer`

<details>
<summary>💻 View solution</summary>

```
SELECT name 
FROM Customer 
WHERE referee_id != 2 OR referee_id IS NULL;
```

</details>
