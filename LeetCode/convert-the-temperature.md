# 🟠 convert-the-temperature — Convert the Temperature

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/convert-the-temperature/) &nbsp;|&nbsp; **Solved:** 2025-12-19

---

## 📝 Summary

Convert a temperature from Celsius to Kelvin and Fahrenheit.

## 🔍 Key Observation

The solution uses a straightforward mathematical formula to convert temperatures.

## ⚙️ Algorithm

The code defines a function `convertTemperature` that takes a temperature in Celsius as input. It returns a list containing the temperature in Kelvin and Fahrenheit. The conversion formulas are applied directly to the input Celsius value.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `conversion` `temperature`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15,celsius*1.80 +32.00]
        
```

</details>
