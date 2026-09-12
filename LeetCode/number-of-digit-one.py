class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        s = str(n)
        digits = len(s)
        base = 10 ** (digits - 1)
        msd = n // base
        rest = n % base

        # Count 1s contributed by the most significant digit
        if msd == 1:
            ones_msd = rest + 1
        else:
            ones_msd = base

        # Count 1s in lower positions
        ones_lower = msd * (digits - 1) * (base // 10)

        # Recursive call
        return ones_msd + ones_lower + self.countDigitOne(rest)