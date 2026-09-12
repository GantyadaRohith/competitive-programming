class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        discounts.sort(reverse = True)
        prices.sort(reverse = True)
        cost = 0.00
        for i in range(len(discounts)):
            if i == len(prices):
                break
            cost+=(prices[i] * (100 - discounts[i])) / 100
        print(cost)
        if len(discounts)<len(prices):
            cost+=sum(prices[len(discounts):])
            print(cost)
        return cost
        