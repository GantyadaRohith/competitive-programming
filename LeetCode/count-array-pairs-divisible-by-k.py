class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        gcd_values = [math.gcd(num, k) for num in nums]
        freq = Counter(gcd_values)

        ans = 0
        gcd_keys = list(freq.keys())

        for i in range(len(gcd_keys)):
            g1 = gcd_keys[i]

            for j in range(i, len(gcd_keys)):
                g2 = gcd_keys[j]

                if (g1 * g2) % k == 0:
                    if i == j:
                        c = freq[g1]
                        ans += c * (c - 1) // 2
                    else:
                        ans += freq[g1] * freq[g2]

        return ans