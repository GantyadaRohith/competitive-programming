# 🟠 course-schedule-iii — Course Schedule III

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/course-schedule-iii/) &nbsp;|&nbsp; **Solved:** 2026-02-28

---

## 📝 Summary

Given a list of courses with start and end times, determine the maximum number of courses that can be taken without overlapping.

## 🔍 Key Observation

The key insight is to use a min-heap to always take the course with the earliest end time first, ensuring that the total time taken does not exceed the end time of the current course.

## ⚙️ Algorithm

1. Sort the courses by their end times. This allows us to process courses in order of their end times, ensuring that we can always take the course with the earliest end time first.
2. Initialize a min-heap to keep track of the durations of the courses we are taking.
3. Iterate through each course:
   a. Add the course duration to the total time taken.
   b. Push the course duration onto the min-heap.
   c. If the total time taken exceeds the end time of the current course, remove the course with the earliest end time from the min-heap and subtract its duration from the total time taken.
   d. Increment the count of courses taken.
4. Return the count of courses taken.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting the courses.` | `O(n) auxiliary space for the min-heap.` |

## 🏷️ Tags

`short` `lowercase` `topic` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x:x[1])
        time_taken = 0
        cnt = 0
        mindur = []
        for d,l in courses:
            time_taken +=d
            heapq.heappush(mindur,-d)
            cnt+=1
            if time_taken>l:
                time_taken-=(-heapq.heappop(mindur))
                cnt-=1
        return cnt
```

</details>
