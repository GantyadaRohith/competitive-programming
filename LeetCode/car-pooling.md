# 🟠 car-pooling — Car Pooling

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/car-pooling/) &nbsp;|&nbsp; **Solved:** 2025-11-27

---

## 📝 Summary

Given a list of trips and a car's capacity, determine if the car can complete all trips without exceeding capacity.

## 🔍 Key Observation

Sort the trips by their start and end times to process them in order.

## ⚙️ Algorithm

1. Create a list of events (start and end times) for each trip, with a positive value for start times and negative values for end times.
2. Sort the events by time.
3. Iterate through the sorted events, updating the current number of passengers on the car.
4. If at any point the number of passengers exceeds the car's capacity, return False.
5. If all trips can be completed without exceeding capacity, return True.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(n) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `carpooling` `events`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        out = []
        for i in trips:
         ppl,fro,to = i[0],i[1],i[2]
         out.append([fro,ppl])
         out.append([to,-ppl])
        out.sort()
        curr = 0
        possible = 1 
        for loc,ppl in out:
            curr+=ppl
            if curr > capacity:
                possible = 0
                break
        return False if possible == 0 else True
```

</details>
