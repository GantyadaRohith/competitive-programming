# 🟠 students-and-examinations — Students and Examinations

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/students-and-examinations/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Given a list of students and their subjects, find the number of exams each student has attended.

## 🔍 Key Observation

Use a CROSS JOIN to generate all possible combinations of students and subjects, then use a LEFT JOIN to count the number of exams each student has attended.

## ⚙️ Algorithm

1. Use a CROSS JOIN to generate all possible combinations of students and subjects.
2. Use a LEFT JOIN to match each student-subject combination with the corresponding exam.
3. Group the results by student and subject to count the number of exams each student has attended.
4. Order the results by student and subject.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m) due to the CROSS JOIN and LEFT JOIN operations.` | `O(n * m) for storing the results.` |

## 🏷️ Tags

`sql` `join` `count`

<details>
<summary>💻 View solution</summary>

```
SELECT 
    s.student_id,
    s.student_name,
    sj.subject_name,
    COUNT(e.subject_name) AS attended_exams 
FROM subjects sj 
CROSS JOIN Students s 
LEFT JOIN Examinations e 
    ON s.student_id = e.student_id 
   AND sj.subject_name = e.subject_name   -- Don't forget to match on subject too!
GROUP BY 
    s.student_id, 
    sj.subject_name
ORDER BY 
    s.student_id, 
    sj.subject_name;
```

</details>
