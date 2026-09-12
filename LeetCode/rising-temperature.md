# 🟠 rising-temperature — Rising Temperature

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rising-temperature/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Identifies days where the temperature is higher than the previous day.

## 🔍 Key Observation

Use of `datediff` to find consecutive days and compare temperatures.

## ⚙️ Algorithm

Join the `Weather` table with itself on the date difference of 1 day. Compare the temperature of the current day (`w1`) with the previous day (`w2`).

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the join operation on the `Weather` table.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`mysql` `join` `datediff` `temperature`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
select w1.id as Id from Weather w1 join Weather w2 on datediff(w1.recordDate,w2.recordDate) = 1 where w1.temperature > w2.temperature;
```

</details>
