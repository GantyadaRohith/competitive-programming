class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        vals = list(count.values())
        g = reduce(gcd, vals)
        return g >= 2