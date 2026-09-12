# 🟠 gas-station — Gas Station

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/gas-station/) &nbsp;|&nbsp; **Solved:** 2026-07-25

---

## 📝 Summary

Given a list of gas stations with their respective gas and cost, determine if a car can complete a full circuit starting from any station.

## 🔍 Key Observation

The solution uses a greedy approach to find the starting station by maintaining a running total of gas and cost differences.

## ⚙️ Algorithm

1. Check if the total gas is less than the total cost. If so, return -1 as it's impossible to complete the circuit.
2. Initialize a variable `start_index` to 0 and `current_tank` to 0.
3. Iterate through the gas stations, updating `current_tank` by adding the gas at the current station and subtracting the cost.
4. If `current_tank` becomes negative, it means the car cannot reach the current station from the previous start station. Update `start_index` to the next station and reset `current_tank` to 0.
5. After the loop, `start_index` will be the starting station that allows the car to complete the circuit.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the number of gas stations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`greedy` `array` `simulation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, it's impossible
        if sum(gas) < sum(cost):
            return -1
        
        start_index = 0
        current_tank = 0
        
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
                
        return start_index
```

</details>
