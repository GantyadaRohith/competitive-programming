# 🟠 average-time-of-process-per-machine — Average Time of Process per Machine

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/average-time-of-process-per-machine/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Calculate the average processing time for each machine based on start and end activities.

## 🔍 Key Observation

Use a Common Table Expression (CTE) to join start and end activities for each machine and calculate the duration.

## ⚙️ Algorithm

1. Create a CTE named `act` that joins the `Activity` table with itself on `machine_id` and `process_id` to find the duration of each process.
2. Filter the joined table to include only 'start' and 'end' activities.
3. Calculate the duration by subtracting the start timestamp from the end timestamp.
4. Group the results by `machine_id` and calculate the average processing time using `AVG()` with 3 decimal places.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting the joined table.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sql` `average` `processing` `time` `machine`

<details>
<summary>💻 View solution</summary>

```
WITH act AS (
    SELECT 
        p1.machine_id,
        (p2.timestamp - p1.timestamp) AS process_duration
    FROM Activity p1 
    JOIN Activity p2 
      ON p1.machine_id = p2.machine_id 
     AND p1.process_id = p2.process_id 
    WHERE p1.activity_type = 'start' 
      AND p2.activity_type = 'end'
)

SELECT 
    machine_id, 
    ROUND(AVG(process_duration), 3) AS processing_time 
FROM act 
GROUP BY machine_id;
```

</details>
