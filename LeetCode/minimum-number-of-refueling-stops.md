# 🟠 minimum-number-of-refueling-stops — Minimum Number of Refueling Stops

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-refueling-stops/) &nbsp;|&nbsp; **Solved:** 2026-05-02

---

## 📝 Summary

Given a car with a certain amount of fuel and a list of gas stations along the way, determine the minimum number of refueling stops required to reach the target destination.

## 🔍 Key Observation

Using a max-heap to always refuel at the station with the most fuel available ensures the car can reach the target with the minimum number of stops.

## ⚙️ Algorithm

1. Initialize a max-heap to store the fuel at each station that can be refueled from the current position.
2. Iterate through the stations, adding fuel to the heap if the station is reachable from the current position.
3. If the car runs out of fuel and the heap is empty, return -1 (impossible to reach the target).
4. Otherwise, refuel the car from the station with the most fuel available and increment the stop count.
5. Repeat steps 2-4 until the car reaches the target or cannot reach it.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to the heap operations.` | `O(n) auxiliary space for the heap.` |

## 🏷️ Tags

`short` `lowercase` `topic` `tags`

<details>
<summary>💻 View solution</summary>

```python
import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxheap = []
        fuel = startFuel
        n = len(stations)
        stopC = 0
        i = 0
        while fuel < target:
            while i < n and stations[i][0] <= fuel:
                heapq.heappush(maxheap,-stations[i][1])
                i+=1
            if not maxheap :
                return -1
            fuel += -heapq.heappop(maxheap)
            stopC += 1
        return stopC
```

</details>
