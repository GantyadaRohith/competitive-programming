from collections import defaultdict
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}

        # Build [first, last] interval for each character
        for i, ch in enumerate(s):
            if ch not in intervals:
                intervals[ch] = [i, i]
            else:
                intervals[ch][1] = i

        # Sort intervals by their starting index
        intervals = sorted(intervals.values(), key=lambda x: x[0])

        merged = []

        # Merge overlapping intervals
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        # Convert merged intervals to partition lengths
        return [end - start + 1 for start, end in merged]