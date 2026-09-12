class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s
        no_of_peaks = n//2
        return (s+m) + (no_of_peaks-1)*(m-1)