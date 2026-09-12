# 🟠 task-scheduler — Task Scheduler

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/task-scheduler/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Given a list of tasks and a cooldown period, determine the minimum time required to complete all tasks without violating the cooldown.

## 🔍 Key Observation

The solution involves identifying the most frequent task and calculating the idle time required to separate them.

## ⚙️ Algorithm

1. Count the frequency of each task using a dictionary.
2. Identify the maximum frequency and count how many tasks have this maximum frequency.
3. Calculate the idle time required by multiplying (maxFreq-1) by (n+1) and adding the count of tasks with maxFreq.
4. Return the maximum of the total tasks or the calculated idle time.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to counting the frequencies and iterating over them.` | `O(1) auxiliary space as the dictionary size is constant (26 for lowercase letters).` |

## 🏷️ Tags

`short` `lowercase` `task` `scheduler`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        x = defaultdict(int)
        for i in tasks:
            x[i] = x.get(i,0) + 1
        maxFreq = max(x.values())
        cnt_max = 0
        for i in x.values():
            if i == maxFreq:
                cnt_max+=1
        return max(sum(x.values()),(maxFreq-1)*(n+1)+cnt_max)
```

</details>
