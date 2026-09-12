# 🟠 article-views-i — Article Views I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/article-views-i/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Given a table of article views, find distinct authors who viewed their own articles.

## 🔍 Key Observation

The key insight is to use a `DISTINCT` clause to ensure each author is listed only once, and to order the results by `author_id`.

## ⚙️ Algorithm

1. Select distinct `author_id` from the `Views` table where `author_id` equals `viewer_id`. This ensures that each author who viewed their own articles is included only once.
2. Order the results by `author_id` to maintain a consistent order of the authors.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the distinct operation and the order operation.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`mysql` `distinct` `order`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
select distinct author_id as id from Views where author_id = viewer_id order by author_id
```

</details>
