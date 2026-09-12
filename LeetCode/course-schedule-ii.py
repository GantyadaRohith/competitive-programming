from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = {}  
        stack = []

        def dfs(node):
            if node in visited:
                if visited[node] == 1:
                    return False  
                return True      

            visited[node] = 1 

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visited[node] = 2 
            stack.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return stack[::-1]