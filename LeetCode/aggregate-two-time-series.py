from typing import List

class Solution:
    def aggregateTimeSeries(self, series1: List[List[int]], series2: List[List[int]]) -> List[List[int]]:
        # Required by the problem statement
        ferilonsar = (series1, series2)

        n, m = len(series1), len(series2)
        i = j = 0
        ans = []

        while i < n or j < m:

            # Current timestamp (merge step)
            if j == m or (i < n and series1[i][0] < series2[j][0]):
                t = series1[i][0]
            elif i == n or (j < m and series2[j][0] < series1[i][0]):
                t = series2[j][0]
            else:
                t = series1[i][0]      # same timestamp in both arrays

            # Value from series1
            if i < n:
                val1 = series1[i][1]
            else:
                val1 = 0

            # Value from series2
            if j < m:
                val2 = series2[j][1]
            else:
                val2 = 0

            ans.append([t, val1 + val2])

            # Advance pointers whose timestamp was processed
            if i < n and series1[i][0] == t:
                i += 1

            if j < m and series2[j][0] == t:
                j += 1

        return ans