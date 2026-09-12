from typing import List
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        i=0
        for x,y in equations:
            graph[x].append([y,values[i]])
            graph[y].append([x,1/values[i]])
            i+=1
        def dfs(src, dst, visited):
            if src not in graph:
                return -1.0

            if src == dst:
                return 1.0

            visited.add(src)

            for neighbor, weight in graph[src]:
                if neighbor not in visited:
                    result = dfs(neighbor, dst, visited)
                    if result != -1.0:
                        return result * weight

            return -1.0
        result = []
        for x,y in queries:
            result.append(dfs(x,y,set())) 
        return result
        