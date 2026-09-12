# 🟠 number-of-elapsed-seconds-between-two-times — Number of Elapsed Seconds Between Two Times

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/) &nbsp;|&nbsp; **Solved:** 2026-07-17

---

## 📝 Summary

Calculate the number of seconds between two given times.

## 🔍 Key Observation

Convert times to total seconds and subtract to find the elapsed time.

## ⚙️ Algorithm

1. Convert each time string to hours, minutes, and seconds.
2. Calculate the total seconds for both start and end times.
3. Subtract the start time from the end time to get the elapsed seconds.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time conversions and arithmetic operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `time` `conversion`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        hr1,min1,sec1 = int(startTime[0:2]),int(startTime[3:5]),int(startTime[6:])
        hr2,min2,sec2 = int(endTime[0:2]),int(endTime[3:5]),int(endTime[6:])
        st = hr1*3600 + min1 * 60 + sec1
        et = hr2*3600 + min2 * 60 + sec2
        print(hr2,min2,sec2)
        return et-st
        
```

</details>
