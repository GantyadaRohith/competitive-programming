# 🟠 customer-who-visited-but-did-not-make-any-transactions — Customer Who Visited but Did Not Make Any Transactions

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Find customers who visited but did not make any transactions.

## 🔍 Key Observation

Use a common table expression (CTE) to identify customers who have not made any transactions.

## ⚙️ Algorithm

1. Create a CTE `noTrans` that joins `Visits` and `Transactions` tables on `visit_id`. This CTE will include all visits and their corresponding transactions, or NULL if no transaction exists for a visit.
2. Select customers from `noTrans` where `transaction_id` is NULL, indicating they did not make any transactions.
3. Group the results by `customer_id` and count the number of such customers.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`mysql` `cte` `join` `count`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
with noTrans as (
    select v.customer_id,t.transaction_id from Visits v left join Transactions t on v.visit_id = t.visit_id
)

select customer_id,count(*) as count_no_trans from noTrans where transaction_id is null group by customer_id;
```

</details>
