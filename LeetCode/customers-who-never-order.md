# 🟠 customers-who-never-order — Customers Who Never Order

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/customers-who-never-order/) &nbsp;|&nbsp; **Solved:** 2026-07-21

---

## 📝 Summary

Find customers who have never placed an order.

## 🔍 Key Observation

Use a left outer join to match customers with orders and filter out those with orders.

## ⚙️ Algorithm

1. Perform a left outer join between the Customers table (c1) and the Orders table (o1) on the customer ID (id). This ensures all customers are included, even those without orders.
2. Filter the result to include only those rows where the order ID (o1.id) is null, indicating no order was placed.
3. Select the customer names from the Customers table for the filtered results.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the join operation, where n is the number of customers.` | `O(1) auxiliary space, as the join operation does not require additional space proportional to the input size.` |

## 🏷️ Tags

`mysql` `left outer join` `filter` `customers` `orders`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
select name as Customers from Customers c1 left outer join Orders o1
on c1.id = o1.customerId where o1.id is null
```

</details>
