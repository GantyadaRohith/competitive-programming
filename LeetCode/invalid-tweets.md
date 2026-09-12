# 🟠 invalid-tweets — Invalid Tweets

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-unknown-555555?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/invalid-tweets/) &nbsp;|&nbsp; **Solved:** 2026-06-04

---

## 📝 Summary

Identify tweets with content longer than 15 characters.

## 🔍 Key Observation

The length of the content column determines if a tweet is invalid.

## ⚙️ Algorithm

The query selects tweet_id from the Tweets table where the length of the content column is greater than 15 characters.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the need to process each tweet.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`mysql` `short` `lowercase` `query` `tags`

<details>
<summary>💻 View solution</summary>

```
# Write your MySQL query statement below
select tweet_id from Tweets where length(content) >15
```

</details>
