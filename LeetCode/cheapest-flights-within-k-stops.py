class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            temp = dist.copy()
            for u, v, w in flights:
                if dist[u] != float('inf'):
                    temp[v] = min(temp[v], dist[u] + w)
            dist = temp

        return dist[dst] if dist[dst] != float('inf') else -1