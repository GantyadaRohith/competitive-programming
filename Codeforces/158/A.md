# 🔵 158A — Next Round

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/158/A) &nbsp;|&nbsp; **Solved:** 2026-07-27

---

## 📝 Summary

Given an array of integers and a number k, find the maximum number of elements that can be selected such that no two selected elements are consecutive.

## 🔍 Key Observation

The problem can be solved using a greedy approach by sorting the array and selecting elements from the end.

## ⚙️ Algorithm

1. Read the input values n and k, and the array a of integers.
2. Create a dictionary d to count the frequency of each element in the array.
3. Convert the dictionary to a list of tuples and sort it in descending order based on the element values.
4. Initialize a variable count to 0 and an index i to 0.
5. While count is less than k and i is less than or equal to the length of the sorted list:
   - If the current element is 0, break the loop.
   - Add the frequency of the current element to count.
   - Increment i by 1.
6. Print the value of count.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(n) auxiliary space.` |

## 🏷️ Tags

`short` `implementation` `greedy`

<details>
<summary>💻 View solution</summary>

```python
n,k = map(int,input().split())
a = list(map(int,input().split()))
d = {}
count = 0
for i in a:
    d[i] = d.get(i,0) + 1
d = list(d.items())
d.sort(key = lambda x:x[0],reverse= True)
i = 0
while count<k and i <= len(d)-1:
    if d[i][0] == 0:
        break
    count+=d[i][1]
    i+=1
print(count)
```

</details>
